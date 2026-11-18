"""Diagram (draw / label, 3 marks) question builders for economics. All figures are original inline SVG.

Each builder yields dicts: text, svg, rows (list of (answer, notes)), diff.
"""
import economics_svg as G
from economics_util import fill, cap

SHIFT_NOTE = "Award 0 marks if both curves are shifted or the wrong curve is shifted. Accept curved or straight lines; labels such as D1/S1, P1 and Q1 or equivalent."


def _dir_effects(curve, d):
    if curve == "D":
        return ("higher", "higher") if d > 0 else ("lower", "lower")
    return ("lower", "higher") if d > 0 else ("higher", "lower")


def sd_question(event, curve, d, market, xlabel, ylabel, pname="equilibrium price", qname="equilibrium quantity",
                plab="Pe", qlab="Qe", cname=None):
    pe, qe = _dir_effects(curve, d)
    cname = cname or ("demand" if curve == "D" else "supply")
    text = (f"{event}\n\nFigure 1 shows the {market}. On Figure 1, draw the likely effect of this change. "
            f"Label the new curve, the new {pname} and the new {qname}.")
    svg = G.sd_base(xlabel, ylabel, plab=plab, qlab=qlab)
    rows = [(f"The {cname} curve shifts to the {'right' if d > 0 else 'left'}, labelled ({curve}1)", SHIFT_NOTE),
            (f"New {pname} identified and labelled, {pe} than {plab}", None),
            (f"New {qname} identified and labelled, {qe} than {qlab}", None)]
    return dict(text=text, svg=svg, rows=rows, diff="4-6")


# ------------------------------------------------------------ product markets

DPRODS = [("coffee", "tea", "milk"), ("cinema tickets", "streaming subscriptions", "popcorn"), ("butter", "margarine", "bread"),
          ("games consoles", "gaming laptops", "video games"), ("tennis rackets", "badminton rackets", "tennis balls"),
          ("petrol cars", "electric cars", "petrol"), ("printers", "tablet computers", "ink cartridges"), ("hot dogs", "burgers", "hot dog rolls")]
MASS = {"coffee", "butter", "petrol", "rice", "bread", "steel", "orange juice", "chocolate", "salt", "electricity", "tap water"}  # take "is"
DEVENTS = [("Average incomes in {city} rise. {Prod} {be} a normal good.", 1),
           ("A recession causes average incomes in {city} to fall. {Prod} {be} a normal good.", -1),
           ("The price of {sub}, a substitute for {prod}, rises.", 1),
           ("The price of {sub}, a substitute for {prod}, falls.", -1),
           ("The price of {comp}, a complement to {prod}, rises.", -1),
           ("The price of {comp}, a complement to {prod}, falls.", 1),
           ("A successful advertising campaign makes {prod} more fashionable in {city}.", 1),
           ("Consumer tastes in {city} move away from {prod}.", -1),
           ("The population of {city} grows rapidly as people move there for work.", 1)]

SPRODS = [("rice", "fertiliser"), ("cotton shirts", "cotton"), ("wooden chairs", "timber"), ("solar panels", "silicon"),
          ("chocolate", "cocoa beans"), ("bread", "flour"), ("steel", "iron ore"), ("orange juice", "oranges")]
SEVENTS = [("The cost of {inp}, a key raw material for {prod}, rises sharply.", -1),
           ("Producers of {prod} introduce new technology that lowers their costs.", 1),
           ("Wages paid to workers producing {prod} rise.", -1),
           ("The government of {nation} gives producers of {prod} a subsidy.", 1),
           ("The government of {nation} places an indirect tax on {prod}.", -1),
           ("Several new firms enter the market for {prod} in {nation}.", 1),
           ("A number of producers of {prod} in {nation} go out of business.", -1),
           ("The cost of the energy used to make {prod} falls.", 1)]


def demand_events(r, c):
    prod, sub, comp = r.choice(DPRODS)
    ev, d = r.choice(DEVENTS)
    c2 = dict(c, prod=prod, Prod=cap(prod), sub=sub, comp=comp, be="is" if prod in MASS else "are")
    return sd_question(fill(ev, c2, r), "D", d, f"market for {prod} in {c['city']}", f"Quantity of {prod}", "Price")


def supply_events(r, c):
    prod, inp = r.choice(SPRODS)
    ev, d = r.choice(SEVENTS)
    c2 = dict(c, prod=prod, inp=inp)
    return sd_question(fill(ev, c2, r), "S", d, f"market for {prod} in {c['nation']}", f"Quantity of {prod}", "Price")


