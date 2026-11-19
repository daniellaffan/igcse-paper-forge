"""Generator for Cambridge IGCSE Spanish 0530 (Listening, Reading, Speaking, Writing).

    .venv/bin/python scripts/gen/spanish.py

Content (all original) lives in spanish_c*.py, one dict per sub-topic ref:
  scene  settings for the short-recordings task          ({fr} friend, {city})
  ex     "lead#utterance#question#category" picture items  ({v} = category value)
  signs  (setting, "sign#sentence" lines)
  ann    announcement: title, desc, sp, open, close, facts "s#q#opts"
  theme  what the speakers talk about ("habla sobre ...")
  facts  "s#iq#q#a#rej#opts#t#f#lvl"  (first-person statement, interviewer question,
         third-person question, mark-scheme answer, refuse note, 4 options (first
         correct, or *x = the alternatives of variable x), true paraphrase, false
         statement, level 1-3)
  tema   conversation / writing title;  tq "tag#question#alternative#indicative"
  rp     role plays: ctx ["context#teacher role"], slots [5 x "q#expected"]
  form   titles, ctx, gaps "label#accept#refuse#n"
  ads    (title, "need#offer#near-miss" lines)
Markup inside content: {x=a|b|c} variable (chosen once per question, reused as {x});
<m|f> narrator-gender form; [a|b] free stylistic choice; {N} narrator's name.
"""
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Bank, row, levels  # noqa: E402
import spanish_lex as LX  # noqa: E402
import spanish_spec as SP  # noqa: E402
import spanish_ca, spanish_cb, spanish_cc, spanish_cd, spanish_ce  # noqa: E402
import spanish_scen as SC  # noqa: E402
from spanish_pictures import PICS  # noqa: E402


def pic(cap):
    """What the printed picture looks like: two captions with the same drawing can't both be options."""
    return PICS.get(cap, cap)

CONTENT = {}
for _m in (spanish_ca, spanish_cb, spanish_cc, spanish_cd, spanish_ce):
    CONTENT.update(_m.C)
# role plays and forms are scenario records (one context + its own questions/fields)
for _r, _c in CONTENT.items():
    assert "rp" not in _c and "form" not in _c, f"{_r}: role plays/forms live in spanish_scen.py"
    if _r in SC.RP:
        _c["rp"] = SC.RP[_r]
    if _r in SC.FORMS:
        _c["form"] = SC.FORMS[_r]

PER_CELL = 13
LET = "ABCDEFGHIJ"
PAPER = {"l": "p1", "r": "p2", "s": "p3", "w": "p4"}

VAR_DEF = re.compile(r"\{(\w+)=([^{}]+)\}")
VAR_REF = re.compile(r"\{(\w+)\}")
GEN = re.compile(r"<([^<>|]*)\|([^<>|]*)>")
FREE = re.compile(r"\[([^\[\]]*\|[^\[\]]*)\]")


# ------------------------------------------------------------------ rendering

class Env(dict):
    pass


def person(rnd, gender=None, used=(), learner=False, need=None):
    """One narrator = one coherent profile: name, gender and ONE place record with true attributes.
    need: optional predicate on the tag set (e.g. lambda t: "spain" in t)."""
    g = gender or rnd.choice("mf")
    pool = [n for n in (LX.MALE if g == "m" else LX.FEMALE) if n not in used]
    name = rnd.choice(pool)
    places = LX.LEARNER_PLACES if learner else LX.PLACES
    prof = LX.LEARNER_PROFILE if learner else LX.PROFILE
    if need:
        places = [pl for pl in places if need(set(prof[pl[0]][1].split()))] or places
    city, country, nm, nf = rnd.choice(places)
    reg, tags = prof[city]
    tags = set(tags.split()) | {country.lower()}
    env = Env(N=name, g=g, city=city, country=country, nat=nm if g == "m" else nf,
              sur=rnd.choice(LX.SURNAMES), vars={}, tags=tags, reg=reg,
              cur=LX.CURRENCY.get(country, "euros"))
    # profile variables usable in facts as {reg} with options *reg
    env["vars"]["reg"] = (reg, list(LX.REGIONS))
    return env


def narrator(c, rnd, **kw):
    return person(rnd, learner=c.get("narrator") == "learner", **kw)


def choose_vars(texts, env, rnd):
    for t in texts:
        for m in VAR_DEF.finditer(t or ""):
            k = m.group(1)
            if k not in env["vars"]:
                alts = [a.strip() for a in m.group(2).split("|")]
                env["vars"][k] = (rnd.choice(alts), alts)


def render(t, env, rnd):
    if not t:
        return ""
    t = VAR_DEF.sub(lambda m: env["vars"][m.group(1)][0], t)

    def ref(m):
        k = m.group(1)
        if k in env["vars"]:
            return env["vars"][k][0]
        if k in env:
            return str(env[k])
        return m.group(0)
    t = VAR_REF.sub(ref, t)
    gi = 0 if env.get("g", "m") == "m" else 1
    t = GEN.sub(lambda m: m.group(1 + gi), t)
    t = FREE.sub(lambda m: rnd.choice(m.group(1).split("|")), t)
    return re.sub(r"\s+([,.;:?!])", r"\1", re.sub(r"  +", " ", t)).strip()


def both(t):
    """Text addressed to an unknown candidate: print both gender forms (enferm<o|a> -> enfermo/a)."""
    return GEN.sub(lambda m: m.group(1) + "/" + m.group(2), t or "")


def contract(t):
    """Obligatory Spanish contractions: de + el -> del, a + el -> al (not before the pronoun él)."""
    t = re.sub(r"\b([Dd])e el\b", lambda m: m.group(1) + "el", t)
    return re.sub(r"\b([Aa]) el\b", lambda m: m.group(1) + "l", t)


LEFTOVER = ("<", "|>", "{", "}")


def finalize(d, where=""):
    """Apply contractions to every output string and refuse any unrendered template markup."""
    if isinstance(d, str):
        t = contract(d)
        for tok in LEFTOVER:
            if tok in t:
                raise ValueError(f"template markup {tok!r} left in output ({where}): {t[:200]}")
        return t
    if isinstance(d, list):
        return [finalize(x, where) for x in d]
    if isinstance(d, tuple):
        return tuple(finalize(x, where) for x in d)
    if isinstance(d, dict):
        return {k: finalize(v, where) for k, v in d.items()}
    return d


def de(t):
    """Spanish 'de' + phrase, contracting de + el."""
    return "del " + t[3:] if t.startswith("el ") else "de " + t


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def lines(block):
    return [l.strip() for l in (block or "").strip().split("\n") if l.strip() and not l.strip().startswith("//")]


FACT_KEYS = ["s", "iq", "q", "a", "rej", "opts", "t", "f", "lvl"]


def facts_of(c):
    """Fact lines have 9 fields plus an optional 10th, cond: space-separated profile tags the
    narrator's place must have ("temperate") or must not have ("!capital"); "+trait" says the fact
    gives the narrator a trait ("+veg") and "-trait" that it cannot go with that trait ("-veg"),
    so pick_facts never puts contradicting facts in one narrator's text.  A statement that
    starts with ^ continues the previous fact (it refers back to it) and is only used with it."""
    out = []
    for i, l in enumerate(lines(c["facts"])):
        bits = [b.strip() for b in l.split("#")]
        assert len(bits) in (9, 10), (l, len(bits))
        d = dict(zip(FACT_KEYS, bits[:9]))
        d["cond"] = bits[9].split() if len(bits) == 10 else []
        d["lvl"] = int(d["lvl"])
        d["dep"] = d["s"].startswith("^")
        d["s"] = d["s"].lstrip("^").strip()
        d["i"] = i
        out.append(d)
    return out


