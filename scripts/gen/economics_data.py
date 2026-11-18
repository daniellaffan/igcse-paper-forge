"""Part (a) calculations for the data-response (Question 4 style) templates.

Each subtopic key maps to one generator per issue (same order as KB[key]["issues"]). A generator receives the
context *after* Extract A was filled, so the product, place and figures it uses are the ones printed in the
extract, and any figure stated in the extract (a rate, a percentage rise, a price) is the one the calculation
reproduces. Same return shape as economics_calc generators: dict(text, working, answer, values, table?, diff).
"""
from fractions import Fraction as F
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import fmt_num  # noqa: E402
from economics_calc import T, ADV, d2, money, pct  # noqa: E402

USD = "US\\$"

# rough size of one unit of each real-city currency relative to £/€ (for plausible prices, rents and wages)
_SCALE = {"RM": 5, "AED ": 4, "QR ": 4, "OMR ": F(1, 2), "JD ": 1}


def sc(c, lo, hi, step, r):
    """A random amount in [lo, hi] (in £/€ terms) rescaled to the context currency, a multiple of step."""
    k = _SCALE.get(c["ccy"], 1)
    v = F(r.randrange(lo, hi + 1, step)) * k
    return int(max(step, (v // step) * step))


def fnum(x):
    t = fmt_num(float(x))
    whole, dot, frac = t.lstrip("-").partition(".")
    return ("-" if t.startswith("-") else "") + f"{int(whole):,}" + dot + frac


def pct_change(a, b):
    return F(b - a, 1) / a * 100


# ---------------------------------------------------------------- ped
def ped_bus(r, c):
    p = int(c["p"])
    q1 = r.randrange(20, 90) * 1000
    if r.random() < 0.5:
        e = F(r.randrange(2, 9), 10)
        q2 = int(q1 * (1 - e * p / 100) // 10 * 10)
        dq = pct_change(q1, q2)
        v = dq / p
        return dict(text=f"After the {p}% fare rise in Extract A, {c['firm']} expects the number of passenger journeys each week to fall from {q1:,} to {q2:,}. "
                         f"Calculate, to two decimal places, the price elasticity of demand (PED) for {c['firm']}'s bus journeys." + ADV,
                    working=f"%Δ Qd = ({q2:,} - {q1:,}) ÷ {q1:,} × 100 = {d2(dq)}%; PED = {d2(dq)} ÷ {p}", answer=d2(v), values={"ped": float(v)}, diff="7-9")
    e = F(r.randrange(2, 9), 10)
    return dict(text=f"{c['firm']} estimates that the PED for its bus journeys is -{fnum(e)}. Using Extract A, calculate the expected percentage change in the "
                     f"number of passenger journeys after the {p}% fare rise." + ADV,
                working=f"-{fnum(e)} × {p}%", answer=f"-{fnum(e * p)}% (a fall of {fnum(e * p)}%)", values={"pct_change_qd": float(-e * p)}, diff="4-6")


def ped_tax(r, c):
    p, e, prod = int(c["p"]), F(c["e"]), c["prod"]
    if r.random() < 0.5:
        return dict(text=f"Using the information in Extract A, calculate the expected percentage change in the quantity of {prod} demanded if the tax raises "
                         f"the price by {p}%." + ADV,
                    working=f"-{fnum(e)} × {p}%", answer=f"-{fnum(e * p)}% (a fall of {fnum(e * p)}%)", values={"pct_change_qd": float(-e * p)}, diff="4-6")
    q = r.randrange(20, 200) * 10
    q2 = F(q) * (1 - e * p / 100)
    unit = {"sugary drinks": "million cans", "cigarettes": "million packs", "alcohol": "million litres"}[prod]
    return dict(text=f"Consumers in {c['nation']} buy {q:,} {unit} of {prod} a year. Using the information in Extract A, calculate the quantity bought each year "
                     f"after the tax raises the price by {p}%." + ADV,
                working=f"%Δ Qd = -{fnum(e)} × {p} = -{fnum(e * p)}%; {q:,} × (1 - {fnum(e * p / 100)})", answer=f"{fnum(q2)} {unit}",
                values={"quantity": float(q2)}, diff="4-6")


def ped_brand(r, c):
    kind = c["kind"]
    item = {"chocolate": "chocolate bar", "snack": "bag of snacks", "soft drink": "bottle of soft drink"}[kind]
    p1 = F(r.randrange(15, 40), 10) * _SCALE.get(c["ccy"], 1)
    p2 = p1 - F(r.randrange(1, 5), 10) * _SCALE.get(c["ccy"], 1)
    q1 = r.randrange(20, 90) * 1000
    q2 = q1 + r.randrange(2, 30) * 1000
    dq, dp = pct_change(q1, q2), (p2 - p1) / p1 * 100
    v = dq / dp
    return dict(text=f"{c['firm']} cut the price of its premium {item} from {money(c['ccy'], p1)} to {money(c['ccy'], p2)}. Weekly sales rose from {q1:,} to {q2:,}. "
                     f"Calculate, to two decimal places, the price elasticity of demand (PED) for the premium {item}." + ADV,
                working=f"%Δ Qd = ({q2:,} - {q1:,}) ÷ {q1:,} × 100 = {d2(dq)}%; %Δ P = ({d2(p2)} - {d2(p1)}) ÷ {d2(p1)} × 100 = {d2(dp)}%; {d2(dq)} ÷ {d2(dp)}",
                answer=d2(v), values={"ped": float(v)}, diff="7-9")


# ---------------------------------------------------------------- price
COMMODITY = {"cocoa": (2000, 3500), "coffee": (3000, 5000), "olive oil": (4000, 6500)}


def price_commodity(r, c):
    prod, p = c["prod"], int(c["p"])
    lo, hi = COMMODITY[prod]
    m = r.randrange(lo // 100, hi // 100)
    a = m * 100
    cnow = m * (100 + p)                       # two-year rise is exactly p%
    mid = a + r.randrange(1, max(2, (cnow - a) // 50)) * 50 if cnow - a > 100 else a + 50
    tab = T("Figure 1", ["Year", f"World price of {prod} ({USD} per tonne)"], [["Two years ago", f"{a:,}"], ["Last year", f"{mid:,}"], ["This year", f"{cnow:,}"]])
    if r.random() < 0.5:
        ch = pct_change(mid, cnow)
        return dict(text=f"Figure 1 shows the world price of {prod}. Calculate, to two decimal places, the percentage change in the price of {prod} between last year and this year." + ADV,
                    table=tab, working=f"({cnow:,} - {mid:,}) ÷ {mid:,} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")
    ch = pct_change(a, mid)
    return dict(text=f"Figure 1 shows the world price of {prod}. Calculate, to two decimal places, the percentage change in the price of {prod} between two years ago and last year." + ADV,
                table=tab, working=f"({mid:,} - {a:,}) ÷ {a:,} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")


def price_rent(r, c):
    rr = int(c["r"])
    r1 = sc(c, 700, 1800, 100, r)
    r2 = F(r1 * (100 + rr), 100)
    tab = T("Figure 1", ["", f"Average monthly rent for a flat in {c['city']} ({c['ccy'].strip()})"], [["Last year", f"{r1:,}"], ["This year", fnum(r2)]])
    inc = (r2 - r1) * 12
    return dict(text=f"Figure 1 shows the average monthly rent for a flat in {c['city']}. Calculate how much more a tenant paying the average rent will pay over a full year "
                     f"at this year's rent compared with last year's." + ADV,
                table=tab, working=f"({fnum(r2)} - {r1:,}) × 12", answer=money(c["ccy"], inc), values={"annual_increase": float(inc)}, diff="4-6")


def price_launch(r, c):
    prod, pr = c["prod"], int(c["pr"])
    step = max(10, (pr // 5) // 10 * 10)
    prices = [pr + i * step for i in range(5)]
    e = r.randrange(2, 5)                      # equilibrium above the launch price (shortage at launch)
    qe = r.randrange(20, 80) * 100
    sd, ss = r.randrange(5, 20) * 100, r.randrange(1, max(2, min(12, (qe - 500) // (e * 100)))) * 100
    qd = [qe + (e - i) * sd for i in range(5)]
    qs = [qe - (e - i) * ss for i in range(5)]
    tab = T("Figure 1", [f"Price of the {prod} ({c['ccy'].strip()})", "Quantity demanded per week", "Quantity supplied per week"],
            [[f"{p_:,}", f"{a:,}", f"{b:,}"] for p_, a, b in zip(prices, qd, qs)])
    if r.random() < 0.5:
        gap = qd[0] - qs[0]
        return dict(text=f"Figure 1 shows the weekly demand and supply schedules for {c['firm']}'s {prod}. Calculate the size of the shortage (excess demand) at the "
                         f"launch price of {c['ccy']}{pr}." + ADV,
                    table=tab, working=f"{qd[0]:,} - {qs[0]:,}", answer=f"excess demand of {gap:,} units", values={"gap": gap}, diff="4-6")
    return dict(text=f"Figure 1 shows the weekly demand and supply schedules for {c['firm']}'s {prod}. Identify the equilibrium price and calculate the total revenue "
                     f"that would be received each week at that price." + ADV,
                table=tab, working=f"Equilibrium where Qd = Qs: price {c['ccy']}{prices[e]:,}, quantity {qe:,}; {prices[e]:,} × {qe:,}",
                answer=money(c["ccy"], prices[e] * qe), values={"pe": prices[e], "qe": qe, "tr": prices[e] * qe}, diff="4-6")


# ---------------------------------------------------------------- unemployment
def unemp_struct(r, c):
    u, v = F(c["u"]), int(c["v"]) * 1000
    lo = int(v * 100 / u * F(3, 2)) // 100000 + 1        # unemployed clearly outnumber the vacancies in Extract A
    lf = r.randrange(max(40, lo), max(41, lo * 3)) * 100000
    un = lf * u / 100
    if r.random() < 0.5:
        return dict(text=f"{c['nation']} has a labour force of {lf:,}. Using the unemployment rate in Extract A, calculate the number of people who are unemployed." + ADV,
                    working=f"{fnum(u)} ÷ 100 × {lf:,}", answer=f"{int(un):,} people", values={"unemployed": float(un)}, diff="1-3")
    ratio = un / v
    return dict(text=f"{c['nation']} has a labour force of {lf:,}. Using Extract A, calculate, to two decimal places, the number of unemployed people for each job vacancy." + ADV,
                working=f"Unemployed = {fnum(u)}% × {lf:,} = {int(un):,}; {int(un):,} ÷ {v:,}", answer=d2(ratio), values={"per_vacancy": float(ratio)}, diff="4-6")


def unemp_recession(r, c):
    u1, u2 = F(c["u1"]), F(c["u2"])
    lf = r.randrange(40, 400) * 100000
    if r.random() < 0.5:
        inc = lf * (u2 - u1) / 100
        return dict(text=f"The labour force of {c['nation']} is {lf:,} and did not change during the year. Using Extract A, calculate the increase in the number of people unemployed." + ADV,
                    working=f"({fnum(u2)} - {fnum(u1)}) ÷ 100 × {lf:,}", answer=f"{int(inc):,} people", values={"increase": float(inc)}, diff="4-6")
    un = lf * u2 / 100
    return dict(text=f"The labour force of {c['nation']} is {lf:,}. Using Extract A, calculate the number of people unemployed at the end of the year." + ADV,
                working=f"{fnum(u2)} ÷ 100 × {lf:,}", answer=f"{int(un):,} people", values={"unemployed": float(un)}, diff="1-3")


# ---------------------------------------------------------------- inflation
def infl_basket(r, c, i):
    b = r.randrange(4, 30) * 10
    n = F(b) * (100 + i) / 100
    return dict(text=f"A typical basket of goods in {c['nation']} cost {money(c['ncy'], b)} at the start of last year and {money(c['ncy'], n)} at the end of it. "
                     f"Calculate, to one decimal place, the rate of inflation shown by the basket." + ADV,
                working=f"({d2(n)} - {b}) ÷ {b} × 100", answer=f"{fnum(i)}%", values={"inflation": float(i)}, diff="4-6")


def infl_cpi(r, c, i):
    i1 = F(r.randrange(1000, 1400), 10)
    i2 = i1 * (100 + i) / 100
    return dict(text=f"The consumer price index (CPI) for {c['nation']} was {fnum(i1)} at the start of last year. Using the inflation rate in Extract A, calculate, to two "
                     f"decimal places, the CPI at the end of the year." + ADV,
                working=f"{fnum(i1)} × (1 + {fnum(i)} ÷ 100)", answer=d2(i2), values={"cpi": float(i2)}, diff="4-6")


def infl_high(r, c):
    i = F(c["i"])
    return (infl_basket if r.random() < 0.5 else infl_cpi)(r, c, i)


def infl_rates(r, c):
    i, rt = F(c["i"]), F(c["r"])
    if r.random() < 0.5:
        loan = r.randrange(50, 300, 10) * 1000
        interest = F(loan) * rt / 100
        return dict(text=f"A family in {c['nation']} has a loan of {money(c['ncy'], loan)}. Using the interest rate in Extract A, calculate the interest they will pay in one year." + ADV,
                    working=f"{loan:,} × {fnum(rt)} ÷ 100", answer=money(c["ncy"], interest), values={"interest": float(interest)}, diff="1-3")
    return infl_basket(r, c, i)


def infl_deflation(r, c):
    i1 = F(r.randrange(1050, 1300), 10)
    i2 = i1 - F(r.randrange(5, 30), 10)
    i3 = i2 - F(r.randrange(5, 30), 10)
    tab = T("Figure 1", ["", f"Consumer price index (CPI) for {c['nation']}"], [["A year ago", fnum(i1)], ["Six months ago", fnum(i2)], ["This month", fnum(i3)]])
    ch = (i3 - i1) / i1 * 100
    return dict(text=f"Figure 1 shows the consumer price index for {c['nation']}. Calculate, to two decimal places, the percentage change in the price level over the last year." + ADV,
                table=tab, working=f"({fnum(i3)} - {fnum(i1)}) ÷ {fnum(i1)} × 100", answer=pct(ch), values={"inflation": float(ch)}, diff="4-6")


# ---------------------------------------------------------------- costs
def costs_fuel(r, c):
    f, biz = int(c["f"]), c["biz"]
    fuel = sc(c, 20, 150, 1, r) * 100
    new = F(fuel) * (100 + f) / 100
    if r.random() < 0.5:
        return dict(text=f"Before the rise described in Extract A, {c['firm']} spent {money(c['ccy'], fuel)} a month on fuel. Calculate its monthly fuel cost after the {f}% rise." + ADV,
                    working=f"{fuel:,} × (1 + {f} ÷ 100)", answer=money(c["ccy"], new), values={"fuel": float(new)}, diff="1-3")
    wages = sc(c, 30, 200, 1, r) * 100
    other = sc(c, 5, 60, 1, r) * 100
    tab = T("Figure 1", ["Monthly cost", f"Before the fuel price rise ({c['ccy'].strip()})"], [["Fuel", f"{fuel:,}"], ["Drivers' wages", f"{wages:,}"], ["Other costs", f"{other:,}"]])
    tot = new + wages + other
    return dict(text=f"Figure 1 shows the monthly costs of {c['firm']}, a {biz}, before fuel costs rose. Using Extract A, calculate the firm's total monthly costs after the {f}% "
                     f"rise in fuel costs, assuming its other costs do not change." + ADV,
                table=tab, working=f"Fuel = {fuel:,} × {fnum(F(100 + f, 100))} = {fnum(new)}; {fnum(new)} + {wages:,} + {other:,}", answer=money(c["ccy"], tot),
                values={"total": float(tot)}, diff="4-6")


def costs_machine(r, c):
    fc = int(c["fc"]) * 1000
    biz = c["biz"]
    unit, vlo, vhi = {"bakery": ("loaves", 4, 15), "restaurant": ("meals", 30, 90), "printing shop": ("print orders", 20, 80)}[biz]
    k = _SCALE.get(c["ccy"], 1)
    vc = F(r.randrange(vlo, vhi), 10) * k if biz == "bakery" else F(r.randrange(vlo, vhi), 10) * k
    q = r.randrange(5, 40) * 100 if biz == "bakery" else r.randrange(5, 30) * 50
    tc = fc + vc * q
    if r.random() < 0.5:
        return dict(text=f"{c['name']}'s variable cost is {money(c['ccy'], vc)} per unit and the business sells {q:,} {unit} a month. Using the fixed costs in Extract A, "
                         f"calculate the total monthly costs of the business." + ADV,
                    working=f"{fc:,} + ({d2(vc)} × {q:,})", answer=money(c["ccy"], tc), values={"tc": float(tc)}, diff="4-6")
    ac = tc / q
    return dict(text=f"{c['name']}'s variable cost is {money(c['ccy'], vc)} per unit and the business sells {q:,} {unit} a month. Using the fixed costs in Extract A, "
                     f"calculate, to two decimal places, the average cost per unit." + ADV,
                working=f"TC = {fc:,} + ({d2(vc)} × {q:,}) = {fnum(tc)}; {fnum(tc)} ÷ {q:,}", answer=money(c["ccy"], ac), values={"ac": float(ac)}, diff="7-9")


def costs_profit(r, c):
    tr = int(c["tr"])
    tr1 = sc(c, 20, 90, 1, r) * 10000
    tr2 = F(tr1) * (100 + tr) / 100
    p1 = F(tr1) * r.randrange(8, 20) / 100
    tc1 = tr1 - p1
    p2 = p1 - F(tr1) * r.randrange(1, 6) / 100
    tc2 = tr2 - p2
    tab = T("Figure 1", ["", f"Last year ({c['ccy'].strip()})", f"This year ({c['ccy'].strip()})"], [["Total revenue", fnum(tr1), fnum(tr2)], ["Total costs", fnum(tc1), fnum(tc2)]])
    ch = (p2 - p1) / p1 * 100
    return dict(text=f"Figure 1 shows the total revenue and total costs of {c['firm']}. Calculate, to two decimal places, the percentage change in {c['firm']}'s profit." + ADV,
                table=tab, working=f"Profit last year = {fnum(tr1)} - {fnum(tc1)} = {fnum(p1)}; this year = {fnum(tr2)} - {fnum(tc2)} = {fnum(p2)}; ({fnum(p2)} - {fnum(p1)}) ÷ {fnum(p1)} × 100",
                answer=pct(ch), values={"pct_change_profit": float(ch)}, diff="7-9")


# ---------------------------------------------------------------- labour
def lab_mw(r, c):
    w, h = F(c["mw"]), r.randrange(20, 45)
    if r.random() < 0.6:
        return dict(text=f"Using Extract A, calculate the lowest weekly wage a worker in {c['nation']} can now earn for a {h}-hour week." + ADV,
                    working=f"{d2(w)} × {h}", answer=money(c["ncy"], w * h), values={"weekly": float(w * h)}, diff="1-3")
    cut = r.randrange(2, 8)
    old, new = w * h, w * (h - cut)
    return dict(text=f"Before the increase, a café worker in {c['nation']} worked {h} hours a week. Their employer has now cut their hours by {cut} a week. Using the new minimum "
                     f"wage in Extract A, calculate the worker's new weekly pay." + ADV,
                working=f"{d2(w)} × ({h} - {cut})", answer=money(c["ncy"], new), values={"weekly": float(new)}, diff="4-6")


def lab_nurses(r, c):
    p = int(c["p"])
    s = r.randrange(250, 500) * 100
    new = F(s) * (100 + p) / 100
    return dict(text=f"A nurse in {c['nation']} earns {money(c['ncy'], s)} a year. Calculate the nurse's annual salary if the {p}% pay rise in Extract A is agreed." + ADV,
                working=f"{s:,} × (1 + {p} ÷ 100)", answer=money(c["ncy"], new), values={"salary": float(new)}, diff="1-3")


def lab_engineers(r, c):
    a = int(c["a"])
    w = F(r.randrange(100, 160), 10) * _SCALE.get(c["ccy"], 1)
    h = r.randrange(35, 41)
    wk = w * h
    return dict(text=f"A shop assistant in {c['city']} earns {money(c['ccy'], w)} an hour and works {h} hours a week. Using Extract A, calculate the average weekly earnings of a software engineer in {c['city']}." + ADV,
                working=f"{d2(w)} × {h} = {d2(wk)}; {d2(wk)} × {a}", answer=money(c["ccy"], wk * a), values={"weekly": float(wk * a)}, diff="4-6")


# ---------------------------------------------------------------- protection
def prot_quota(r, c):
    prod = c["prod"]
    qty = (lambda n: f"{n:,} tyres") if prod == "tyres" else (lambda n: f"{n:,} tonnes of {prod}")
    before = r.randrange(50, 400) * 1000
    after = before - r.randrange(10, before // 2000) * 1000
    ch = pct_change(before, after)
    return dict(text=f"Before the quota, {c['nation']} imported {qty(before)} a year. The quota limits imports to {qty(after)} a year. "
                     f"Calculate, to two decimal places, the percentage change in imports of {prod}." + ADV,
                working=f"({after:,} - {before:,}) ÷ {before:,} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")


def prot_fta(r, c):
    t = r.randrange(5, 20)
    ex = r.randrange(5, 90) * 100000
    saving = F(ex) * t / 100
    return dict(text=f"Before {c['nation']} joined the free trade area, a firm exporting to member countries paid a {t}% tariff on its exports. The firm sells "
                     f"{money(c['ncy'], ex)} of goods a year to these countries. Calculate how much the firm saves in tariffs each year now that {c['nation']} is a member." + ADV,
                working=f"{ex:,} × {t} ÷ 100", answer=money(c["ncy"], saving), values={"saving": float(saving)}, diff="1-3")


TARIFF_GOODS = {"steel": ("one tonne of imported steel", 500, 1000, 10), "solar panels": ("one imported solar panel", 120, 400, 5), "cars": ("one imported car", 15000, 40000, 500)}


def prot_tariff(r, c):
    t, prod = int(c["t"]), c["prod"]
    what, lo, hi, step = TARIFF_GOODS[prod]
    p = r.randrange(lo, hi, step)
    new = F(p) * (100 + t) / 100
    return dict(text=f"Before the tariff in Extract A, {what} sold for {money(c['ncy'], p)} in {c['nation']}. Calculate its new price, assuming the whole tariff is passed on to buyers." + ADV,
                working=f"{p:,} × (1 + {t} ÷ 100)", answer=money(c["ncy"], new), values={"price": float(new)}, diff="1-3")


# ---------------------------------------------------------------- exchange
def ex_dep(r, c):
    d = int(c["d"])
    x = F(r.randrange(40, 200), 100)
    x2 = x * (100 - d) / 100
    p = r.randrange(10, 90) * 100
    if r.random() < 0.5:
        return dict(text=f"Before the depreciation in Extract A, the exchange rate was {c['ncy']}1 = {USD}{d2(x)}. Calculate, to four decimal places, the new exchange rate." + ADV,
                    working=f"{d2(x)} × (1 - {d} ÷ 100)", answer=f"{c['ncy']}1 = {USD}{fmt_num(float(x2), dp=4)}", values={"rate": float(x2)}, diff="4-6")
    return dict(text=f"Before the depreciation in Extract A, the exchange rate was {c['ncy']}1 = {USD}{d2(x)}. A product exported from {c['nation']} costs {money(c['ncy'], p)}. "
                     f"Calculate, to two decimal places, its price in US dollars after the depreciation." + ADV,
                working=f"New rate = {d2(x)} × (1 - {d} ÷ 100) = {fmt_num(float(x2), dp=4)}; {p:,} × {fmt_num(float(x2), dp=4)}", answer=f"{USD}{float(p * x2):,.2f}",
                values={"usd_price": float(p * x2)}, diff="4-6")


def ex_app(r, c):
    a = int(c["a"])
    x = F(r.randrange(40, 200), 100)
    x2 = x * (100 + a) / 100
    h = r.randrange(8, 40) * 100
    cost1, cost2 = F(h) / x, F(h) / x2
    return dict(text=f"Before the appreciation in Extract A, the exchange rate was {c['ncy']}1 = {USD}{d2(x)}. A family in {c['nation']} plans a holiday in the USA costing {USD}{h:,}. "
                     f"Calculate, to two decimal places, how much less the holiday now costs the family in {c['ncy']}." + ADV,
                working=f"Before: {h:,} ÷ {d2(x)} = {d2(cost1)}; new rate = {d2(x)} × {fnum(F(100 + a, 100))} = {fmt_num(float(x2), dp=4)}; after: {h:,} ÷ {fmt_num(float(x2), dp=4)} = {d2(cost2)}; {d2(cost1)} - {d2(cost2)}",
                answer=money(c["ncy"], F(d2(cost1)) - F(d2(cost2))), values={"saving": float(F(d2(cost1)) - F(d2(cost2)))}, diff="7-9")


def ex_vol(r, c):
    v = int(c["v"])
    x1 = F(r.randrange(80, 250), 100)
    lim = int(x1 * v)                           # change of at most v% (in hundredths)
    x2 = x1 + r.choice([-1, 1]) * F(r.randrange(1, max(2, lim)), 100)
    ch = (x2 - x1) / x1 * 100
    return dict(text=f"In one month the exchange rate changed from {c['ncy']}1 = {USD}{d2(x1)} to {c['ncy']}1 = {USD}{d2(x2)}. Calculate, to two decimal places, the percentage change in the value of {c['nation']}'s currency." + ADV,
                working=f"({d2(x2)} - {d2(x1)}) ÷ {d2(x1)} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")


# ---------------------------------------------------------------- growth
def gr_fast(r, c):
    g = F(c["g"])
    g1 = r.randrange(2, 20) * 100
    g2 = g1 * (100 + g) / 100
    if r.random() < 0.5:
        tab = T("Figure 1", ["", f"Real GDP of {c['nation']} ({c['ncy']}bn)"], [["Two years ago", f"{g1:,}"], ["Last year", fnum(g2)]])
        return dict(text=f"Figure 1 shows the real GDP of {c['nation']}. Calculate, to one decimal place, the rate of economic growth last year." + ADV,
                    table=tab, working=f"({fnum(g2)} - {g1:,}) ÷ {g1:,} × 100", answer=f"{fnum(g)}%", values={"growth": float(g)}, diff="4-6")
    pop = r.randrange(5, 90)
    pc = g2 * 1000 / pop
    return dict(text=f"Real GDP in {c['nation']} was {c['ncy']}{g1:,}bn two years ago. Using the growth rate in Extract A and a population of {pop} million, calculate, to two decimal places, "
                     f"real GDP per capita last year." + ADV,
                working=f"GDP = {g1:,} × {fnum(F(100) + g)} ÷ 100 = {fnum(g2)}bn; ({fnum(g2)} × 1,000,000,000) ÷ ({pop} × 1,000,000)", answer=f"{c['ncy']}{float(pc):,.2f}",
                values={"gdp_per_capita": float(pc)}, diff="7-9")


def gr_recession(r, c):
    f = F(c["f"])
    q2 = r.randrange(2, 20) * 250
    q1 = q2 + r.randrange(2, 12) * 2
    q3 = q2 * (100 - f) / 100
    tab = T("Figure 1", ["Quarter", f"Real GDP of {c['nation']} ({c['ncy']}bn)"], [["Quarter 1", f"{q1:,}"], ["Quarter 2", f"{q2:,}"], ["Quarter 3 (last quarter)", fnum(q3)]])
    ch = pct_change(q1, q2)
    return dict(text=f"Figure 1 shows the real GDP of {c['nation']} in the last three quarters. Calculate, to two decimal places, the percentage change in real GDP between quarter 1 and quarter 2." + ADV,
                table=tab, working=f"({q2:,} - {q1:,}) ÷ {q1:,} × 100", answer=pct(ch), values={"growth": float(ch)}, diff="4-6")


def gr_income(r, c):
    y = int(c["y"]) * 1000
    pop = r.randrange(5, 90)
    gdp = F(y) * pop / 1000
    return dict(text=f"{c['nation']} has a population of {pop} million. Using the average income per person in Extract A, calculate the total income (GDP) of {c['nation']} in {c['ncy']}bn." + ADV,
                working=f"{y:,} × {pop},000,000 = {y * pop:,},000,000", answer=f"{c['ncy']}{fnum(gdp)}bn", values={"gdp_bn": float(gdp)}, diff="4-6")


# ---------------------------------------------------------------- fiscal
def fis_deficit(r, c):
    d, n = F(c["d"]), int(c["n"])
    gdp = r.randrange(5, 200) * 10
    if r.random() < 0.5:
        dv = gdp * d / 100
        return dict(text=f"The GDP of {c['nation']} is {c['ncy']}{gdp:,}bn. Using Extract A, calculate the size of the budget deficit in {c['ncy']}bn." + ADV,
                    working=f"{fnum(d)} ÷ 100 × {gdp:,}", answer=f"{c['ncy']}{fnum(dv)}bn", values={"deficit_bn": float(dv)}, diff="1-3")
    nv = F(gdp * n, 100)
    return dict(text=f"The GDP of {c['nation']} is {c['ncy']}{gdp:,}bn. Using Extract A, calculate the national debt of {c['nation']} in {c['ncy']}bn." + ADV,
                working=f"{n} ÷ 100 × {gdp:,}", answer=f"{c['ncy']}{fnum(nv)}bn", values={"debt_bn": float(nv)}, diff="1-3")


def fis_subsidy(r, c):
    s = int(c["s"])
    jobs = r.randrange(20, 150) * 1000
    per = F(s) * 10 ** 9 / jobs
    return dict(text=f"The government of {c['nation']} expects the subsidies in Extract A to create {jobs:,} green jobs. Calculate, to the nearest whole number, the subsidy cost per job created." + ADV,
                working=f"{s:,},000,000,000 ÷ {jobs:,}", answer=f"{c['ncy']}{round(float(per)):,}", values={"per_job": float(per)}, diff="4-6")


def fis_taxes(r, c):
    inc, sal, bus = [F(r.randrange(50, 400), 10) for _ in range(3)]
    tab = T("Figure 1", ["Tax", f"Revenue ({c['ncy']}bn)"], [["Income tax", fnum(inc)], ["Sales tax", fnum(sal)], ["Business (corporation) tax", fnum(bus)]])
    share = (inc + bus) / (inc + sal + bus) * 100
    return dict(text=f"Figure 1 shows the main sources of tax revenue in {c['nation']}. Calculate, to two decimal places, the percentage of this revenue that comes from direct taxes." + ADV,
                table=tab, working=f"Direct taxes = {fnum(inc)} + {fnum(bus)} = {fnum(inc + bus)}; total = {fnum(inc + sal + bus)}; {fnum(inc + bus)} ÷ {fnum(inc + sal + bus)} × 100",
                answer=pct(share), values={"direct_share": float(share)}, diff="4-6")


# ---------------------------------------------------------------- externalities
def ext_bags(r, c):
    b1 = r.randrange(200, 900) * 10
    b2 = r.randrange(10, b1 // 50) * 10
    ch = pct_change(b1, b2)
    return dict(text=f"Before the ban, shops in {c['nation']} gave out about {b1:,} million plastic bags a year. Inspectors estimate that {b2:,} million are still given out illegally each year. "
                     f"Calculate, to two decimal places, the percentage change in the number of bags given out." + ADV,
                working=f"({b2:,} - {b1:,}) ÷ {b1:,} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")


def ext_plant(r, c):
    pc = sc(c, 100, 900, 1, r) * 1000
    ec = sc(c, 20, 300, 1, r) * 1000
    return dict(text=f"{c['firm']}'s chemical plant has private costs of {money(c['ccy'], pc)} a week. The external costs of its waste are estimated at {money(c['ccy'], ec)} a week. "
                     f"Calculate the social cost of the plant's production per week." + ADV,
                working=f"{pc:,} + {ec:,}", answer=money(c["ccy"], pc + ec), values={"social_cost": pc + ec}, diff="1-3")


def ext_vacc(r, c):
    v1, v2 = int(c["v1"]), int(c["v2"])
    n = r.randrange(50, 900) * 1000
    inc = F(n * (v2 - v1), 100)
    return dict(text=f"There are {n:,} children in {c['nation']} who are eligible for vaccination. Using Extract A, calculate how many more children are vaccinated now than five years ago, "
                     f"assuming the number of eligible children has not changed." + ADV,
                working=f"({v2} - {v1}) ÷ 100 × {n:,}", answer=f"{fnum(inc)} children", values={"extra": float(inc)}, diff="4-6")


DGEN = {"ped": [ped_bus, ped_tax, ped_brand], "price": [price_commodity, price_rent, price_launch],
        "unemployment": [unemp_struct, unemp_recession], "inflation": [infl_high, infl_rates, infl_deflation],
        "costs": [costs_fuel, costs_machine, costs_profit], "labour": [lab_mw, lab_nurses, lab_engineers],
        "protection": [prot_quota, prot_fta, prot_tariff], "exchange": [ex_dep, ex_app, ex_vol],
        "growth": [gr_fast, gr_recession, gr_income], "fiscal": [fis_deficit, fis_subsidy, fis_taxes],
        "externalities": [ext_bags, ext_plant, ext_vacc]}