def price_events(r, c):
    return demand_events(r, c) if r.random() < 0.5 else supply_events(r, c)


# ------------------------------------------------------------ elasticity

EPRODS = ["salt", "petrol", "designer jeans", "a brand of crisps", "tap water", "foreign holidays", "cigarettes", "a brand of trainers",
          "electricity", "restaurant meals"]


def ped_draw(r, c):
    prod = r.choice(EPRODS)
    kind = r.choice(["elastic", "inelastic"])
    move = r.choice(["rise", "fall"])
    steep = "steep" if kind == "inelastic" else "shallow (flat)"
    prop = "smaller" if kind == "inelastic" else "larger"
    text = (f"{c['firm']} has found that the demand for {prod} is price {kind}.\n\nOn the axes in Figure 1, draw a demand curve for {prod} "
            f"and use it to show the effect on quantity demanded of a {move} in price from P1 to P2.")
    rows = [(f"Demand curve drawn relatively {steep} and labelled D", "Do not accept a perfectly elastic or perfectly inelastic curve."),
            (f"P1 and P2 shown on the price axis, with P2 {'above' if move == 'rise' else 'below'} P1", None),
            (f"Q1 and Q2 shown, with the change in quantity demanded proportionately {prop} than the change in price", None)]
    return dict(text=text, svg=G.blank_axes(f"Quantity of {prod}", "Price"), rows=rows, diff="4-6")


SUPP_E = [("wheat", "in the short run, because crops take months to grow"), ("houses", "because building takes a long time"),
          ("plastic bottles", "because spare capacity and stocks are available"), ("T-shirts", "because production can be increased quickly"),
          ("coffee beans", "because new coffee plants take years to mature"), ("printed books", "because extra copies can be printed quickly"),
          ("fresh fish", "because catches are limited by fish stocks"), ("phone cases", "because factories have large stocks")]


def pes_draw(r, c):
    prod, why = r.choice(SUPP_E)
    kind = "inelastic" if any(w in why for w in ("long", "months", "years", "limited")) else "elastic"
    move = r.choice(["rise", "fall"])
    steep = "steep" if kind == "inelastic" else "shallow (flat)"
    prop = "smaller" if kind == "inelastic" else "larger"
    text = (f"The supply of {prod} in {c['nation']} is price {kind} {why}.\n\nOn the axes in Figure 1, draw a supply curve for {prod} "
            f"and use it to show the effect on quantity supplied of a {move} in price from P1 to P2.")
    rows = [(f"Upward-sloping supply curve drawn relatively {steep} and labelled S", None),
            (f"P1 and P2 shown on the price axis, with P2 {'above' if move == 'rise' else 'below'} P1", None),
            (f"Q1 and Q2 shown, with the change in quantity supplied proportionately {prop} than the change in price", None)]
    return dict(text=text, svg=G.blank_axes(f"Quantity of {prod}", "Price"), rows=rows, diff="4-6")


# ------------------------------------------------------------ intervention and externalities

BADS = ["cigarettes", "sugary drinks", "petrol", "plastic bags", "fast food", "single-use plastic cups"]
GOODS = ["solar panels", "bicycles", "home insulation", "electric cars", "bus travel", "flu vaccinations"]