def fits(f, p):
    tags = p.get("tags", set())
    for t in f["cond"]:
        if t[0] in "+-":
            continue  # narrator traits, checked between facts in pick_facts
        if (t[1:] in tags) if t.startswith("!") else (t not in tags):
            return False
    return True


def usable(F, p, alone=False):
    """Facts true for this narrator; with alone=True (a fact heard on its own) drop continuations."""
    ok = [f for f in F if fits(f, p)]
    ids = {f["i"] for f in ok}
    # a continuation needs its head fact
    ok = [f for f in ok if not f["dep"] or (f["i"] - 1 in ids and not alone)]
    return ok


def pick_facts(F, n, rnd):
    """n facts in text order; a continuation is always taken together with the fact before it."""
    units = []
    for f in F:
        if f["dep"] and units and units[-1][-1]["i"] == f["i"] - 1:
            units[-1].append(f)
        elif not f["dep"]:
            units.append([f])
    for _ in range(200):
        rnd.shuffle(units)
        got, k, has, bans = [], 0, set(), set()
        for u in units:
            uh = {c[1:] for f in u for c in f.get("cond", []) if c[0] == "+"}
            ub = {c[1:] for f in u for c in f.get("cond", []) if c[0] == "-"}
            if uh & bans or ub & has:
                continue  # contradicts what the narrator already says (vegetarian + ate ceviche)
            if k + len(u) <= n:
                got.append(u)
                k += len(u)
                has |= uh
                bans |= ub
            if k == n:
                break
        if k == n:
            return sorted([f for u in got for f in u], key=lambda f: f["i"])
    raise ValueError("cannot pick facts")


def inst(fact, env, rnd, nopt=4):
    """Instantiate a fact for one narrator: returns rendered fields + options (correct first)."""
    choose_vars([fact[k] for k in FACT_KEYS if k != "lvl"], env, rnd)
    r = {k: render(fact[k], env, rnd) for k in ("s", "iq", "q", "a", "rej", "t", "f")}
    o = fact["opts"]
    if o.startswith("*"):
        ch, alts = env["vars"][o[1:]]
        others = [a for a in alts if a != ch]
        rnd.shuffle(others)
        opts = [ch] + others[:nopt - 1]
    else:
        raw = [x.strip() for x in o.split(";")]
        others = raw[1:]
        rnd.shuffle(others)
        opts = [raw[0]] + others[:nopt - 1]
    r["opts"] = [cap(render(x, env, rnd)) if x[:1].isupper() else render(x, env, rnd) for x in opts]
    r["lvl"] = fact["lvl"]
    return r


def shuffle_opts(opts, rnd):
    idx = list(range(len(opts)))
    rnd.shuffle(idx)
    return [opts[i] for i in idx], idx.index(0)


def pick_ordered(seq, k, rnd):
    ix = sorted(rnd.sample(range(len(seq)), k))
    return [seq[i] for i in ix]


def labels(n):
    return [chr(97 + i) for i in range(n)]


def band_from(lv, base):
    order = ["1-3", "4-6", "7-9"]
    i = order.index(base)
    if lv >= 2.6 and i < 2:
        i += 1
    elif lv < 1.4 and i > 0:
        i -= 1
    return order[i]


def mean(xs):
    return sum(xs) / len(xs)


def paragraphs(sents, rnd, sizes=(2, 3)):
    out, cur = [], []
    target = rnd.choice(sizes)
    for s in sents:
        cur.append(s)
        if len(cur) >= target:
            out.append(" ".join(cur))
            cur, target = [], rnd.choice(sizes)
    if cur:
        out.append(" ".join(cur))
    return out


SEQ = ["Luego, ", "Después, ", "Más tarde, ", "Entonces ", "A continuación, ", ""]

# ------------------------------------------------------------------ option ambiguity

STOP = set("""el la los las un una unos unas mi mis tu su a al de del en con y o muy hace hay esta está es son
para por que se me te le lo nos the of and uno dos tres cuatro cinco seis siete ocho nueve diez once doce
quince veinte treinta cincuenta cien doscientos quinientos medio media y_ con_""".split())


def _deacc(w):
    return w.translate(str.maketrans("áéíóúüÁÉÍÓÚÜ", "aeiouuAEIOUU"))


def _stem(w):
    if len(w) > 4 and w.endswith("es"):
        return w[:-2]
    if len(w) > 3 and w.endswith("s"):
        return w[:-1]
    return w


def words(t):
    return {_stem(_deacc(w)) for w in re.findall(r"[a-záéíóúñü]+", (t or "").lower()) if w not in STOP}


_CONCEPT = {_stem(_deacc(k)): v for k, v in LX.CONCEPT.items()}
_SYN = {_stem(_deacc(k)): words(v) for k, v in LX.SYNONYMS.items()}
_GENERIC = {}
for _cat, _vals in LX.CATS.items():
    _cnt = {}
    for _es, _en in _vals:
        for _w in words(_es):
            _cnt[_w] = _cnt.get(_w, 0) + 1
    _GENERIC[_cat] = {w for w, n in _cnt.items() if n >= 3}


def concepts(val, cat):
    """Key concepts of one option value: its distinctive words, their synonyms and the country
    concept (francesa / Francia / el francés all share 'francesa')."""
    ws = words(val) - _GENERIC.get(cat, set())
    out = set(ws)
    for w in ws:
        out |= _SYN.get(w, set())
        if w in _CONCEPT:
            out.add("@" + _CONCEPT[w])
    return out


def ambiguous(sentences, opts, keys):
    """opts: [(value, cat)]; keys[k] = index of the option keyed for sentences[k].
    True if two options share a key concept, or a sentence mentions the concept of an option
    other than its keyed one (so more than one option could fit it)."""
    cs = [concepts(v, cat) for v, cat in opts]
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            if cs[i] & cs[j]:
                return True
    for k, sent in enumerate(sentences):
        sw = words(sent)
        sw |= {"@" + _CONCEPT[w] for w in sw if w in _CONCEPT}
        for j, c in enumerate(cs):
            if j != keys[k] and c & sw:
                return True
    return False


def plural(v):
    w = v.split()
    if w[0] in ("los", "las", "unos", "unas"):
        return True
    if w[0] in ("el", "la", "un", "una", "mi"):
        return False
    return w[-1].endswith("s") and len(w) == 1


DETS = {"el", "la", "los", "las", "un", "una", "unos", "unas", "mi", "mis", "tu", "tus", "su", "sus", "este", "esta", "estos", "estas"}
LIKE_V = re.compile(r"\b((?:me|te|le|nos|les) (?:gust|encant|interes|molest|chifl)\w*(?: nada| mucho| más| bastante)?) \{v\}")


def with_article(utt, v):
    """Gustar-type verbs take a definite article before a bare plural noun: 'no me gustan nada los pimientos'."""
    w = v.split()[0].lower()
    if w in DETS or re.search(r"(ar|er|ir)$", w) or not plural(v):
        return utt
    return LIKE_V.sub(lambda m: m.group(1) + (" las " if w.endswith("as") else " los ") + "{v}", utt)


def val_env(base, v):
    e = Env(base)
    e["vars"] = {}
    e["v"] = v[0]
    e["n"] = "n" if plural(v[0]) else ""
    return e


def needs_spain(c):
    return any(l.split("#")[-1].strip() == "precio" for l in lines(c.get("ex", "")))


# ------------------------------------------------------------------ Listening

