"""Statistics and probability templates (spec section 6)."""
import math
from fractions import Fraction as F

from maths_util import (tpl, P, R, Q, sf, dp, num, ftex, name, fig, table, grid_fig, PL, L, T, DOT, tree_fig, venn_fig,
                        big)


def fr_tex(x):
    return ftex(F(x))


def interp(xs, ys, y):
    """inverse linear interpolation: x where piecewise-linear (xs, ys) reaches y."""
    for i in range(1, len(xs)):
        if ys[i] >= y:
            if ys[i] == ys[i - 1]:
                return xs[i]
            return xs[i - 1] + (xs[i] - xs[i - 1]) * (y - ys[i - 1]) / (ys[i] - ys[i - 1])
    return xs[-1]


def fwd(xs, ys, x):
    for i in range(1, len(xs)):
        if xs[i] >= x:
            return ys[i - 1] + (ys[i] - ys[i - 1]) * (x - xs[i - 1]) / (xs[i] - xs[i - 1])
    return ys[-1]


CTX = [("time, $t$ minutes", "t", "minutes", "the time, in minutes, that each of {n} people waited for a bus"),
       ("mass, $m$ grams", "m", "grams", "the masses, in grams, of {n} apples"),
       ("height, $h$ cm", "h", "cm", "the heights, in centimetres, of {n} plants"),
       ("length, $l$ cm", "l", "cm", "the lengths, in centimetres, of {n} fish"),
       ("distance, $d$ km", "d", "km", "the distances, in kilometres, that {n} people travel to work"),
       ("speed, $s$ km/h", "s", "km/h", "the speeds, in km/h, of {n} cars on a road")]


def classes(r, k=5, widths=None):
    start = r.choice([0, 0, 10, 20, 40, 100])
    w = r.choice([5, 10, 10, 20]) if widths is None else None
    bounds = [start]
    for i in range(k):
        bounds.append(bounds[-1] + (w if widths is None else r.choice(widths)))
    return bounds


def cls_label(a, b, v):
    return f"${a} < {v} \\leqslant {b}$"


# ================================================================ 6.2 averages
@tpl("stats.averages", "short", n=17)
def mean_combined(r):
    kind = r.choice(["combine", "missing", "missing"])
    if kind == "combine":
        n1, n2 = r.randint(8, 30), r.randint(8, 30)
        m1, m2 = r.choice([F(k, 10) for k in range(100, 900, 7)]), r.choice([F(k, 10) for k in range(100, 900, 7)])
        g = r.choice([("boys", "girls", "test score"), ("men", "women", "age in years"), ("Class A", "Class B", "mark")])
        mean = (n1 * m1 + n2 * m2) / (n1 + n2)
        return Q(intro=f"In a group, there are {n1} {g[0]} and {n2} {g[1]}.\n\nThe mean {g[2]} of the {g[0]} is {num(float(m1))}.\nThe mean {g[2]} of the {g[1]} is {num(float(m2))}.",
                 parts=[P("", f"Work out the mean {g[2]} of all {n1 + n2} people in the group.\n\nGive your answer to 1 decimal place.", 3, prefix="")],
                 rows=[R("", f"${n1} \\times {num(float(m1))}$ or ${n2} \\times {num(float(m2))}$", "M1", ""),
                       R("", f"$({num(float(n1 * m1))} + {num(float(n2 * m2))}) \\div {n1 + n2}$", "M1", ""),
                       R("", dp(mean, 1), "A1", f"awrt {dp(mean, 1)}")],
                 values={"mean": float(mean)}, diff="4-6", cw="Work out", refs=["F6.2B"])
    k = r.randint(5, 9)
    nums = [r.randint(2, 40) for _ in range(k - 1)]
    last = r.randint(2, 40)
    tot = sum(nums) + last
    if tot % k:
        return None
    m = tot // k
    return Q(intro=f"There are {k} numbers in a list.\n\nThe mean of the {k} numbers is {m}.\n\n{k - 1} of the numbers are {', '.join(map(str, nums))}",
             parts=[P("", "Work out the other number.", 2, prefix="")],
             rows=[R("", f"${k} \\times {m} = {tot}$", "M1", f"and subtracting the sum of the {k - 1} numbers"),
                   R("", str(last), "A1", "cao")],
             values={"number": last}, diff="4-6", cw="Work out", refs=["F6.2B"])


@tpl("stats.averages", "short", n=17)
def freq_table_mean(r):
    vals = list(range(r.choice([0, 1]), 6 + r.choice([0, 1])))
    fs = [r.randint(1, 15) for _ in vals]
    n = sum(fs)
    mean = F(sum(v * f for v, f in zip(vals, fs)), n)
    item = r.choice(["number of brothers and sisters", "number of goals scored", "number of books read",
                     "number of pets", "number of text messages sent"])
    return Q(intro=f"The table shows information about the {item} for each of {n} people.",
             figs=[table(["Number", "Frequency"], [[v, f] for v, f in zip(vals, fs)])],
             parts=[P("", "Work out the mean.", 3, prefix="")],
             rows=[R("", "$" + " + ".join(f"{v} \\times {f}" for v, f in zip(vals, fs)) + f" = {sum(v * f for v, f in zip(vals, fs))}$", "M1", "for at least 3 correct products"),
                   R("", f"${sum(v * f for v, f in zip(vals, fs))} \\div {n}$", "M1", "dep on M1"),
                   R("", num(float(mean)) if mean.denominator in (1, 2, 4, 5, 8, 10) else sf(mean, 3), "A1", "oe")],
             values={"mean": float(mean)}, diff="4-6", cw="Work out", refs=["F6.2B"])