def intervention_draw(r, c):
    k = r.randrange(4)
    n = c["nation"]
    if k == 0:
        prod = r.choice(BADS)
        return sd_question(f"The government of {n} places an indirect tax on {prod}.", "S", -1, f"market for {prod} in {n}", f"Quantity of {prod}", "Price")
    if k == 1:
        prod = r.choice(GOODS)
        return sd_question(f"The government of {n} gives producers of {prod} a subsidy for each unit sold.", "S", 1, f"market for {prod} in {n}", f"Quantity of {prod}", "Price")
    if k == 2:
        prod = r.choice(["rented flats", "bread", "baby milk", "cooking oil", "bus tickets"])
        text = (f"The government of {n} sets a maximum price for {prod} below the equilibrium price.\n\nOn Figure 1, draw the maximum price "
                f"and label the quantity demanded, the quantity supplied and the resulting shortage.")
        rows = [("Maximum price drawn as a horizontal line below Pe and labelled (e.g. Pmax)", None),
                ("Quantity supplied (Qs) and quantity demanded (Qd) at the maximum price identified on the quantity axis", "Qs must be to the left of Qe and Qd to the right of Qe."),
                ("Shortage/excess demand shown as the distance between Qs and Qd", None)]
        return dict(text=text, svg=G.sd_base(f"Quantity of {prod}", "Price"), rows=rows, diff="7-9")
    prod = r.choice(["wheat", "rice", "milk", "sugar cane", "coffee beans"])
    text = (f"The government of {n} sets a minimum price for {prod} above the equilibrium price to support farmers.\n\nOn Figure 1, draw the minimum price "
            f"and label the quantity demanded, the quantity supplied and the resulting surplus.")
    rows = [("Minimum price drawn as a horizontal line above Pe and labelled (e.g. Pmin)", None),
            ("Quantity demanded (Qd) and quantity supplied (Qs) at the minimum price identified on the quantity axis", "Qd must be to the left of Qe and Qs to the right of Qe."),
            ("Surplus/excess supply shown as the distance between Qd and Qs", None)]
    return dict(text=text, svg=G.sd_base(f"Quantity of {prod}", "Price"), rows=rows, diff="7-9")


def ext_draw(r, c):
    k = r.randrange(5)
    n = c["nation"]
    if k == 0:
        p = r.choice(BADS)
        return sd_question(f"To reduce the external costs of consumption, the government of {n} places a tax on {p}.", "S", -1, f"market for {p} in {n}", f"Quantity of {p}", "Price")
    if k == 1:
        p = r.choice(GOODS)
        return sd_question(f"Because {p} create external benefits, the government of {n} gives producers a subsidy.", "S", 1, f"market for {p} in {n}", f"Quantity of {p}", "Price")
    if k == 2:
        p = r.choice(BADS)
        return sd_question(f"A government advertising campaign in {n} warns people about the harmful effects of {p}.", "D", -1, f"market for {p} in {n}", f"Quantity of {p}", "Price")
    if k == 3:
        p = r.choice(["steel", "cement", "paper", "chemicals", "electricity from coal"])
        return sd_question(f"New regulations in {n} force producers of {p} to fit expensive equipment to reduce pollution.", "S", -1, f"market for {p} in {n}", f"Quantity of {p}", "Price")
    p = r.choice(GOODS)
    return sd_question(f"A government information campaign in {n} encourages more people to use {p}.", "D", 1, f"market for {p} in {n}", f"Quantity of {p}", "Price")


# ------------------------------------------------------------ labour, currency, trade

JOBS = ["nurse", "electrician", "software engineer", "bus driver", "teacher", "plumber", "chef", "pilot"]
LEVENTS = [("Demand for the goods and services that {job}s help to provide rises.", "D", 1),
           ("New technology replaces many of the tasks done by {job}s.", "D", -1),
           ("Many more students train to become {job}s.", "S", 1),
           ("Large numbers of {job}s retire or emigrate.", "S", -1),
           ("The qualifications needed to become {a_job} become harder to obtain.", "S", -1),
           ("The government pays for free training courses for people who want to become {job}s.", "S", 1),
           ("The productivity of {job}s rises, so each worker is worth more to employers.", "D", 1)]


def labour_draw(r, c):
    job = r.choice(JOBS)
    ev, cv, d = r.choice(LEVENTS)
    ev = ev.format(job=job, a_job=("an " if job[0] in "aeiou" else "a ") + job)
    return sd_question(f"{ev} This affects the labour market for {job}s in {c['nation']}.", cv, d, f"labour market for {job}s in {c['nation']}",
                       f"Number of {job}s", "Wage rate", pname="equilibrium wage rate", qname="number employed", plab="We", qlab="Qe",
                       cname=("demand for labour" if cv == "D" else "supply of labour"))


XEVENTS = [("Foreign demand for exports from {nation} rises.", "D", 1), ("Tourism to {nation} increases strongly.", "D", 1),
           ("The central bank of {nation} raises interest rates, attracting savings from abroad.", "D", 1),
           ("Foreign firms reduce their investment in {nation}.", "D", -1),
           ("Consumers in {nation} buy more imported goods.", "S", 1), ("Firms based in {nation} increase their investment abroad.", "S", 1),
           ("Exports from {nation} fall because of a recession in its main trading partners.", "D", -1),
           ("Households in {nation} take more holidays abroad.", "S", 1)]