def b_l_short(c, rnd):
    exs = lines(c["ex"])
    fr = person(rnd, need=(lambda t: "spain" in t) if needs_spain(c) else None)
    base = Env(fr=fr["N"], city=fr["city"], g=fr["g"], vars={})
    for _ in range(100):
        chosen = rnd.sample(exs, 8) if len(exs) >= 8 else (exs + rnd.sample(exs, 8 - len(exs)))
        used, items, bad = set(), [], False
        for e in chosen:
            lead, utt, qq, cat = [x.strip() for x in e.split("#")]
            vals = [v for v in LX.CATS[cat] if not (concepts(v[0], cat) & used)]
            rnd.shuffle(vals)
            if len(vals) < 4:
                bad = True
                break
            good = vals[0]
            dis, shown = [], {pic(good[1])}
            for v in vals[1:]:
                if pic(v[1]) not in shown and len(dis) < 3:
                    dis.append(v)
                    shown.add(pic(v[1]))
            if len(dis) < 3:
                bad = True
                break
            utt = with_article(utt, good[0])
            env = val_env(base, good)
            sent = render(utt, env, rnd)
            if ambiguous([sent], [(o[0], cat) for o in [good] + dis], [0]):
                bad = True
                break
            used |= concepts(good[0], cat)
            items.append((lead, utt, qq, cat, good, dis, env))
        if not bad:
            break
    else:
        raise ValueError("l-short: no unambiguous set")
    scene = render(rnd.choice(c["scene"]), Env(fr=fr["N"], city=fr["city"], g=fr["g"], vars={}), rnd)
    parts, rows, tr = [], [], []
    for k, (lead, utt, qq, cat, good, dis, env) in enumerate(items):
        pre = "" if k == 0 else ("Finalmente, " if k == 7 else rnd.choice(SEQ))
        ld = render(lead, env, rnd)
        ld = pre + (ld if pre == "" or ld[:1].isupper() and ld.split()[0] == fr["N"] else ld[:1].lower() + ld[1:]) if pre else ld
        opts, ans = shuffle_opts([good] + dis, rnd)
        lab = labels(8)[k]
        parts.append({"label": lab, "text": render(qq, env, rnd), "marks": 1, "space": "mcq",
                      "choices": [f"[picture: {o[1]}]" for o in opts]})
        rows.append(row(lab, LET[ans], 1, f"[picture: {good[1]}] — key word: *{good[0]}*"))
        tr.append(f"Narrador: Pregunta {k + 1}. {ld}")
        tr.append(f"{fr['N']}: {cap(render(utt, env, rnd))}")
    intro = ("Escucha ocho grabaciones cortas; cada una se oye dos veces. "
             "Para cada pregunta, marca con una X la casilla correcta (A–D).\n\n" + scene)
    return dict(intro=intro, parts=parts, rows=rows, figures=[audio(tr)], difficulty="1-3",
                command_word="Elige", minutes=6, ao=["AO1 Listening"], general="One mark for each correct letter.")


def audio(tr, voices=None):
    f = {"type": "audio", "lang": "es-ES", "transcript": "\n".join(tr)}
    sp = []
    for l in tr:
        w = l.split(":", 1)[0]
        if w not in sp:
            sp.append(w)
    f["voices"] = voices or sp
    return f


def b_l_announce(c, rnd):
    a = c["ann"]
    # a line starting with ^ refers back to the line before it and is only used together with it
    fl = [{"i": i, "dep": l.startswith("^"), "l": l.lstrip("^").strip()} for i, l in enumerate(lines(a["facts"]))]
    chosen = [f["l"] for f in pick_facts(fl, 6, rnd)]
    env = Env(vars={}, g=rnd.choice("mf"))
    # announcements never name a real place, so nothing in them can be a false fact about it
    env.update(city="nuestra ciudad", country="nuestro país")
    sp = a["sp"]
    tr = [f"{sp}: {render(a['open'], env, rnd)}"]
    parts, rows = [], []
    for k, l in enumerate(chosen):
        s, q, o = [x.strip() for x in l.split("#")]
        choose_vars([s, q, o], env, rnd)
        tr.append(f"{sp}: {render(s, env, rnd)}")
        if o.startswith("*"):
            ch, alts = env["vars"][o[1:]]
            oth = [x for x in alts if x != ch]
            rnd.shuffle(oth)
            opts = [ch] + oth[:3]
        else:
            raw = [x.strip() for x in o.split(";") if x.strip()]
            vr = VAR_REF.findall(raw[0])
            if len(raw) == 1 and vr and vr[0] in env["vars"]:
                ch, alts = env["vars"][vr[0]]
                oth = [x for x in alts if x != ch]
                rnd.shuffle(oth)
                opts = [raw[0]] + [raw[0].replace("{" + vr[0] + "}", x) for x in oth[:3]]
            else:
                oth = raw[1:]
                rnd.shuffle(oth)
                opts = [raw[0]] + oth[:3]
        opts = [render(x, env, rnd) for x in opts]
        sh, ans = shuffle_opts(opts, rnd)
        lab = labels(6)[k]
        parts.append({"label": lab, "text": render(q, env, rnd), "marks": 1, "space": "mcq", "choices": sh})
        rows.append(row(lab, LET[ans], 1))
        # the vars of one fact must not leak into the next
        for key in list(env["vars"]):
            if key not in ("keep",):
                del env["vars"][key]
    tr.append(f"{sp}: {render(a['close'], env, rnd)}")
    title = render(a["title"], env, rnd)
    intro = (f"Vas a oír {render(a['desc'], env, rnd)}. El anuncio se oye dos veces, con una pausa en el medio. "
             "En cada pregunta, elige la respuesta correcta (A–D). "
             "Antes de escuchar, lee las preguntas.\n\n**" + title + "**")
    return dict(intro=intro, parts=parts, rows=rows, figures=[audio(tr)], difficulty=rnd.choice(["1-3", "1-3", "4-6"]),
                command_word="Elige", minutes=5, ao=["AO1 Listening"])


def b_l_match(c, rnd):
    F = facts_of(c)
    used, spk, taken = [], [], set()
    for k in range(6):
        p = narrator(c, rnd, used=used)
        used.append(p["N"])
        f = rnd.choice([f for f in usable(F, p, alone=True) if f["i"] not in taken])
        taken.add(f["i"])
        spk.append((p, inst(f, p, rnd)))
    extra = spk.pop()[1]
    stm = [x["t"] for _, x in spk] + [extra["t"]]
    order = list(range(6))
    rnd.shuffle(order)
    letter_of = {i: LET[order.index(i)] for i in range(6)}
    table = [[LET[j], cap(stm[order[j]])] for j in range(6)]
    parts, rows, tr = [], [], []
    for k, (p, x) in enumerate(spk):
        lab = labels(5)[k]
        parts.append({"label": lab, "text": f"**{p['N']}**", "marks": 1, "space": "box", "lines": 1})
        rows.append(row(lab, letter_of[k], 1, f"{p['N']} says: *{x['s']}*"))
        tr.append(f"{p['N']}: {x['s']}")
    intro = (f"Cinco jóvenes hablan {de(c['theme'])}. Cada grabación se oye dos veces.\n\n"
             "Para cada persona, escribe en la casilla la letra de la afirmación correcta (A–F). "
             "Sobra una afirmación. Antes de escuchar, lee las afirmaciones.")
    fig = {"type": "table", "headers": ["", "Afirmaciones"], "rows": table}
    lv = mean([x["lvl"] for _, x in spk])
    return dict(intro=intro, parts=parts, rows=rows, figures=[fig, audio(tr)], difficulty=band_from(lv, "4-6"),
                command_word="Empareja", minutes=5, ao=["AO1 Listening"],
                general=f"Statement {LET[order.index(5)]} is not needed.")