@tpl("stats.averages", "stats", n=16)
def grouped_mean(r):
    k = r.choice([4, 5, 5, 6])
    lab, v, unit, desc = r.choice(CTX)
    b = classes(r, k)
    fs = [r.randint(2, 25) for _ in range(k)]
    n = sum(fs)
    mids = [F(b[i] + b[i + 1], 2) for i in range(k)]
    est = sum(m * f for m, f in zip(mids, fs)) / n
    modal = fs.index(max(fs))
    if fs.count(max(fs)) > 1:
        return None
    cum = 0
    for i, f in enumerate(fs):
        cum += f
        if cum >= F(n, 2):
            med_cls = i
            break
    rows_tbl = [[cls_label(b[i], b[i + 1], v), fs[i]] for i in range(k)]
    return Q(intro=f"The table summarises {desc.format(n=n)}.", figs=[table([lab.capitalize(), "Frequency"], rows_tbl)],
             parts=[P("a", "Write down the modal class.", 1, prefix=""),
                    P("b", "Write down the class interval that contains the median.", 1, prefix=""),
                    P("c", "Work out an estimate for the mean.", 4, prefix=unit)],
             rows=[R("a", cls_label(b[modal], b[modal + 1], v), "B1", ""),
                   R("b", cls_label(b[med_cls], b[med_cls + 1], v), "B1", ""),
                   R("c", "midpoints " + ", ".join(num(float(m)) for m in mids), "M1", "for at least 4 correct midpoints"),
                   R("c", "$" + " + ".join(f"{num(float(m))} \\times {f}" for m, f in zip(mids, fs)) + f" = {num(float(sum(m * f for m, f in zip(mids, fs))))}$", "M1",
                     "for products of frequencies with values in each class (consistent within the class, including the ends)"),
                   R("c", f"$\\div {n}$", "M1", "dep on M1 or the second M1"),
                   R("c", sf(est, 4) if F(est).denominator > 100 else num(float(est)), "A1", f"awrt {sf(est, 3)}")],
             values={"modal": [b[modal], b[modal + 1]], "median_class": [b[med_cls], b[med_cls + 1]], "mean": float(est)},
             diff="4-6", cw="Work out", refs=["F6.2C", "F6.2D", "F6.2B"])


@tpl("stats.averages", "problem", n=17)
def mean_algebra(r):
    xv = r.randint(3, 15)
    cs = sorted([(1, r.randint(-5, 10)), (2, r.randint(-5, 5)), (1, r.randint(0, 20)), (3, r.randint(-8, 2)), (1, r.randint(-3, 3))])
    vals = [c * xv + k for c, k in cs]
    if min(vals) <= 0 or len(set(vals)) < 5:
        return None
    m = F(sum(vals), 5)
    if m.denominator != 1:
        return None

    def lt(c, k):
        s = ("" if c == 1 else str(c)) + "x"
        return s + (f" + {k}" if k > 0 else (f" - {-k}" if k < 0 else ""))
    r.shuffle(cs)
    vals = [c * xv + k for c, k in cs]
    med = sorted(vals)[2]
    return Q(intro=f"Here are five expressions.\n\n$${', \\quad '.join(lt(c, k) for c, k in cs)}$$\n\nThe mean of the five expressions is {m}.",
             parts=[P("a", "Find the value of $x$.", 3, prefix="$x =$"),
                    P("b", "Find the median of the five values.", 1, prefix="")],
             rows=[R("a", f"${sum(c for c, _ in cs)}x + {sum(k for _, k in cs)}$".replace("+ -", "- ") + " seen", "M1", "for collecting the terms"),
                   R("a", f"$\\dfrac{{{sum(c for c, _ in cs)}x + {sum(k for _, k in cs)}}}{{5}} = {m}$".replace("+ -", "- "), "M1", ""),
                   R("a", str(xv), "A1", "cao"),
                   R("b", str(med), "B1", "ft their $x$")],
             values={"x": xv, "median": med}, diff="7-9", cw="Find", refs=["F6.2B"])


@tpl("stats.averages", "problem", n=17)
def mean_change(r):
    n = r.randint(8, 30)
    m1 = r.choice([F(k, 10) for k in range(150, 800, 5)])
    kind = r.choice(["join", "leave"])
    new = r.randint(5, 95)
    if kind == "join":
        m2 = (n * m1 + new) / (n + 1)
        if F(m2 * 10).denominator != 1:
            return None
        return Q(intro=f"{n} students took a test. Their mean mark was {num(float(m1))}.\n\nOne more student took the test. The mean mark for all {n + 1} students was {num(float(m2))}.",
                 parts=[P("", "Work out the mark of the extra student.", 3, prefix="")],
                 rows=[R("", f"${n} \\times {num(float(m1))} = {num(float(n * m1))}$", "M1", ""),
                       R("", f"${n + 1} \\times {num(float(m2))} - {num(float(n * m1))}$", "M1", ""),
                       R("", str(new), "A1", "cao")],
                 values={"mark": new}, diff="7-9", cw="Work out", refs=["F6.2B", "F6.2A"])
    m2 = (n * m1 - new) / (n - 1)
    if F(m2 * 10).denominator != 1 or m2 <= 0:
        return None
    return Q(intro=f"The mean weight of {n} parcels is {num(float(m1))} kg.\n\nOne parcel is removed. The mean weight of the other parcels is {num(float(m2))} kg.",
             parts=[P("", "Work out the weight of the parcel that was removed.", 3, prefix="kg")],
             rows=[R("", f"${n} \\times {num(float(m1))} = {num(float(n * m1))}$", "M1", ""),
                   R("", f"${num(float(n * m1))} - {n - 1} \\times {num(float(m2))}$", "M1", ""),
                   R("", str(new), "A1", "cao")],
             values={"weight": new}, diff="7-9", cw="Work out", refs=["F6.2B", "F6.2A"])