def exchange_draw(r, c):
    ev, cv, d = r.choice(XEVENTS)
    cur = f"the {c['nation']} currency"
    other = r.choice(["euros", "pounds", "yen"])
    out = sd_question(ev.format(nation=c["nation"]), cv, d, f"foreign exchange market for {cur}", f"Quantity of {c['nation']} currency",
                      f"Price in {other}", pname="exchange rate", qname="quantity traded", plab="ERe", qlab="Qe",
                      cname=("demand for the currency" if cv == "D" else "supply of the currency"))
    up = (cv == "D" and d > 0) or (cv == "S" and d < 0)
    out["rows"][1] = (f"New exchange rate identified and labelled, {'higher than ERe (appreciation)' if up else 'lower than ERe (depreciation)'}", None)
    return out


TPRODS = ["steel", "cars", "rice", "clothing", "sugar", "mobile phones", "furniture", "tyres"]
TEVENTS = [("The government of {nation} imposes a tariff on imported {prod}.", "S", -1, "imported"),
           ("{nation} removes its tariff on imported {prod} after joining a free trade area.", "S", 1, "imported"),
           ("The government of {nation} raises the tariff on imported {prod}.", "S", -1, "imported"),
           ("A campaign encourages consumers in {nation} to buy home-produced goods rather than imported {prod}.", "D", -1, "imported"),
           ("The government of {nation} subsidises domestic producers of {prod} to protect them from foreign competition.", "S", 1, "domestic")]


def protection_draw(r, c):
    prod = r.choice(TPRODS)
    ev, cv, d, kind = r.choice(TEVENTS)
    mk = f"market for imported {prod} in {c['nation']}" if kind == "imported" else f"market for {prod} produced in {c['nation']}"
    return sd_question(ev.format(nation=c["nation"], prod=prod), cv, d, mk, f"Quantity of {prod}", "Price")


# ------------------------------------------------------------ PPC, cycle, LRAC

PPC_PAIRS = [("Capital goods", "Consumer goods"), ("Food", "Manufactured goods"), ("Agricultural goods", "Services"), ("Wheat", "Cloth")]
PEVENTS = [("A large deposit of natural gas is discovered in {nation}.", "out"), ("Many skilled workers emigrate from {nation}.", "in"),
           ("A major earthquake destroys factories and roads in {nation}.", "in"), ("Firms in {nation} invest heavily in new machinery.", "out"),
           ("The government of {nation} improves the quality of education and training.", "out"),
           ("New technology increases productivity in the production of {x} only.", "pivot-out"),
           ("A long drought reduces the amount of {x} that can be produced, but not the amount of {y}.", "pivot-in"),
           ("Large-scale immigration of working-age people increases the labour force of {nation}.", "out")]


def ppc_draw(r, c):
    if r.random() < 0.25:
        xg, yg = r.choice(PPC_PAIRS)
        names = r.sample(["A", "B", "C", "X", "Y", "Z"], 3)
        svg = G.ppc_base(xg, yg, points=[(names[0], "on:0.45"), (names[1], "in"), (names[2], "out")])
        text = (f"Figure 1 shows the production possibility curve (PPC) for {c['nation']}.\n\nUsing the points in Figure 1, identify the point that shows: "
                f"(i) an efficient use of resources; (ii) unemployed or inefficiently used resources; (iii) a combination that cannot be produced with current resources.")
        rows = [(f"(i) point {names[0]}", None), (f"(ii) point {names[1]}", None), (f"(iii) point {names[2]}", None)]
        return dict(text=text, svg=svg, rows=rows, diff="1-3")
    xg, yg = r.choice(PPC_PAIRS)
    ev, kind = r.choice(PEVENTS)
    ev = ev.format(nation=c["nation"], x=xg.lower(), y=yg.lower())
    text = (f"{ev}\n\nFigure 1 shows the production possibility curve (PPC) for {c['nation']}. On Figure 1, draw the likely effect of this "
            f"change on the PPC. Label the new curve PPC1.")
    if kind in ("out", "in"):
        rows = [(f"New PPC drawn {'outside' if kind == 'out' else 'inside'} the original curve", None),
                ("New curve labelled PPC1", None),
                ("Both intercepts move, showing a change in the capacity to produce both goods", None)]
    else:
        rows = [(f"New PPC drawn {'outside' if kind == 'pivot-out' else 'inside'} the original curve", None),
                ("New curve labelled PPC1", None),
                (f"Only the intercept on the {xg.lower()} axis moves; the {yg.lower()} intercept stays the same", None)]
    return dict(text=text, svg=G.ppc_base(xg, yg), rows=rows, diff="4-6")