def interview_lines(p, facts, rnd, first=True):
    iv = p.setdefault("iv", rnd.choice(["Entrevistador", "Entrevistadora"]))
    tr = []
    if first:
        tr.append(f"{iv}: " + rnd.choice([
            f"Hoy hablamos con {p['N']}, de {p['city']}. Bienvenid<o|a>, {p['N']}.",
            f"Buenos días. Hoy está con nosotros {p['N']}, que vive en {p['city']}. Hola, {p['N']}.",
            f"Nuestr<o|a> invitad<o|a> de hoy es {p['N']}. Gracias por venir, {p['N']}."]))
        tr[-1] = f"{iv}: " + GEN.sub(lambda m: m.group(1 if p["g"] == "m" else 2), tr[-1].split(": ", 1)[1])
        tr.append(f"{p['N']}: " + rnd.choice(["¡Hola! Gracias a vosotros.", "Hola, encantad" + ("o" if p["g"] == "m" else "a") + " de estar aquí.",
                                              "Hola a todos. Es un placer."]))
    else:
        tr.append(f"{iv}: " + rnd.choice(["Seguimos con la entrevista.", "Continuamos hablando con " + p["N"] + ".",
                                          "Bueno, seguimos."]))
    for x in facts:
        tr.append(f"{iv}: {x['iq']}")
        tr.append(f"{p['N']}: {x['s']}")
    return tr


def b_l_interview(c, rnd, nopt):
    F = facts_of(c)
    n = 9 if nopt == 3 else 6
    p = narrator(c, rnd)
    chosen = pick_facts(usable(F, p), n, rnd)
    xs = [inst(f, p, rnd, nopt) for f in chosen]
    parts, rows = [], []
    for k, x in enumerate(xs):
        lab = labels(n)[k]
        sh, ans = shuffle_opts(x["opts"][:nopt], rnd)
        txt = x["q"]
        if nopt == 3 and k == 0:
            txt = "**Primera parte**\n\n" + txt
        if nopt == 3 and k == 5:
            txt = "**Segunda parte**\n\n" + txt
        parts.append({"label": lab, "text": txt, "marks": 1, "space": "mcq", "choices": sh})
        rows.append(row(lab, LET[ans], 1))
    if nopt == 3:
        figs = [audio(interview_lines(p, xs[:5], rnd)), audio(interview_lines(p, xs[5:], rnd, first=False))]
        intro = (f"Escucha esta entrevista. {p['N']} contesta a preguntas sobre {c['theme']}. La entrevista tiene dos partes "
                 "y cada parte se oye dos veces. Para cada pregunta, marca con una X la casilla correcta (A–C). "
                 "Antes de escuchar, lee las preguntas de la primera parte.")
        base, mins = "4-6", 9
    else:
        figs = [audio(interview_lines(p, xs, rnd))]
        intro = (f"Escucha esta entrevista. {p['N']} contesta a preguntas sobre {c['theme']}. La entrevista se oye dos veces, "
                 "con una pausa en el medio. Para cada pregunta, marca con una X la casilla correcta (A–D). "
                 "Antes de escuchar, lee las preguntas.")
        base, mins = "7-9", 7
    lv = mean([x["lvl"] for x in xs])
    return dict(intro=intro, parts=parts, rows=rows, figures=figs, difficulty=band_from(lv, base),
                command_word="Elige", minutes=mins, ao=["AO1 Listening"])


def b_l_multi(c, rnd):
    F = facts_of(c)
    p = narrator(c, rnd)
    F = usable(F, p)
    chosen = pick_facts(F, 9, rnd)
    rest = [f for f in F if f not in chosen]
    xs = [inst(f, p, rnd) for f in chosen]
    rx = [inst(f, p, rnd) for f in rest]
    parts, rows = [], []
    tr = []
    for k in range(3):
        sec = xs[3 * k:3 * k + 3]
        tr += interview_lines(p, sec, rnd, first=(k == 0))
        trues = rnd.sample(range(3), 2)
        fal_own = [i for i in range(3) if i not in trues][0]
        stm = [(sec[i]["t"], True) for i in trues] + [(sec[fal_own]["f"], False)]
        pool = [r["f"] for r in rx]
        rnd.shuffle(pool)
        extra = pool[:2] if len(pool) >= 2 else [sec[trues[0]]["f"], sec[trues[1]]["f"]]
        if len(pool) >= 2 and rnd.random() < 0.4:
            extra = [pool[0], sec[trues[0]]["f"]]
        stm += [(e, False) for e in extra]
        rnd.shuffle(stm)
        lab = labels(3)[k]
        good = [LET[i] for i, (_, ok) in enumerate(stm) if ok]
        parts.append({"label": lab, "text": f"Sección {k + 1}: marca con una X **dos** afirmaciones correctas.",
                      "marks": 2, "space": "mcq", "choices": [cap(s) for s, _ in stm]})
        rows.append(row(lab, " / ".join(good), 2, "One mark for each correct letter. If more than two letters are marked, deduct one mark for each extra letter."))
    intro = (f"Escucha esta entrevista. {p['N']} contesta a preguntas sobre {c['theme']}. La entrevista se oye dos veces, "
             "con dos pausas. Para cada sección, marca con una X las **dos** casillas correctas (A–E). "
             "Antes de escuchar, lee las afirmaciones.")
    return dict(intro=intro, parts=parts, rows=rows, figures=[audio(tr)], difficulty=band_from(mean([x["lvl"] for x in xs]), "7-9"),
                command_word="Elige", minutes=8, ao=["AO1 Listening"])


# ------------------------------------------------------------------ Reading

def b_r_pictures(c, rnd):
    exs = lines(c["ex"])
    fr = person(rnd, need=(lambda t: "spain" in t) if needs_spain(c) else None)
    base = Env(fr=fr["N"], g=fr["g"], city=fr["city"], vars={})
    for _ in range(200):
        chosen = rnd.sample(exs, 5)
        seen, items = set(), []
        for e in chosen:
            lead, utt, qq, cat = [x.strip() for x in e.split("#")]
            vals = [v for v in LX.CATS[cat] if pic(v[1]) not in seen]
            v = rnd.choice(vals)
            seen.add(pic(v[1]))
            items.append((cap(render(with_article(utt, v[0]), val_env(base, v), rnd)), v, cat))
        cat_x = rnd.choice([i[2] for i in items])
        extra = rnd.choice([v for v in LX.CATS[cat_x] if pic(v[1]) not in seen])
        opts = [(i[1][0], i[2]) for i in items] + [(extra[0], cat_x)]
        if not ambiguous([i[0] for i in items], opts, list(range(5))):
            break
    else:
        raise ValueError("r-pictures: no unambiguous set")
    pics = [i[1] for i in items] + [extra]
    order = list(range(6))
    rnd.shuffle(order)
    table = [[LET[j], f"[picture: {pics[order[j]][1]}]"] for j in range(6)]
    parts, rows = [], []
    for k, (sent, v, _) in enumerate(items):
        lab = labels(5)[k]
        parts.append({"label": lab, "text": sent, "marks": 1, "space": "box", "lines": 1})
        rows.append(row(lab, LET[order.index(k)], 1, f"*{v[0]}* = {v[1]}"))
    intro = "Mira los dibujos. Para cada frase, escribe en la casilla la letra correcta (A–F). Hay un dibujo que no necesitas."
    return dict(intro=intro, parts=parts, rows=rows, figures=[{"type": "table", "headers": ["", "Dibujos"], "rows": table}],
                difficulty="1-3", command_word="Mira", minutes=3, ao=["AO2 Reading"])