# ================================================================ 6.1 histograms
def hist_classes(r):
    lab, v, unit, desc = r.choice(CTX)
    start = r.choice([0, 10, 20, 40])
    ws = r.choice([[10, 10, 20, 30, 20], [5, 5, 10, 20, 10], [10, 20, 10, 20, 40], [20, 10, 10, 30, 30], [5, 10, 15, 10, 20],
                   [10, 5, 5, 20, 40], [20, 20, 10, 10, 40]])
    b = [start]
    for w in ws:
        b.append(b[-1] + w)
    # frequency densities on a grid of 0.2 steps
    fds = [F(r.randint(2, 24), 5) if w % 5 == 0 else F(r.randint(2, 24), 5) for w in ws]
    fs = [fd * w for fd, w in zip(fds, ws)]
    if any(f.denominator != 1 for f in fs):
        return None
    return lab, v, unit, desc, b, ws, fds, [int(f) for f in fs]


def hist_fig(b, fds, v, unit, show=None):
    show = show if show is not None else range(len(fds))
    ymax = max(5, math.ceil(float(max(fds)) + 0.5))
    step = 1

    def items(M):
        out = ""
        for i in show:
            pts = [M((b[i], 0)), M((b[i + 1], 0)), M((b[i + 1], float(fds[i]))), M((b[i], float(fds[i])))]
            out += PL(pts, close=True, w=2)
        return out
    xs = b[0], b[-1]
    xt = 10 if xs[1] - xs[0] >= 60 else 5
    return grid_fig(xs[0], xs[1], 0, ymax, xstep=xt, ystep=step, minor=5, items=items, xlabel=v, ylabel="Frequency density",
                    axes_at_zero=False, w=380, h=300)


@tpl("stats.histograms", "stats", n=8)
def hist_read(r):
    h = hist_classes(r)
    if h is None:
        return None
    lab, v, unit, desc, b, ws, fds, fs = h
    n = sum(fs)
    i = r.randrange(len(fs))
    cut = r.choice([x for x in range(b[0] + 1, b[-1]) if x not in b and x % 5 == 0] or [None])
    if cut is None:
        return None
    j = max(k for k in range(len(ws)) if b[k] < cut)
    above = F(b[j + 1] - cut) * fds[j] + sum(fs[j + 1:])
    s = hist_fig(b, fds, v, unit)
    return Q(intro=f"The histogram summarises {desc.format(n=n)}.", figs=[fig(s, 85, note=None)],
             parts=[P("a", f"Work out the number of values in the class ${b[i]} < {v} \\leqslant {b[i + 1]}$.", 2, prefix=""),
                    P("b", f"Work out an estimate for the number of values greater than {cut} {unit}.", 3, prefix="")],
             rows=[R("a", f"${num(float(fds[i]))} \\times {ws[i]}$", "M1", "frequency = frequency density × class width"),
                   R("a", str(fs[i]), "A1", "cao"),
                   R("b", f"${b[j + 1] - cut} \\times {num(float(fds[j]))}$", "M1", "for the part of the class containing " + str(cut)),
                   R("b", "$" + " + ".join([num(float((b[j + 1] - cut) * fds[j]))] + [str(f) for f in fs[j + 1:]]) + "$", "M1", "for adding the frequencies of the classes above"),
                   R("b", num(float(above)), "A1", "oe")],
             values={"freq": fs[i], "above": float(above)}, diff="7-9", cw="Work out", refs=["H6.1A"])


@tpl("stats.histograms", "stats", n=8)
def hist_total(r):
    h = hist_classes(r)
    if h is None:
        return None
    lab, v, unit, desc, b, ws, fds, fs = h
    n = sum(fs)
    known = r.randrange(len(fs))
    s = hist_fig(b, fds, v, unit)
    return Q(intro=f"The histogram represents the {lab.split(',')[0]} of some objects.\n\nThere are {fs[known]} objects in the class ${b[known]} < {v} \\leqslant {b[known + 1]}$.\n\nThe vertical scale has not been labelled with values.",
             figs=[fig(s, 85, note=None)],
             parts=[P("", "Work out the total number of objects.", 3, prefix="")],
             rows=[R("", f"scale: frequency density for that class is ${fs[known]} \\div {ws[known]} = {num(float(fds[known]))}$", "M1", "or for using area of bars, eg 1 small square = a known frequency"),
                   R("", "$" + " + ".join(str(f) for f in fs) + "$", "M1", "for at least 3 correct frequencies added"),
                   R("", str(n), "A1", "cao")],
             values={"total": n}, diff="7-9", cw="Work out", refs=["H6.1A"])


@tpl("stats.histograms", "graph", n=16)
def hist_draw(r):
    h = hist_classes(r)
    if h is None:
        return None
    lab, v, unit, desc, b, ws, fds, fs = h
    n = sum(fs)
    shown = r.sample(range(len(fs)), 2)
    s = hist_fig(b, fds, v, unit, show=shown)
    miss = [i for i in range(len(fs)) if i not in shown]
    return Q(intro=f"The table summarises {desc.format(n=n)}.",
             figs=[table([lab.capitalize(), "Frequency"], [[cls_label(b[i], b[i + 1], v), fs[i]] for i in range(len(fs))]),
                   fig(s, 85, note=None)],
             parts=[P("", "Use the information in the table to complete the histogram.", 3, space="none")],
             rows=[R("", "frequency densities " + ", ".join(num(float(fds[i])) for i in miss), "M1", "for at least 2 correct frequency densities, or a consistent scale from the bars shown"),
                   R("", f"bars for the classes {', '.join(f'${b[i]}$–${b[i + 1]}$' for i in miss)} at heights {', '.join(num(float(fds[i])) for i in miss)}", "A2",
                     "A1 for 2 correct bars")],
             values={"fd": [float(x) for x in fds]}, diff="7-9", cw="Complete", refs=["H6.1A"])