def cycle_draw(r, c):
    given = r.choice(G.CYCLE)
    order = G.CYCLE
    text = (f"Figure 1 shows the economic cycle for {c['nation']}. One stage of the cycle, {given.lower()}, has been labelled.\n\n"
            f"Label the other three stages of the economic cycle in the empty boxes on Figure 1.")
    rows = [(f"{st} correctly placed", None) for st in order if st != given]
    return dict(text=text, svg=G.cycle_base(given), rows=rows, diff="1-3")


def growth_draw(r, c):
    if r.random() < 0.5:
        return cycle_draw(r, c)
    xg, yg = r.choice(PPC_PAIRS)
    ev = r.choice(["Investment in new infrastructure and technology leads to economic growth in {nation}.",
                   "{nation} experiences long-term economic growth as its labour force grows and becomes more skilled.",
                   "A natural disaster destroys a large share of the capital stock of {nation}."]).format(nation=c["nation"])
    kind = "in" if "disaster" in ev else "out"
    text = (f"{ev}\n\nFigure 1 shows the production possibility curve (PPC) for {c['nation']}. On Figure 1, draw the likely effect on the PPC. Label the new curve PPC1.")
    rows = [(f"New PPC drawn {'outside' if kind == 'out' else 'inside'} the original curve", None), ("New curve labelled PPC1", None),
            ("Both intercepts move, showing a change in the productive capacity of the economy", None)]
    return dict(text=text, svg=G.ppc_base(xg, yg), rows=rows, diff="4-6")


def scale_draw(r, c):
    if r.random() < 0.5:
        text = (f"Figure 1 shows the long-run average cost (LRAC) curve for {c['firm']}.\n\nOn Figure 1, label the output where average cost is lowest, "
                f"the range of output over which {c['firm']} benefits from economies of scale and the range over which it suffers diseconomies of scale.")
        rows = [("Lowest point of LRAC / optimum output identified (e.g. Q1)", None),
                ("Economies of scale shown as the falling section of LRAC, to the left of Q1", None),
                ("Diseconomies of scale shown as the rising section of LRAC, to the right of Q1", None)]
        return dict(text=text, svg=G.lrac_base(), rows=rows, diff="4-6")
    text = (f"{c['firm']} is growing quickly and its managers want to understand how its average costs will change as output rises.\n\n"
            f"On the axes in Figure 1, draw a long-run average cost (LRAC) curve for {c['firm']}. Label the areas of economies of scale and diseconomies of scale.")
    rows = [("U-shaped LRAC curve drawn and labelled", None), ("Economies of scale labelled on the falling section", None),
            ("Diseconomies of scale labelled on the rising section", None)]
    return dict(text=text, svg=G.blank_axes("Output", "Average cost"), rows=rows, diff="4-6")


DIAG = {"ppc": ppc_draw, "demand": demand_events, "supply": supply_events, "price": price_events, "ped": ped_draw, "pes": pes_draw,
        "intervention": intervention_draw, "externalities": ext_draw, "scale": scale_draw, "labour": labour_draw, "growth": growth_draw,
        "protection": protection_draw, "exchange": exchange_draw}


PEV = [("The government of {n} fines producers of {p} heavily whenever their waste exceeds a legal limit, so many firms install costly cleaning equipment.", "S", -1),
       ("Producers of {p} in {n} must now buy a permit for every tonne of carbon they emit.", "S", -1),
       ("New legislation in {n} requires all producers of {p} to use cleaner but more expensive production methods.", "S", -1),
       ("The government of {n} introduces an environmental tax on each unit of {p} produced.", "S", -1),
       ("The government of {n} gives producers of {g} a grant for each unit sold because of the external benefits.", "S", 1),
       ("The government of {n} cuts the cost of making {g} by paying part of producers' energy bills.", "S", 1)]


def intervention_pol_draw(r, c):
    ev, cv, d = r.choice(PEV)
    p, g = r.choice(["cement", "steel", "paper", "plastic packaging", "fertiliser"]), r.choice(GOODS)
    prod = g if "{g}" in ev else p
    return sd_question(ev.format(n=c["nation"], p=p, g=g), cv, d, f"market for {prod} in {c['nation']}", f"Quantity of {prod}", "Price")


DIAG["intervention-pol"] = intervention_pol_draw