def b_r_signs(c, rnd):
    setting, block = c["signs"]
    # "sign#sentence#group": signs sharing a group could each fit the other's sentence,
    # so at most one sign per group is ever shown.
    sl = [tuple(x.strip() for x in l.split("#")) for l in lines(block)]
    for _ in range(200):
        shown = rnd.sample(sl, 8)
        groups = [x[2] for x in shown if len(x) > 2 and x[2]]
        if len(groups) == len(set(groups)):
            break
    else:
        raise ValueError("r-signs: cannot pick signs from distinct groups")
    asked = rnd.sample(range(8), 5)
    table = [[LET[j], f"**{shown[j][0]}**"] for j in range(8)]
    parts, rows = [], []
    for k, j in enumerate(asked):
        lab = labels(5)[k]
        parts.append({"label": lab, "text": shown[j][1], "marks": 1, "space": "box", "lines": 1})
        rows.append(row(lab, LET[j], 1))
    intro = f"Lee los letreros. Para cada frase, escribe en la casilla la letra correcta (A–H).\n\n**{setting}**"
    return dict(intro=intro, parts=parts, rows=rows, figures=[{"type": "table", "headers": ["", "Letreros"], "rows": table}],
                difficulty=rnd.choice(["1-3", "1-3", "4-6"]), command_word="Lee", minutes=4, ao=["AO2 Reading"])


def b_r_text_mcq(c, rnd):
    F = facts_of(c)
    p = narrator(c, rnd)
    rcp = person(rnd, used=[p["N"]])
    chosen = pick_facts(usable(F, p), 7, rnd)
    xs = [inst(f, p, rnd, 3) for f in chosen]
    body = paragraphs([x["s"] for x in xs], rnd, (2, 3))
    greet = rnd.choice([f"Hola, {rcp['N']}:", f"¡Hola, {rcp['N']}!", f"Querid{'o' if rcp['g'] == 'm' else 'a'} {rcp['N']}:"])
    close = rnd.choice(["Un abrazo,", "Besos,", "Escríbeme pronto,", "Hasta pronto,"])
    opener = rnd.choice(["¿Qué tal estás? Te escribo para contarte cosas de mi vida.", "¿Cómo estás? Aquí todo bien.",
                         "Perdona por no escribir antes. Tengo muchas cosas que contarte."])
    text = f"{greet}\n\n{opener} " + "\n\n".join(body) + f"\n\n{close}\n{p['N']}"
    parts, rows = [], []
    for k, x in enumerate(xs):
        lab = labels(7)[k]
        sh, ans = shuffle_opts(x["opts"][:3], rnd)
        parts.append({"label": lab, "text": x["q"], "marks": 1, "space": "mcq", "choices": sh})
        rows.append(row(lab, LET[ans], 1))
    intro = "Lee el texto. Para cada pregunta, marca con una X la casilla correcta (A–C)."
    return dict(intro=intro, parts=parts, rows=rows, figures=[{"type": "source", "label": "", "text": text}],
                difficulty=band_from(mean([x["lvl"] for x in xs]), "1-3"), command_word="Lee", minutes=7, ao=["AO2 Reading"])


def _plain(t):
    return re.sub(r"[()]", "", t).lower().strip(" .")


def clean_note(rej, ans):
    """Drop draft/self-contradictory refuse notes: notes containing '?', and 'Refuse X' where X is
    itself an accepted answer (e.g. conditional/imperfect forms that are the same in 1st and 3rd person)."""
    if not rej or "?" in rej:
        return None
    m = re.match(r"Refuse (.+?)(?: tc.*| on its own.*)?$", rej)
    if m:
        bad = _plain(m.group(1))
        alts = re.split(r"\s*/\s*", ans)
        forms = {_plain(a) for a in alts} | {re.sub(r"\s+", " ", _plain(re.sub(r"\([^)]*\)", "", a))) for a in alts}
        if bad in forms:
            return None
    return rej


SPECIFIC = re.compile(r"^(.*?),? (?:sobre todo|especialmente|en especial|en particular) ", re.I)


def general_specific(x):
    """Text gives 'general category, sobre todo specific' and the question does not ask for the specific
    ('sobre todo'): either level answers it, so a refuse note on the general category is wrong."""
    m = SPECIFIC.match(x["s"])
    if not m or re.search(r"sobre todo|especial|en particular", x["q"], re.I) or not x["rej"]:
        return x["a"], clean_note(x["rej"], x["a"])
    r = re.match(r"Refuse (.+?)(?: tc.*| on its own.*)?$", x["rej"])
    if r and _plain(m.group(1)).endswith(_plain(r.group(1))):
        g = r.group(1)
        return f"{x['a']} / {g}", f"Accept the general category ({g}) or the specific item"
    return x["a"], clean_note(x["rej"], x["a"])


def answer_row(lab, x):
    a, note = general_specific(x)
    return row(lab, a, 1, note)


def b_r_short(c, rnd):
    F = facts_of(c)
    p = narrator(c, rnd)
    chosen = pick_facts(usable(F, p), 11, rnd)
    xs = [inst(f, p, rnd) for f in chosen]
    hello = rnd.choice([f"¡Hola! Me llamo {p['N']} y vivo en {p['city']}, en {p['country']}.",
                        f"Hola a todos. Soy {p['N']}, tengo {rnd.choice(['quince', 'dieciséis', 'diecisiete'])} años y vivo en {p['city']} ({p['country']})."])
    body = paragraphs([x["s"] for x in xs], rnd, (3, 4))
    text = hello + " " + "\n\n".join(body)
    parts = [{"label": "a", "text": f"¿En qué país vive {p['N']}?", "marks": 1, "lines": 1}]
    rows = [row("a", f"(En) {p['country']}", 1, f"Refuse {p['city']} (a city, not the country)" if p['city'] != p['country'] else None)]
    for k, x in enumerate(xs):
        lab = labels(12)[k + 1]
        parts.append({"label": lab, "text": x["q"], "marks": 1, "lines": 1})
        rows.append(answer_row(lab, x))
    intro = "Lee el texto. Contesta a las preguntas **en español**."
    return dict(intro=intro, parts=parts, rows=rows, figures=[{"type": "source", "label": f"El blog de {p['N']}", "text": text}],
                difficulty=band_from(mean([x["lvl"] for x in xs]), "4-6"), command_word="Contesta", minutes=13,
                ao=["AO2 Reading"], general=GEN_READ)


GEN_READ = ("Mark for communication: tolerate minor spelling errors if the meaning is clear and no other Spanish word is created. "
            "Answers must refer to the person in the text (third person); a lift in the first person is not accepted where it changes the meaning. "
            "( ) = not required; / = alternatives; tc = not enough on its own; INV = extra material invalidates the answer.")

SAY = ["cuenta", "explica", "nos dice", "añade", "comenta", "asegura"]