# ================================================================ 6.1 cumulative frequency
def cf_data(r):
    lab, v, unit, desc = r.choice(CTX)
    k = 6
    start = r.choice([0, 0, 10, 20])
    w = r.choice([10, 10, 20, 5])
    b = [start + w * i for i in range(k + 1)]
    shape = r.choice([[1, 3, 6, 5, 3, 1], [2, 5, 8, 4, 2, 1], [1, 2, 4, 7, 5, 2], [1, 4, 7, 6, 3, 1], [2, 4, 6, 6, 4, 2]])
    tot = r.choice([40, 60, 80, 100, 120, 160])
    fs = [max(1, round(s * tot / sum(shape) + r.randint(-2, 2))) for s in shape]
    cf = []
    c = 0
    for f in fs:
        c += f
        cf.append(c)
    return lab, v, unit, desc, b, fs, cf


def cf_fig(b, cf, v, plot=True):
    n = cf[-1]
    ymax = int(math.ceil(n / 10.0) * 10)
    ys = 10 if ymax <= 100 else 20

    def items(M):
        if not plot:
            return ""
        pts = [M((b[0], 0))] + [M((b[i + 1], cf[i])) for i in range(len(cf))]
        out = PL(pts, w=1.8)
        for p in pts[1:]:
            out += DOT(*p, r=2.2)
        return out
    return grid_fig(b[0], b[-1], 0, ymax, xstep=b[1] - b[0], ystep=ys, minor=5 if ys == 10 else 4, items=items, xlabel=v,
                    ylabel="Cumulative frequency", axes_at_zero=False, w=380, h=320)


@tpl("stats.cumulative", "graph", n=16)
def cf_draw(r):
    lab, v, unit, desc, b, fs, cf = cf_data(r)
    n = cf[-1]
    xs = [b[0]] + b[1:]
    ys = [0] + cf
    med = interp(xs, ys, n / 2)
    cut = r.choice([x for x in range(b[1], b[-1]) if x not in b and x % 5 == 0] or [b[2] + 1])
    gt = n - fwd(xs, ys, cut)
    s = cf_fig(b, cf, v, plot=False)
    return Q(intro=f"The table summarises {desc.format(n=n)}.",
             figs=[table([lab.capitalize(), "Frequency"], [[cls_label(b[i], b[i + 1], v), fs[i]] for i in range(len(fs))]),
                   fig(s, 85, note=None)],
             parts=[P("a", "Complete the cumulative frequency table.", 1, space="table"),
                    P("b", "On the grid, draw a cumulative frequency graph for your table.", 2, space="none"),
                    P("c", f"Use your graph to find an estimate for the number of values greater than {cut} {unit}.", 2, prefix="")],
             rows=[R("a", ", ".join(map(str, cf)), "B1", "all correct"),
                   R("b", f"points plotted at ({b[1]}, {cf[0]}), ..., ({b[-1]}, {cf[-1]}) and joined with a curve or line segments", "B2",
                     "B1 for at least 4 points plotted correctly at the ends of the intervals; ft their table"),
                   R("c", f"reading at {v} = {cut} from their graph (about {round(fwd(xs, ys, cut))})", "M1", ""),
                   R("c", f"{round(gt) - 2} to {round(gt) + 2}", "A1", f"ft their graph; value from straight-line joins {dp(gt, 1)}")],
             values={"cf": cf, "greater": gt, "median": med}, diff="7-9", cw="Draw", refs=["H6.1B", "H6.1C"])


@tpl("stats.cumulative", "stats", n=16)
def cf_read(r):
    lab, v, unit, desc, b, fs, cf = cf_data(r)
    n = cf[-1]
    xs = [b[0]] + b[1:]
    ys = [0] + cf
    med = interp(xs, ys, n / 2)
    lq, uq = interp(xs, ys, n / 4), interp(xs, ys, 3 * n / 4)
    iqr = uq - lq
    w = b[1] - b[0]
    tol = w / 10 * 2
    cut = r.choice([x for x in range(b[1], b[-1]) if x not in b and x % 5 == 0] or [b[2] + 1])
    less = fwd(xs, ys, cut)
    s = cf_fig(b, cf, v)
    return Q(intro=f"The graph shows cumulative frequencies for {desc.format(n=n)}.", figs=[fig(s, 85, note=None)],
             parts=[P("a", "Use the graph to find an estimate for the median.", 1, prefix=unit),
                    P("b", "Use the graph to find an estimate for the interquartile range.", 2, prefix=unit),
                    P("c", f"Use the graph to find an estimate for the number of values that are more than {cut} {unit}.", 2, prefix="")],
             rows=[R("a", f"{dp(med - tol, 1)} to {dp(med + tol, 1)}", "B1", f"reading at {num(n / 2)}"),
                   R("b", f"readings at {num(n / 4)} and {num(3 * n / 4)}: about {dp(lq, 1)} and {dp(uq, 1)}", "M1", ""),
                   R("b", f"{dp(iqr - tol, 1)} to {dp(iqr + tol, 1)}", "A1", ""),
                   R("c", f"reading at {cut}: about {round(less)}", "M1", ""),
                   R("c", f"{round(n - less) - 2} to {round(n - less) + 2}", "A1", "")],
             values={"median": med, "iqr": iqr, "more": n - less}, diff="7-9", cw="Find", refs=["H6.2A", "H6.2D", "H6.1C"])


# ================================================================ 6.2 spread
def quartiles(xs):
    s = sorted(xs)
    n = len(s)

    def pos(p):
        k = p - 1
        lo = int(math.floor(k))
        if lo == k:
            return F(s[lo])
        return F(s[lo] + s[lo + 1], 2)
    return pos(F(n + 1, 4)), pos(F(n + 1, 2)), pos(F(3 * (n + 1), 4))