def b_r_long(c, rnd):
    F = facts_of(c)
    p = narrator(c, rnd)
    F = usable(F, p)
    hard = [f for f in F if f["lvl"] >= 2]
    pool = F if len(hard) < 10 else hard
    try:
        chosen = pick_facts(pool, 10, rnd)
    except ValueError:
        chosen = pick_facts(F, 10, rnd)
    xs = [inst(f, p, rnd) for f in chosen]
    joven = "un joven" if p["g"] == "m" else "una joven"
    intro_t = rnd.choice([
        f"{p['N']} {p['sur']} es {joven} {p['nat']} que vive en {p['city']}. Hemos hablado con {'él' if p['g'] == 'm' else 'ella'} sobre {c['theme']}.",
        f"Nació en {p['city']}, {p['country']}, y hoy nos habla {de(c['theme'])}. Se llama {p['N']} {p['sur']}.",
        f"Esta semana entrevistamos a {p['N']} {p['sur']}, {joven} de {p['city']}, para conocer su opinión sobre {c['theme']}."])
    groups = paragraphs([x["s"] for x in xs], rnd, (2, 3))
    paras = []
    for g in groups:
        v = rnd.choice(SAY)
        g = g[:-1] if g.endswith(".") else g
        paras.append(f"‘{g}’, {v} {p['N']}.")
    text = intro_t + "\n\n" + "\n\n".join(paras)
    parts = [{"label": "a", "text": f"¿De qué país es {p['N']}?", "marks": 1, "lines": 1}]
    rows = [row("a", f"(De) {p['country']} / (Es) {p['nat']}", 1, f"Refuse {p['city']} tc")]
    for k, x in enumerate(xs):
        lab = labels(11)[k + 1]
        parts.append({"label": lab, "text": x["q"], "marks": 1, "lines": 1})
        rows.append(answer_row(lab, x))
    title = rnd.choice([f"{cap(c['tema'])}: la experiencia de {p['N']}", f"{p['N']} {p['sur']}: {c['tema'].lower()}",
                        f"Hablamos con {p['N']} {p['sur']}"])
    return dict(intro="Lee el texto. Contesta a las preguntas **en español**.", parts=parts, rows=rows,
                figures=[{"type": "source", "label": title, "text": text}],
                difficulty=band_from(mean([x["lvl"] for x in xs]), "7-9"), command_word="Contesta", minutes=15,
                ao=["AO2 Reading"], general=GEN_READ)


def b_r_ads(c, rnd):
    title, block = c["ads"]
    al = [tuple(x.strip() for x in l.split("#")) for l in lines(block)]
    chosen = rnd.sample(al, 5)
    rest = [a for a in al if a not in chosen]
    decoys = []
    nears = [a[2] for a in chosen]
    rnd.shuffle(nears)
    decoys += nears[:2]
    decoys += [a[1] for a in rest][:1] if rest else nears[2:3]
    adverts = [a[1] for a in chosen] + decoys[:3]
    order = list(range(8))
    rnd.shuffle(order)
    table = [[str(j + 1), adverts[order[j]]] for j in range(8)]
    used, parts, rows = [], [], []
    for k, a in enumerate(chosen):
        pp = person(rnd, used=used)
        used.append(pp["N"])
        lab = labels(5)[k]
        parts.append({"label": lab, "text": f"**{pp['N'].upper()}:** {render(a[0], pp, rnd)}", "marks": 1, "space": "box", "lines": 1})
        rows.append(row(lab, str(order.index(k) + 1), 1))
    intro = (f"Lee los textos (a–e) y los anuncios (1–8). ¿Cuál es el mejor anuncio para cada persona? "
             f"Para cada texto, escribe el número correcto (1–8) en la casilla.\n\n**{title}**")
    return dict(intro=intro, parts=parts, rows=rows, figures=[{"type": "table", "headers": ["", "Anuncios"], "rows": table}],
                difficulty=rnd.choice(["4-6", "4-6", "7-9"]), command_word="Lee", minutes=8, ao=["AO2 Reading"])


# ------------------------------------------------------------------ Speaking

RP_GRID = ("Role play: up to 2 marks per task. 2 = the information is communicated; language appropriate and accurate "
           "(minor slips such as an adjective ending or preposition allowed). 1 = partly communicated, or meaning ambiguous; "
           "errors get in the way. 0 = nothing creditable. A short answer that communicates fully earns 2. "
           "The teacher may repeat a task once but must not rephrase it.")


TU = re.compile(r"\b(te|tu|tus|tú|ti|contigo|quieres|tienes|prefieres|puedes|vas|estás|eres|necesitas|buscas|usas|"
                r"sois|hiciste|fuiste|compraste|comiste|viniste|llegaste|visitaste|estudiaste|has|"
                r"\w+aste|\w+iste)\b", re.I)


def b_s_roleplay(c, rnd):
    sc = rnd.choice(c["rp"])
    p = person(rnd)
    env = Env(city=p["city"], country=p["country"], vars={}, g=p["g"])
    ctx = render(sc["ctx"], env, rnd)
    parts, rows = [], []
    for k, slot in enumerate(sc["slots"]):
        q, exp = [x.strip() for x in rnd.choice(lines(slot)).split("#")]
        q = both(render(q, env, rnd))
        if sc["formal"] and TU.search(q.replace("[PAUSA]", "")):
            raise ValueError(f"role play with a formal examiner uses tú: {q}")
        lab = str(k + 1)
        parts.append({"label": lab, "text": q.replace(" [PAUSA] ", " ‖ "), "marks": 2, "space": "none"})
        rows.append(row(lab, render(exp, env, rnd), 2,
                        "1 mark if the information is only partly communicated or is ambiguous (e.g. wrong time frame, verb form that changes the meaning)."))
    card = (f"**Juego de rol**\n\n{ctx}\n\nTu papel: eres tú.\nEl papel del examinador: {sc['role']}"
            + (" (habla de usted)" if sc["formal"] else "") + ".\n\n"
            "Escucha al examinador, que habla primero, y contesta cada pregunta.\n\n"
            "*Teacher/examiner script: read the context aloud, then ask each question below exactly as printed. "
            "At ‖ wait for the answer to the first half of a two-part question.*")
    return dict(intro=card, parts=parts, rows=rows, difficulty=rnd.choice(["4-6", "4-6", "1-3"]),
                command_word="Responde", minutes=2.5, ao=["AO3 Speaking"], general=RP_GRID)


COMM = [("13–15", "13-15", "Very good: answers confidently, needing repetition only rarely; information always relevant; often develops ideas and opinions; justifies and explains several answers."),
        ("10–12", "10-12", "Good: answers well, occasionally needing an alternative question; information almost always relevant; sometimes develops ideas; gives reasons for some answers."),
        ("7–9", "7-9", "Satisfactory: copes with most questions but often needs the alternative questions; gives most of the information asked for, with some irrelevance; simple opinions."),
        ("4–6", "4-6", "Weak: struggles with many questions but tries to answer; some simple relevant information."),
        ("1–3", "1-3", "Poor: often fails to understand and replies with great difficulty; one or two basic relevant details."),
        ("0", "0", "Nothing creditable.")]
QUAL = [("13–15", "13-15", "Very good: wide range of syllabus structures and vocabulary used accurately, slips mainly in complex language; very good pronunciation, fluency and intonation."),
        ("10–12", "10-12", "Good: a range of structures and vocabulary with some errors; good pronunciation and fluency despite some hesitation."),
        ("7–9", "7-9", "Satisfactory: some syllabus structures and adequate vocabulary with frequent errors; pronunciation and fluency acceptable despite errors and hesitation."),
        ("4–6", "4-6", "Weak: narrow range of structures and vocabulary, seldom accurate; often ambiguous; understood only with effort; stilted delivery."),
        ("1–3", "1-3", "Poor: very narrow range, nearly always inaccurate; pronunciation rarely comprehensible."),
        ("0", "0", "Nothing creditable.")]


def tq_of(c):
    out = []
    for l in lines(c.get("tq", "")):
        tag, q, alt, ind = [x.strip() for x in l.split("#")]
        out.append({"tag": tag, "q": both(q), "alt": both(alt), "ind": both(ind)})
    return out