@tpl("stats.spread", "short", n=8)
def quartiles_list(r):
    n = r.choice([7, 11, 15, 19])
    data = [r.randint(5, 60) for _ in range(n)]
    lq, med, uq = quartiles(data)
    ordered = r.random() < 0.5
    show = sorted(data) if ordered else data
    ctx = r.choice(["the numbers of minutes", "the ages, in years,", "the scores", "the numbers of points"])
    return Q(intro=f"Here are {ctx} of {n} people.\n\n$${', \\; '.join(map(str, show))}$$",
             parts=[P("", "Work out the interquartile range.", 3, prefix="")],
             rows=[R("", "ordered list" if not ordered else f"lower quartile ({num(F(n + 1, 4))}th value) or upper quartile ({num(F(3 * (n + 1), 4))}th value)", "M1", "may be implied"),
                   R("", f"lower quartile $= {num(lq)}$ and upper quartile $= {num(uq)}$", "M1", ""),
                   R("", num(uq - lq), "A1", "cao")],
             values={"lq": lq, "uq": uq, "iqr": uq - lq}, diff="4-6", cw="Work out", refs=["H6.2C"])


@tpl("stats.spread", "short", n=8)
def quartiles_freq(r):
    vals = list(range(r.choice([0, 1]), 7))
    fs = [r.randint(1, 9) for _ in vals]
    n = sum(fs)
    if (n + 1) % 4:
        return None
    data = [v for v, f in zip(vals, fs) for _ in range(f)]
    lq, med, uq = quartiles(data)
    item = r.choice(["number of hours of homework", "number of times late", "number of drinks bought", "number of emails sent"])
    return Q(intro=f"The table shows information about the {item} last week for {n} people.",
             figs=[table(["Number", "Frequency"], [[v, f] for v, f in zip(vals, fs)])],
             parts=[P("a", "Find the median.", 1, prefix=""), P("b", "Work out the interquartile range.", 2, prefix="")],
             rows=[R("a", num(med), "B1", f"{num(F(n + 1, 2))}th value"),
                   R("b", f"{num(F(n + 1, 4))}th and {num(F(3 * (n + 1), 4))}th values: ${num(lq)}$ and ${num(uq)}$", "M1", ""),
                   R("b", num(uq - lq), "A1", "cao")],
             values={"median": med, "iqr": uq - lq}, diff="7-9", cw="Work out", refs=["H6.2C", "F6.2B"])


@tpl("stats.spread", "stats", n=16)
def compare_distributions(r):
    n = r.choice([11, 15, 19])
    a = [r.randint(10, 70) for _ in range(n)]
    lq, med, uq = quartiles(a)
    m2 = med + r.choice([-9, -6, -4, 4, 6, 9])
    i2 = (uq - lq) + r.choice([-6, -4, -3, 3, 4, 6])
    if i2 <= 0:
        return None
    g = r.choice([("Year 10", "Year 11", "times, in seconds, to complete a puzzle", "in"), ("Team A", "Team B", "scores in a quiz", "in"),
                  ("Monday", "Friday", "journey times, in minutes,", "on"), ("Group P", "Group Q", "reaction times, in hundredths of a second,", "in")])
    better_low = "times" in g[2]
    return Q(intro=f"Here are the {g[2]} for {n} people {g[3]} {g[0]}.\n\n$${', \\; '.join(map(str, sorted(a)))}$$",
             parts=[P("a", f"Find the median and the interquartile range for {g[0]}.", 3, space="working"),
                    P("b", f"For {g[1]}, the median was {num(m2)} and the interquartile range was {num(i2)}.\n\nCompare the distributions for {g[0]} and {g[1]}.", 2, space="lines", lines=4)],
             rows=[R("a", f"median $= {num(med)}$", "B1", ""),
                   R("a", f"lower quartile $= {num(lq)}$ or upper quartile $= {num(uq)}$", "M1", ""),
                   R("a", f"interquartile range $= {num(uq - lq)}$", "A1", ""),
                   R("b", f"a correct comparison of the medians, eg the median for {g[0] if med > m2 else g[1]} is higher" + (", so on average they took longer" if better_low else ", so on average they scored more"), "B1",
                     "ft their median; must be in context for full marks"),
                   R("b", f"a correct comparison of the interquartile ranges, eg the {g[2].split(',')[0]} for {g[0] if (uq - lq) > i2 else g[1]} were more spread out (less consistent)", "B1",
                     "ft their IQR; a comparison of the ranges does not score")],
             values={"median": med, "iqr": uq - lq}, diff="7-9", cw="Compare", refs=["H6.2B", "H6.2C", "F6.2A"])


# ================================================================ 6.3 probability
@tpl("stats.probability", "short", n=17)
def prob_table(r):
    labels = r.choice([["red", "blue", "green", "yellow"], ["1", "2", "3", "4", "5"], ["A", "B", "C", "D"], ["win", "lose", "draw"]])
    k = len(labels)
    ps = [F(r.randint(5, 40), 100) for _ in range(k - 1)]
    last = 1 - sum(ps)
    if last <= F(4, 100):
        return None
    ps.append(last)
    miss = r.randrange(k)
    obj = r.choice(["a biased spinner", "a biased dice", "a game"]) if labels[0] != "win" else "a game"
    trials = r.choice([50, 80, 120, 150, 200, 250, 300, 400, 500])
    j = r.choice([i for i in range(k) if i != miss])
    shown = [dp(float(p), 2) if i != miss else "" for i, p in enumerate(ps)]
    return Q(intro=f"The table shows the probabilities of the possible outcomes for {obj}.",
             figs=[table(["Outcome"] + labels, [["Probability"] + shown])],
             parts=[P("a", f"Work out the probability of {labels[miss]}." if labels[0] != "1" else f"Work out the probability of a {labels[miss]}.", 2, prefix=""),
                    P("b", f"The {'spinner is spun' if 'spinner' in obj else ('dice is rolled' if 'dice' in obj else 'game is played')} {trials} times.\n\nWork out an estimate for the number of times the outcome is {labels[j]}.", 2, prefix="")],
             rows=[R("a", f"$1 - ({' + '.join(dp(float(p), 2) for i, p in enumerate(ps) if i != miss)})$", "M1", ""),
                   R("a", dp(float(ps[miss]), 2), "A1", "oe"),
                   R("b", f"${dp(float(ps[j]), 2)} \\times {trials}$", "M1", ""),
                   R("b", num(float(ps[j] * trials)), "A1", "cao")],
             values={"p": float(ps[miss]), "expected": float(ps[j] * trials)}, diff="4-6", cw="Work out", refs=["F6.3H", "F6.3J", "F6.3I"])


@tpl("stats.probability", "short", n=17)
def relative_freq(r):
    nm = name(r)
    n = r.choice([40, 50, 60, 80, 100, 120, 150, 200])
    k = r.randint(n // 10, n * 8 // 10)
    obj = r.choice([("drawing pin", "lands point up", "drops"), ("biased coin", "lands on heads", "flips"),
                    ("spinner", "lands on 6", "spins"), ("paper cup", "lands on its side", "throws")])
    m = r.choice([300, 400, 500, 600, 750, 1000, 1200])
    rf = F(k, n)
    return Q(intro=f"{nm} {obj[2]} a {obj[0]} {n} times. It {obj[1]} {k} times.",
             parts=[P("a", f"Write down the relative frequency that the {obj[0]} {obj[1]}.", 1, prefix=""),
                    P("b", f"{nm} is going to {obj[2][:-1] if obj[2] != 'flips' else 'flip'} the {obj[0]} {m} more times.\n\nWork out an estimate for the number of times it {obj[1]}.", 2, prefix="")],
             rows=[R("a", f"${ftex(rf)}$", "B1", "oe"),
                   R("b", f"${ftex(rf)} \\times {m}$", "M1", "ft their (a)"),
                   R("b", num(float(rf * m)), "A1", "accept the nearest whole number")],
             values={"rf": rf, "estimate": float(rf * m)}, diff="4-6", cw="Write down", refs=["F6.3G", "F6.3J"])


@tpl("stats.probability", "problem", n=17)
def prob_algebra(r):
    k = 4
    cs = [r.choice([1, 2, 3]) for _ in range(k)]
    ks = [F(r.choice([0, 0, 5, 10, -5]), 100) for _ in range(k)]
    tot = sum(cs)
    xv = (1 - sum(ks)) / tot
    if xv <= 0 or F(xv * 100).denominator != 1:
        return None
    ps = [c * xv + kk for c, kk in zip(cs, ks)]
    if min(ps) <= 0:
        return None
    labels = r.choice([["red", "blue", "green", "white"], ["1", "2", "3", "4"], ["A", "B", "C", "D"]])

    def lt(c, kk):
        s = ("" if c == 1 else str(c)) + "x"
        if kk > 0:
            s += f" + {dp(float(kk), 2)}"
        elif kk < 0:
            s += f" - {dp(float(-kk), 2)}"
        return f"${s}$"
    i, j = r.sample(range(k), 2)
    return Q(intro=f"A bag contains counters. Each counter is labelled {', '.join(labels[:-1])} or {labels[-1]}.\n\nA counter is taken at random from the bag. The table shows the probability of each label.",
             figs=[table(["Label"] + labels, [["Probability"] + [lt(c, kk) for c, kk in zip(cs, ks)]])],
             parts=[P("", f"Work out the probability that the counter is labelled {labels[i]} or {labels[j]}.", 4, prefix="")],
             rows=[R("", f"${tot}x + {dp(float(sum(ks)), 2)} = 1$".replace("+ -", "- ").replace(" + 0.00", ""), "M1", "for a correct equation"),
                   R("", f"$x = {dp(float(xv), 2)}$", "A1", ""),
                   R("", f"${lt(cs[i], ks[i])[1:-1]} + {lt(cs[j], ks[j])[1:-1]}$ with their $x$", "M1", "for adding the two probabilities (mutually exclusive)"),
                   R("", dp(float(ps[i] + ps[j]), 2), "A1", "oe")],
             values={"x": float(xv), "p": float(ps[i] + ps[j])}, diff="7-9", cw="Work out", refs=["F6.3I", "F6.3H"])


@tpl("stats.probability", "problem", n=17)
def venn_prob(r):
    a, ab, b, out = r.randint(2, 20), r.randint(1, 12), r.randint(2, 20), r.randint(1, 15)
    n = a + ab + b + out
    grp = r.choice([("F", "B", "football", "basketball"), ("T", "C", "tea", "coffee"), ("G", "H", "geography", "history"),
                    ("S", "M", "swimming", "music")])
    kind = r.choice(["union_not", "one_only", "not_both"])
    if kind == "union_not":
        num_, desc = out, f"does not play/like either {grp[2]} or {grp[3]}"
        desc = f"is not in set ${grp[0]}$ and is not in set ${grp[1]}$"
    elif kind == "one_only":
        num_, desc = a + b, f"is in exactly one of the sets ${grp[0]}$ and ${grp[1]}$"
    else:
        num_, desc = n - ab, f"is not in ${grp[0]} \\cap {grp[1]}$"
    p2 = F(a + ab + b, n)
    s = venn_fig([grp[0], grp[1]], [str(a), str(ab), str(b)], outside=str(out))
    return Q(intro=f"There are {n} students in a club.\n\n${grp[0]}$ is the set of students who study {grp[2]}. ${grp[1]}$ is the set of students who study {grp[3]}.\n\nThe Venn diagram shows the number of students in each region.",
             figs=[fig(s, 65, note=None)],
             parts=[P("a", f"One of the students is chosen at random.\n\nFind the probability that this student {desc}.", 2, prefix=""),
                    P("b", f"Find $P({grp[0]} \\cup {grp[1]})$.", 1, prefix=""),
                    P("c", f"A student who studies {grp[3]} is chosen at random.\n\nFind the probability that this student also studies {grp[2]}.", 2, prefix="")],
             rows=[R("a", f"${num_}$ out of ${n}$", "M1", ""), R("a", f"${ftex(F(num_, n))}$", "A1", "oe"),
                   R("b", f"${ftex(p2)}$", "B1", "oe"),
                   R("c", f"denominator ${ab + b}$", "M1", ""), R("c", f"${ftex(F(ab, ab + b))}$", "A1", "oe")],
             values={"a": F(num_, n), "b": p2, "c": F(ab, ab + b)}, diff="7-9", cw="Find", refs=["F6.3D", "H6.3C"])


@tpl("stats.probability", "problem", n=16)
def sample_space(r):
    s1 = r.choice([[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [2, 3, 5, 7], [0, 1, 2, 3]])
    s2 = r.choice([[1, 2, 3], [1, 2, 3, 4, 5, 6], [2, 4, 6, 8], [1, 3, 5], [1, 2, 3, 4]])
    op = r.choice(["sum", "product"])
    vals = [(a + b if op == "sum" else a * b) for a in s1 for b in s2]
    cond = r.choice(["more", "even", "equal"])
    if cond == "more":
        t = sorted(vals)[len(vals) // 2]
        good = [v for v in vals if v > t]
        desc = f"is greater than {t}"
    elif cond == "even":
        good = [v for v in vals if v % 2 == 0]
        desc = "is an even number"
    else:
        t = r.choice(vals)
        good = [v for v in vals if v == t]
        desc = f"is {t}"
    if not good or len(good) == len(vals):
        return None
    p = F(len(good), len(vals))
    return Q(intro=f"Spinner A has {len(s1)} equal sections labelled {', '.join(map(str, s1))}.\nSpinner B has {len(s2)} equal sections labelled {', '.join(map(str, s2))}.\n\nBoth spinners are spun once. The {op} of the two numbers is the score.",
             parts=[P("", f"Work out the probability that the score {desc}.", 3, prefix="")],
             rows=[R("", f"a sample space with all {len(vals)} outcomes", "M1", "or a correct systematic list"),
                   R("", f"{len(good)} favourable outcomes identified", "M1", ""),
                   R("", f"${ftex(p)}$", "A1", "oe")],
             values={"p": p}, diff="4-6", cw="Work out", refs=["F6.3E"])


# ================================================================ 6.3 combined events
@tpl("stats.combined", "stats", n=16)
def tree_complete(r):
    pa = F(r.randint(2, 18), 20)
    pb = F(r.randint(2, 18), 20)
    ctx = r.choice([("passes the theory test", "passes the practical test", "Theory", "Practical", "pass", "fail"),
                    ("is late on Monday", "is late on Tuesday", "Monday", "Tuesday", "late", "not late"),
                    ("hits the target with the first arrow", "hits the target with the second arrow", "First arrow", "Second arrow", "hit", "miss"),
                    ("wins the first game", "wins the second game", "First game", "Second game", "win", "not win")])
    nm = name(r)
    s = tree_fig([dp(float(pa), 2), ""], [[dp(float(pb), 2), ""], ["", ""]], [ctx[4], ctx[5]], [[ctx[4], ctx[5]], [ctx[4], ctx[5]]])
    one = pa * (1 - pb) + (1 - pa) * pb
    least = 1 - (1 - pa) * (1 - pb)
    ask = r.choice(["exactly", "least"])
    return Q(intro=f"The probability that {nm} {ctx[0]} is {dp(float(pa), 2)}.\nThe probability that {nm} {ctx[1]} is {dp(float(pb), 2)}.\nThe two events are independent.",
             figs=[fig(s, 75, note=None, caption=f"{ctx[2]} → {ctx[3]}")],
             parts=[P("a", "Complete the probability tree diagram.", 2, space="none"),
                    P("b", f"Work out the probability that {nm} has the outcome '{ctx[4]}' both times.", 2, prefix=""),
                    P("c", f"Work out the probability that {nm} has the outcome '{ctx[4]}' " + ("exactly once." if ask == "exactly" else "at least once."), 3, prefix="")],
             rows=[R("a", f"{dp(float(1 - pa), 2)} on the first set of branches", "B1", ""),
                   R("a", f"{dp(float(pb), 2)}, {dp(float(1 - pb), 2)} correctly placed on all second branches", "B1", ""),
                   R("b", f"${dp(float(pa), 2)} \\times {dp(float(pb), 2)}$", "M1", "ft their tree"),
                   R("b", dp(float(pa * pb), 4).rstrip("0").rstrip("."), "A1", "oe"),
                   R("c", f"${dp(float(pa), 2)} \\times {dp(float(1 - pb), 2)}$ or ${dp(float(1 - pa), 2)} \\times {dp(float(pb), 2)}$" if ask == "exactly"
                     else f"${dp(float(1 - pa), 2)} \\times {dp(float(1 - pb), 2)}$", "M1", "ft their tree"),
                   R("c", "sum of both products" if ask == "exactly" else f"$1 - {dp(float((1 - pa) * (1 - pb)), 4)}$", "M1", "or adding the three correct products" if ask == "least" else ""),
                   R("c", dp(float(one if ask == "exactly" else least), 4).rstrip("0").rstrip("."), "A1", "oe")],
             values={"both": pa * pb, "c": one if ask == "exactly" else least}, diff="7-9", cw="Work out", refs=["H6.3A", "H6.3B"])


@tpl("stats.combined", "problem", n=8)
def without_replacement(r):
    cols = r.sample(["red", "blue", "green", "yellow", "white", "black"], r.choice([2, 3]))
    ns = [r.randint(2, 9) for _ in cols]
    n = sum(ns)
    kind = r.choice(["same", "different", "least_one"])
    if kind == "same":
        p = sum(F(k * (k - 1), n * (n - 1)) for k in ns)
        desc = "both counters are the same colour"
        m1 = " + ".join(f"\\frac{{{k}}}{{{n}}} \\times \\frac{{{k - 1}}}{{{n - 1}}}" for k in ns)
    elif kind == "different":
        p = 1 - sum(F(k * (k - 1), n * (n - 1)) for k in ns)
        desc = "the two counters are different colours"
        m1 = "1 - (" + " + ".join(f"\\frac{{{k}}}{{{n}}} \\times \\frac{{{k - 1}}}{{{n - 1}}}" for k in ns) + ")"
    else:
        k = ns[0]
        p = 1 - F((n - k) * (n - k - 1), n * (n - 1))
        desc = f"at least one of the counters is {cols[0]}"
        m1 = f"1 - \\frac{{{n - k}}}{{{n}}} \\times \\frac{{{n - k - 1}}}{{{n - 1}}}"
    items = ", ".join(f"{k} {c}" for k, c in zip(ns[:-1], cols[:-1])) + f" and {ns[-1]} {cols[-1]}"
    return Q(intro=f"There are {n} counters in a bag: {items} counters.\n\nTwo counters are taken at random from the bag, without replacement.",
             parts=[P("", f"Work out the probability that {desc}.", 4, prefix="")],
             rows=[R("", f"$\\frac{{{ns[0]}}}{{{n}}} \\times \\frac{{{ns[0] - 1}}}{{{n - 1}}}$ or another correct product", "M1", "for one correct product with denominators $" + f"{n}$ and ${n - 1}$"),
                   R("", "all the products needed for their method", "M1", ""),
                   R("", f"${m1}$", "M1", "for a complete correct method"),
                   R("", f"${ftex(p)}$", "A1", "oe")],
             values={"p": p}, diff="7-9", cw="Work out", refs=["H6.3C", "H6.3D"])


@tpl("stats.combined", "problem", n=8)
def reverse_prob(r):
    red = r.randint(2, 8)
    blue = r.randint(2, 12)
    n = red + blue
    p = F(red * (red - 1), n * (n - 1))
    return Q(intro=f"A bag contains {red} red sweets and $x$ blue sweets.\n\n{name(r)} takes two sweets at random from the bag, without replacement.\n\nThe probability that both sweets are red is ${ftex(p)}$.",
             parts=[P("", "Work out the value of $x$.\n\nShow clear algebraic working.", 5, prefix="$x =$")],
             rows=[R("", f"$\\dfrac{{{red}}}{{{red} + x}} \\times \\dfrac{{{red - 1}}}{{{red - 1} + x}} = {ftex(p)}$", "M1", ""),
                   R("", f"${red * (red - 1) * p.denominator} = {'' if p.numerator == 1 else p.numerator}({red} + x)({red - 1} + x)$", "M1", "for removing fractions"),
                   R("", "a correct three-term quadratic equal to zero", "A1", ""),
                   R("", "correct method to solve their quadratic", "M1", ""),
                   R("", str(blue), "A1", "dep on M2; reject any negative solution")],
             values={"x": blue}, diff="7-9", cw="Work out", refs=["H6.3C", "H6.3D"])


@tpl("stats.combined", "structured", n=16)
def combined_struct(r):
    pr = F(r.randint(3, 17), 20)
    pl_r = F(r.randint(1, 9), 20)
    pl_n = F(r.randint(1, 9), 20)
    if pl_n == pl_r:
        return None
    nm = name(r)
    days = r.choice([60, 100, 120, 150, 180, 200, 250, 300])
    s = tree_fig(["", ""], [["", ""], ["", ""]], ["rain", "no rain"], [["late", "not late"], ["late", "not late"]])
    pl = pr * pl_r + (1 - pr) * pl_n
    cond = pr * pl_r / pl
    return Q(intro=(f"The probability that it rains on any day is {dp(float(pr), 2)}.\n\nIf it rains, the probability that {nm} is late for work is {dp(float(pl_r), 2)}.\n"
                    f"If it does not rain, the probability that {nm} is late for work is {dp(float(pl_n), 2)}."),
             figs=[fig(s, 75, note=None)],
             parts=[P("a", "Complete the probability tree diagram.", 2, space="none"),
                    P("b", f"Work out the probability that {nm} is late for work on a day chosen at random.", 3, prefix=""),
                    P("c", f"Work out an estimate for the number of days {nm} is late in {days} working days.", 1, prefix=""),
                    P("d", f"On one day, {nm} is late for work.\n\nWork out the probability that it rained on that day.", 2, prefix="")],
             rows=[R("a", f"{dp(float(pr), 2)}, {dp(float(1 - pr), 2)} on the first branches", "B1", ""),
                   R("a", f"{dp(float(pl_r), 2)}, {dp(float(1 - pl_r), 2)}, {dp(float(pl_n), 2)}, {dp(float(1 - pl_n), 2)} on the second branches", "B1", ""),
                   R("b", f"${dp(float(pr), 2)} \\times {dp(float(pl_r), 2)}$ or ${dp(float(1 - pr), 2)} \\times {dp(float(pl_n), 2)}$", "M1", ""),
                   R("b", "sum of the two products", "M1", ""),
                   R("b", dp(float(pl), 4).rstrip("0").rstrip("."), "A1", "oe"),
                   R("c", num(float(pl * days)), "B1", "ft their (b)"),
                   R("d", f"$\\dfrac{{{dp(float(pr * pl_r), 4)}}}{{{dp(float(pl), 4)}}}$", "M1", "ft their (b)"),
                   R("d", f"${ftex(cond)}$", "A1", f"oe, awrt {sf(cond, 3)}")],
             values={"late": pl, "days": float(pl * days), "cond": cond}, diff="7-9", cw="Work out", refs=["H6.3A", "H6.3C", "H6.3D"])