TENSE = {"p": "present", "o": "opinion + reason", "pa": "past", "f": "future", "c": "conditional", "d": "description/explanation"}


def conv_set(c, rnd):
    T = tq_of(c)
    by = lambda *tags: [t for t in T if t["tag"] in tags]
    q12 = rnd.sample(by("p"), 2)
    q3 = rnd.choice(by("o"))
    q4 = rnd.choice(by("pa"))
    q5 = rnd.choice(by("f", "c"))
    return [q12[0], q12[1], q3, q4, q5]


def conv_text(n, c, qs):
    out = [f"**Conversación {n} – Tema: {c['tema']}**"]
    for k, t in enumerate(qs):
        out.append(f"{k + 1}  {t['q']}")
        if k >= 2 and t["alt"]:
            out.append(f"     *Si no contesta, pregunta:* {t['alt']}")
    return "\n".join(out)


def b_s_conversation(c, rnd, ref):
    group1 = ref[0] in "AB"
    others = [r for r, cc in CONTENT.items() if cc.get("tq") and ((r[0] in "CDE") if group1 else (r[0] in "AB"))]
    pr = rnd.choice(others)
    pc = CONTENT[pr]
    a, b = (c, pc) if group1 else (pc, c)
    qa, qb = conv_set(a, rnd), conv_set(b, rnd)
    text = conv_text(1, a, qa) + "\n\n" + conv_text(2, b, qb)
    intro = ("Two topic conversations of 4 minutes each. Say: *Primero vamos a hablar de …* / *Ahora vamos a hablar de …*. "
             "Ask all five questions in order. If there is no relevant answer, repeat the question; for questions 3–5 then use "
             "the alternative question. Extension prompts such as *¿Puedes decirme algo más (sobre eso)?* may be used. "
             "If a conversation lasts 3½ minutes or less, ask up to two further questions on the same topic.")
    ind = []
    for n, (cc, qs) in enumerate(((a, qa), (b, qb)), 1):
        for k, t in enumerate(qs):
            ind.append(f"C{n} Q{k + 1} ({TENSE[t['tag']]}): {t['ind']}")
    lv = [levels("", COMM, ind, title="Communication (both conversations, out of 15)", ao_split="AO3 15"),
          levels("", QUAL, ["Look for accurate verbs in past, present and future/conditional time frames.",
                            "Credit linked, extended sentences (porque, aunque, sin embargo, cuando, si …) and opinion phrases.",
                            "Credit topic vocabulary used accurately and pronunciation that is easily understood."],
                 title="Quality of Language (both conversations, out of 15)", ao_split="AO3 15")]
    parts = [{"label": "", "text": text, "marks": 30, "space": "none"}]
    return dict(intro=intro, parts=parts, rows=[], levels=lv, difficulty=rnd.choice(["4-6", "7-9", "7-9"]),
                command_word="Habla", minutes=8, ao=["AO3 Speaking"], extra_refs=[pr],
                general="Award one mark out of 15 for Communication and one out of 15 for Quality of Language across BOTH conversations together. "
                        "Start at the bottom band and work up; top of band if the descriptor is convincingly met, bottom if just met.")


# ------------------------------------------------------------------ Writing

def gap_note(n):
    """Form gap note: plain refuse list gets a 'Refuse:' label; notes that grant acceptance stay as written."""
    return n if ("accept" in n.lower() or n.lower().startswith("refuse")) else "Refuse: " + n


def b_w_form(c, rnd):
    fm = rnd.choice(c["form"])   # one scenario: title, context and its own fields
    p = person(rnd)
    gaps = [tuple(x.strip() for x in l.split("#")) for l in lines(fm["gaps"])]
    doubles = [g for g in gaps if g[3] == "2"]
    singles = [g for g in gaps if g[3] == "1"]
    if doubles and (rnd.random() < 0.7 or len(singles) < 5):
        chosen = [rnd.choice(doubles)] + rnd.sample(singles, 3)
    else:
        chosen = rnd.sample(singles, 5)
    order = [g for g in gaps if g in chosen]
    title = render(fm["title"], p, rnd)
    ctx = render(fm["ctx"], p, rnd)
    rows_t = [["Nombre:", f"{p['N']} {p['sur']}"]]
    extra_given = [("Edad:", f"{rnd.randint(15, 17)} años"), ("Nacionalidad:", p["nat"]), ("Ciudad:", p["city"])]
    rows_t.append(list(rnd.choice(extra_given)))
    rows, gapn = [], 1
    for g in order:
        lab = g[0]
        if g[3] == "2":
            rows_t.append([lab + " *(Menciona dos cosas.)*", "…………………… y ……………………"])
            rows.append(row("", f"Gaps {gapn} & {gapn + 1}: {g[1]}", 2, (gap_note(g[2]) + " Two different items needed; 1 mark each.") if g[2] else "Two different items needed; 1 mark each."))
            gapn += 2
        else:
            rows_t.append([lab, "……………………………………"])
            rows.append(row("", f"Gap {gapn}: {g[1]}", 1, gap_note(g[2]) if g[2] else None))
            gapn += 1
    rows_t.append(["E-mail:", f"{p['N'].lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')}{rnd.randint(10, 99)}@correo.es"])
    intro = f"Te llamas {p['N']} {p['sur']}. {ctx}\n\nRellena el formulario **en español**."
    parts = [{"label": "", "text": f"**{title}**", "marks": 5, "space": "table",
              "figures": [{"type": "table", "headers": ["", ""], "rows": rows_t}]}]
    return dict(intro=intro, parts=parts, rows=rows, difficulty="1-3", command_word="Completa", minutes=5,
                ao=["AO4 Writing"],
                general="One mark per correct item. Mark for communication: a single word is enough; tolerate spelling errors if a Spanish speaker would understand. Accept singular for plural and vice versa. Answers must fit the purpose of the form.")


SHORT_GRID = [("10–12", "10-12", "All tasks completed in the detail required; information and opinions consistently relevant; meaning clear despite some slips; straightforward vocabulary and structures; words and phrases linked with a range of simple connectors."),
              ("7–9", "7-9", "Most tasks completed in the detail required; mostly relevant; meaning mostly clear despite errors; limited vocabulary and structures with some repetition; some attempt at a range of simple connectors."),
              ("4–6", "4-6", "Some tasks completed with some detail; some relevant information; meaning sometimes clear; basic vocabulary and structures, often repeated; linking limited to a few simple connectors (y, o)."),
              ("1–3", "1-3", "Task(s) attempted with little or no detail; information mostly irrelevant; meaning rarely clear; isolated words and phrases; little linking."),
              ("0", "0", "Nothing creditable.")]
TC_GRID = [("9–10", "9-10", "All tasks completed; detailed information, opinions/reactions and explanations; focused and wholly relevant."),
           ("7–8", "7-8", "Most tasks completed; straightforward information, opinions and explanations; mostly relevant."),
           ("5–6", "5-6", "Some tasks completed; some information, opinions and simple explanations; more relevant than irrelevant."),
           ("3–4", "3-4", "Some tasks attempted with some success; basic information and opinions; only occasionally relevant."),
           ("1–2", "1-2", "Task(s) attempted with little or no success; information almost always irrelevant."),
           ("0", "0", "Nothing creditable.")]
RANGE_GRID = [("9–10", "9-10", "Frequent extended, well-linked sentences; wide range of simple and complex syllabus structures giving sentences of varied length; wide task-appropriate vocabulary."),
              ("7–8", "7-8", "Some extended sentences, mostly well linked; a range of structures including some complex ones; a range of vocabulary with occasional repetition."),
              ("5–6", "5-6", "Some extended sentences with some linking; simple structures with attempts at complex ones; mostly straightforward vocabulary with some repetition."),
              ("3–4", "3-4", "Simple structures only, no attempt at complex ones; a small range of straightforward vocabulary, repeated."),
              ("1–2", "1-2", "Isolated phrases and some attempt at basic structures; small range of basic vocabulary, repeated."),
              ("0", "0", "Nothing creditable.")]
ACC_GRID = [("7–8", "7-8", "Accurate spelling and grammar, though not necessarily faultless; occasional errors do not impede communication."),
            ("5–6", "5-6", "Mostly accurate spelling and grammar; errors sometimes impede communication."),
            ("3–4", "3-4", "Some accurate spelling and grammar; errors frequently impede communication."),
            ("1–2", "1-2", "Spelling and grammar rarely accurate; errors persistently impede communication."),
            ("0", "0", "Nothing creditable.")]


def bullet_ind(n, t):
    return f"Task {n} ({TENSE[t['tag']]}): {t['ind']}"


def b_w_short(c, rnd):
    T = tq_of(c)
    by = lambda *tags: [t for t in T if t["tag"] in tags]
    ps = rnd.sample(by("p"), 2)
    o = rnd.choice(by("o"))
    fut = rnd.choice(by("f", "c", "pa"))
    bl = [ps[0], o, ps[1], fut]
    text = f"**{c['tema']}**\n\n" + "\n".join(f"•  {t['q']}" for t in bl) + "\n\nTu texto debe tener entre 80 y 90 palabras, **en español**."
    ind = [bullet_ind(k + 1, t) for k, t in enumerate(bl)]
    ind.append("Two-part bullet (opinion + ¿Por qué?): both parts must be answered for full task completion; the future/conditional bullet needs a future or conditional verb.")
    parts = [{"label": "", "text": text, "marks": 12, "lines": 15}]
    return dict(intro="", parts=parts, rows=[], levels=[levels("", SHORT_GRID, ind, title="Question 2 (out of 12)", ao_split="AO4 12")],
                difficulty="4-6", command_word="Escribe", minutes=15, ao=["AO4 Writing"],
                general="Read the whole answer and award one mark from the grid. Full marks need at least one relevant detail for every task, in prose, with correct subject–verb agreement.")


FRAMES = [
    ("e-mail", "Tu amigo/amiga quiere saber tu opinión sobre {t}. Escribe un e-mail a tu amigo/amiga."),
    ("blog", "Quieres hablar de {t} en tu blog. Escribe un artículo para tu blog."),
    ("revista", "La revista de tu instituto prepara un número especial sobre {t}. Escribe un artículo para la revista."),
    ("carta", "Un(a) estudiante de intercambio quiere saber cómo viven los jóvenes de tu país. Escríbele un e-mail sobre {t}."),
]


def b_w_extended(c, rnd):
    T = tq_of(c)
    by = lambda *tags: [t for t in T if t["tag"] in tags]
    first = rnd.choice(by("p", "d"))
    past = rnd.choice(by("pa"))
    op = rnd.choice(by("o", "d"))
    while op is first:
        op = rnd.choice(by("o", "d"))
    fut = rnd.choice(by("f"))
    cond = rnd.choice([t for t in by("c", "f") if t is not fut] or [fut])
    bl = [first, past, op, fut, cond] if rnd.random() < 0.5 else [first, op, past, cond, fut]
    kind, frame = rnd.choice(FRAMES)
    frame = frame.format(t=f"el tema «{c['tema']}»")
    text = (f"**{c['tema']}**\n\n{frame}\n\n" + "\n".join(f"•  {t['q']}" for t in bl) +
            "\n\nTu texto debe tener entre 130 y 140 palabras, **en español**.")
    ind = [bullet_ind(k + 1, t) for k, t in enumerate(bl)]
    lv = [levels("", TC_GRID, ind, title="Task completion (out of 10)", ao_split="AO4 10"),
          levels("", RANGE_GRID, ["Credit extended sentences linked with connectives (aunque, sin embargo, ya que, cuando …).",
                                  "Credit complex structures from the syllabus: preterite and imperfect, future, conditional, object pronouns, comparatives, subordinate clauses, a subjunctive after cuando / es importante que."],
                 title="Range (out of 10)", ao_split="AO4 10"),
          levels("", ACC_GRID, ["Judge verb endings, agreements and spelling (including accents that change meaning, e.g. bailé/baile)."],
                 title="Accuracy (out of 8)", ao_split="AO4 8")]
    parts = [{"label": "", "text": text, "marks": 28, "lines": 24}]
    return dict(intro="", parts=parts, rows=[], levels=lv, difficulty="7-9", command_word="Escribe", minutes=35,
                ao=["AO4 Writing"],
                general="Read the whole answer and award a mark from each of the three grids, then add them. For a task to be fully completed it must be answered in the time frame it asks for with a correct verb. Material unrelated to the bullets is disregarded; a wholly irrelevant answer scores 0.")


BUILDERS = {
    "l-short": b_l_short, "l-announce": b_l_announce, "l-match": b_l_match,
    "l-interview-3": lambda c, r: b_l_interview(c, r, 3), "l-interview-4": lambda c, r: b_l_interview(c, r, 4),
    "l-multi": b_l_multi, "r-pictures": b_r_pictures, "r-signs": b_r_signs, "r-text-mcq": b_r_text_mcq,
    "r-short": b_r_short, "r-long": b_r_long, "r-match-ads": b_r_ads, "s-roleplay": b_s_roleplay,
    "w-form": b_w_form, "w-short": b_w_short, "w-extended": b_w_extended,
}


def norm(d):
    bits = [d.get("intro", "")]
    for p in d["parts"]:
        bits.append(p["text"])
        bits += p.get("choices", [])
    for f in d.get("figures", []):
        bits.append(f.get("text", "") or f.get("transcript", ""))
        for r in f.get("rows", []) or []:
            bits += r
    return re.sub(r"\s+", " ", " ".join(bits).lower())


def main():
    SP.build()
    bank = Bank("spanish")
    for tid, ref, sid, title, qts in SP.subtopics():
        c = CONTENT[ref]
        for qt in qts:
            seen = set()
            made, tries = 0, 0
            while made < PER_CELL and tries < 200:
                tries += 1
                rnd = random.Random(f"{ref}-{qt}-{tries}")
                if qt == "s-conversation":
                    d = b_s_conversation(c, rnd, ref)
                else:
                    d = BUILDERS[qt](c, rnd)
                d = finalize(d, f"{ref} {qt}")
                key = norm(d)
                if key in seen:
                    continue
                seen.add(key)
                made += 1
                ms = {"style": "levels" if d.get("levels") else ("mcq" if qt.startswith("l-") else "points"),
                      "rows": d["rows"]}
                if d.get("levels"):
                    ms["levels"] = d["levels"]
                if d.get("general"):
                    ms["general"] = d["general"]
                refs = [ref] + [r for r in d.get("extra_refs", []) if r != ref]
                bank.add(topic=tid, subtopic=sid, qtype=qt, command_word=d["command_word"], difficulty=d["difficulty"],
                         parts=d["parts"], markscheme=ms, spec_refs=refs, paper=[PAPER[qt[0]]], ao=d["ao"],
                         template=f"{qt}.{ref.lower()}", intro=d.get("intro") or None, figures=d.get("figures") or None,
                         minutes=d["minutes"], calculator=None,
                         provenance="Original text written for this bank.", tags=[ref, qt[0].upper()])
            assert made >= 12, (ref, qt, made)
    bank.save()


if __name__ == "__main__":
    main()
