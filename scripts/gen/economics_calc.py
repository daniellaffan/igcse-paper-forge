"""Calculation question generators for economics. Every answer is computed here with exact arithmetic.

Each generator: f(r, c) -> dict(text, working, answer, values, intro?, table?, ao, diff, mcq?)
`c` is a context dict from economics_util.new_ctx. Money is written with c['ccy'] / c['ncy'].
"""
from fractions import Fraction as F
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import fmt_num  # noqa: E402


def d2(x):
    return fmt_num(float(x), dp=2)


def money(cur, x, dp=2):
    x = F(x)
    s = f"{float(x):,.{dp}f}" if (dp and x.denominator != 1) else f"{int(x):,}" if x.denominator == 1 else f"{float(x):,.2f}"
    return f"{cur}{s}"


def pct(x, dp=2):
    return f"{d2(x) if dp == 2 else fmt_num(float(x), dp=dp)}%"


def T(caption, headers, rows):
    return {"type": "table", "caption": caption, "headers": headers, "rows": [[str(v) for v in row] for row in rows]}


ADV = " Show your working."

# ---------------------------------------------------------------- Topic 1

PPC_GOODS = [("wheat", "cloth", "tonnes", "metres"), ("rice", "cars", "tonnes", "cars"), ("food", "clothing", "units", "units"),
             ("maize", "machinery", "tonnes", "machines"), ("fish", "furniture", "tonnes", "items"), ("coffee", "computers", "tonnes", "computers")]


def ppc_oc(r, c):
    g1, g2, u1, u2 = r.choice(PPC_GOODS)
    a1 = r.randrange(400, 900, 10); b1 = r.randrange(50, 200, 5)
    a2 = a1 - r.randrange(60, 250, 10); b2 = b1 + r.randrange(20, 120, 5)
    per = F(a1 - a2, b2 - b1)
    if r.random() < 0.5:
        return dict(text=f"Figure 1 shows two points on the production possibility curve of {c['nation']}. Calculate the opportunity cost of moving from point A to point B, in terms of {g1}." + ADV,
                    table=T("Figure 1", ["Point", f"{g1.capitalize()} ({u1})", f"{g2.capitalize()} ({u2})"], [["A", a1, b1], ["B", a2, b2]]),
                    working=f"{a1} - {a2}", answer=f"{a1 - a2} {u1} of {g1}", values={"opportunity_cost": a1 - a2}, diff="1-3")
    return dict(text=f"Figure 1 shows two points on the production possibility curve of {c['nation']}. Calculate, to two decimal places, the opportunity cost in {g1} of producing each extra unit of {g2} when moving from A to B." + ADV,
                table=T("Figure 1", ["Point", f"{g1.capitalize()} ({u1})", f"{g2.capitalize()} ({u2})"], [["A", a1, b1], ["B", a2, b2]]),
                working=f"({a1} - {a2}) ÷ ({b2} - {b1}) = {a1 - a2} ÷ {b2 - b1}", answer=f"{d2(per)} {u1} of {g1}", values={"oc_per_unit": float(per)}, diff="4-6")


PRODS = ["cinema tickets", "bottles of juice", "loaves of bread", "bus journeys", "phone cases", "bags of rice", "cups of coffee", "packs of batteries"]


def demand_calc(r, c):
    k = r.randrange(3)
    p = r.choice(PRODS)
    if k == 0:
        qs = [r.randrange(5, 60) for _ in range(3)]
        price = r.randrange(2, 9)
        names = [c["name"], c["name2"], "Ali"]
        return dict(text=f"Figure 1 shows the weekly demand for {p} of three consumers at a price of {c['ccy']}{price}. Assume they are the only consumers in the market. Calculate the market demand for {p} at this price." + ADV,
                    table=T("Figure 1", ["Consumer", f"Quantity demanded at {c['ccy']}{price}"], [[n, q] for n, q in zip(names, qs)]),
                    working=" + ".join(map(str, qs)), answer=f"{sum(qs)} {p}", values={"market_demand": sum(qs)}, diff="1-3")
    q1 = r.randrange(200, 2000, 10); q2 = q1 + r.choice([-1, 1]) * r.randrange(10, int(q1 * 0.4), 5)
    ch = F(q2 - q1, q1) * 100
    if k == 1:
        return dict(text=f"Weekly sales of {p} at a shop in {c['city']} changed from {q1:,} to {q2:,} after {'a nearby rival shop closed' if q2 > q1 else 'a new rival shop opened nearby'}. Calculate, to two decimal places, the percentage change in quantity demanded." + ADV,
                    working=f"({q2} - {q1}) ÷ {q1} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")
    inc = r.randrange(2, 9); ped = F(r.randrange(5, 25), 10)
    return dict(text=f"The price of {p} rises by {inc}% and the PED is -{d2(ped)[:-1] if d2(ped).endswith('0') else d2(ped)}. Calculate the percentage change in quantity demanded." + ADV,
                working=f"-{fmt_num(float(ped))} × {inc}%", answer=f"-{pct(ped * inc)} (a fall of {pct(ped * inc)})", values={"pct_change_qd": float(-ped * inc)}, diff="4-6")


def supply_calc(r, c):
    k = r.randrange(2)
    p = r.choice(["tonnes of rice", "bicycles", "solar panels", "tonnes of cocoa", "shirts", "chairs"])
    if k == 0:
        qs = [r.randrange(100, 900, 10) for _ in range(r.choice([3, 4]))]
        price = r.randrange(5, 40)
        firms = ["Firm A", "Firm B", "Firm C", "Firm D"][:len(qs)]
        return dict(text=f"Figure 1 shows the quantity of {p} each firm in a market is willing to supply per month at a price of {c['ccy']}{price}. Calculate the market supply at this price." + ADV,
                    table=T("Figure 1", ["Firm", f"Quantity supplied at {c['ccy']}{price}"], [[f, q] for f, q in zip(firms, qs)]),
                    working=" + ".join(map(str, qs)), answer=f"{sum(qs):,} {p}", values={"market_supply": sum(qs)}, diff="1-3")
    q1 = r.randrange(500, 5000, 50); q2 = q1 + r.randrange(25, int(q1 * 0.5), 25) * r.choice([1, -1])
    ch = F(q2 - q1, q1) * 100
    return dict(text=f"After a change in the market price, {c['firm']} changed its monthly output of {p} from {q1:,} to {q2:,}. Calculate, to two decimal places, the percentage change in quantity supplied." + ADV,
                working=f"({q2} - {q1}) ÷ {q1} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")


def price_calc(r, c):
    p = r.choice(["kilograms of tomatoes", "concert tickets", "litres of milk", "T-shirts", "bags of cement"])
    prices = sorted(r.sample(range(2, 20), 5))
    e = r.randrange(1, 4)  # index of equilibrium
    qe = r.randrange(300, 800, 10)
    step_d = r.randrange(30, 90, 10); step_s = r.randrange(30, 90, 10)
    qd = [qe + (e - i) * step_d for i in range(5)]
    qs = [qe - (e - i) * step_s for i in range(5)]
    i = r.choice([j for j in range(5) if j != e])
    gap = qd[i] - qs[i]
    kind = "excess demand" if gap > 0 else "excess supply"
    tab = T("Figure 1", [f"Price ({c['ccy'].strip()})", "Quantity demanded", "Quantity supplied"], [[pr, a, b] for pr, a, b in zip(prices, qd, qs)])
    if r.random() < 0.3:
        return dict(text=f"Figure 1 shows the weekly demand and supply schedules for {p} in {c['city']}. Identify the equilibrium price and calculate the total revenue received by sellers at that price." + ADV,
                    table=tab, working=f"Equilibrium where Qd = Qs: price {c['ccy']}{prices[e]}, quantity {qe}; {prices[e]} × {qe}",
                    answer=money(c["ccy"], prices[e] * qe), values={"pe": prices[e], "qe": qe, "tr": prices[e] * qe}, diff="4-6")
    return dict(text=f"Figure 1 shows the weekly demand and supply schedules for {p} in {c['city']}. Calculate the size of the excess demand or excess supply when the price is {c['ccy']}{prices[i]}." + ADV,
                table=tab, working=f"{qd[i]} - {qs[i]}" if gap > 0 else f"{qs[i]} - {qd[i]}", answer=f"{kind} of {abs(gap)} {p}",
                values={"gap": abs(gap), "kind": kind}, diff="4-6")


def ped_calc(r, c):
    k = r.randrange(5)
    p = r.choice(["coffee", "bus tickets", "trainers", "petrol", "chocolate bars", "smartphones", "cinema tickets"])
    if k == 0:
        dq = r.randrange(2, 40); dp = r.randrange(3, 25)
        v = F(-dq, dp) if True else 0
        return dict(text=f"The price of {p} rises by {dp}% and quantity demanded falls by {dq}%. Calculate, to two decimal places, the price elasticity of demand (PED) for {p}." + ADV,
                    working=f"-{dq}% ÷ {dp}%", answer=d2(v), values={"ped": float(v)}, diff="4-6")
    if k == 1:
        ped = F(r.randrange(2, 30), 10); dp = r.randrange(4, 20)
        fall = r.random() < 0.5
        res = ped * dp
        return dict(text=f"Calculate the percentage change in quantity demanded for {p} if the price elasticity of demand (PED) is -{fmt_num(float(ped))} and the price {'falls' if fall else 'rises'} by {dp}%." + ADV,
                    working=f"{'-' if fall else ''}{dp}% × -{fmt_num(float(ped))}", answer=f"{'+' if fall else '-'}{fmt_num(float(res))}% ({'a rise' if fall else 'a fall'})",
                    values={"pct_change_qd": float(res if fall else -res)}, diff="4-6")
    if k == 2:
        p1 = r.randrange(2, 20); p2 = p1 + r.choice([-1, 1]) * r.randrange(1, max(2, p1 // 2) + 1)
        q1 = r.randrange(200, 1000, 10); q2 = q1 - (1 if p2 > p1 else -1) * r.randrange(10, q1 // 2, 10)
        dq = F(q2 - q1, q1) * 100; dpp = F(p2 - p1, p1) * 100
        v = dq / dpp
        return dict(text=f"{c['firm']} changed the price of its {p} from {c['ccy']}{p1} to {c['ccy']}{p2}. As a result, weekly sales changed from {q1} to {q2}. Calculate, to two decimal places, the PED for {c['firm']}'s {p}." + ADV,
                    working=f"%Δ Qd = ({q2} - {q1}) ÷ {q1} × 100 = {d2(dq)}%; %Δ P = ({p2} - {p1}) ÷ {p1} × 100 = {d2(dpp)}%; {d2(dq)} ÷ {d2(dpp)}",
                    answer=d2(v), values={"ped": float(v)}, diff="7-9")
    if k == 3:
        di = r.randrange(2, 12); dq = r.choice([1, -1]) * r.randrange(1, 30)
        v = F(dq, di)
        return dict(text=f"Calculate, to two decimal places, the income elasticity of demand (YED) for {p} if income increases by {di}% and quantity demanded {'increases' if dq > 0 else 'decreases'} by {abs(dq)}%." + ADV,
                    working=f"{dq}% ÷ {di}%", answer=d2(v), values={"yed": float(v)}, diff="4-6")
    p1 = r.randrange(4, 30); q1 = r.randrange(100, 900, 10); p2 = p1 + r.choice([-2, -1, 1, 2]); q2 = q1 + r.randrange(-80, 81, 10)
    d = p2 * q2 - p1 * q1
    return dict(text=f"{c['name']} sells {p} at a market stall. When the price was {c['ccy']}{p1}, {q1} units were sold each week. After the price changed to {c['ccy']}{p2}, {q2} units were sold. Calculate the change in {c['name']}'s weekly total revenue." + ADV,
                working=f"({p2} × {q2}) - ({p1} × {q1}) = {p2 * q2} - {p1 * q1}", answer=f"{'an increase' if d >= 0 else 'a decrease'} of {money(c['ccy'], abs(d))}",
                values={"tr_change": d}, diff="4-6")


def pes_calc(r, c):
    p = r.choice(["wheat", "bricks", "plastic bottles", "T-shirts", "houses", "coffee beans"])
    if r.random() < 0.5:
        dq = r.randrange(2, 40); dp = r.randrange(3, 25)
        v = F(dq, dp)
        return dict(text=f"The price of {p} rose by {dp}% and the quantity supplied rose by {dq}%. Calculate, to two decimal places, the price elasticity of supply (PES)." + ADV,
                    working=f"{dq}% ÷ {dp}%", answer=d2(v), values={"pes": float(v)}, diff="4-6")
    p1 = r.randrange(5, 50); p2 = p1 + r.randrange(1, max(2, p1 // 3) + 1)
    q1 = r.randrange(500, 4000, 50); q2 = q1 + r.randrange(25, q1 // 2, 25)
    dq = F(q2 - q1, q1) * 100; dpp = F(p2 - p1, p1) * 100; v = dq / dpp
    return dict(text=f"When the price of {p} rose from {c['ccy']}{p1} to {c['ccy']}{p2} per unit, {c['firm']} increased its monthly supply from {q1:,} to {q2:,} units. Calculate, to two decimal places, the PES for the firm." + ADV,
                working=f"%Δ Qs = {d2(dq)}%; %Δ P = {d2(dpp)}%; {d2(dq)} ÷ {d2(dpp)}", answer=d2(v), values={"pes": float(v)}, diff="7-9")


def intervention_calc(r, c):
    k = r.randrange(3)
    p = r.choice(["cigarettes", "litres of petrol", "sugary drinks", "plastic bottles", "bottles of wine"])
    n = c["ncy"]
    if k == 0:
        t = F(r.randrange(5, 300), 100); q = r.randrange(2, 90) * 1000
        return dict(text=f"The government of {c['nation']} places a tax of {money(n, t)} per unit on {p}. After the tax, {q:,} units are sold each week. Calculate the weekly tax revenue for the government." + ADV,
                    working=f"{d2(t)} × {q}", answer=money(n, t * q), values={"revenue": float(t * q)}, diff="1-3")
    if k == 1:
        price = F(r.randrange(100, 5000), 100); rate = r.choice([5, 8, 10, 12, 15, 20, 25])
        new = price * (100 + rate) / 100
        return dict(text=f"A product has a price of {money(n, price)} before tax. The government introduces a sales tax of {rate}%. Calculate the price of the product including the tax, assuming the full tax is passed on to consumers." + ADV,
                    working=f"{d2(price)} × 1.{rate:02d}" if rate >= 10 else f"{d2(price)} × 1.0{rate}", answer=money(n, new), values={"new_price": float(new)}, diff="1-3")
    s = r.randrange(50, 3000, 50); q = r.randrange(200, 9000, 100)
    return dict(text=f"The government of {c['nation']} pays a subsidy of {money(n, s)} for each electric car sold. {q:,} electric cars are sold in a year. Calculate the total cost of the subsidy to the government." + ADV,
                working=f"{s} × {q}", answer=money(n, s * q), values={"cost": s * q}, diff="1-3")


def ext_calc(r, c):
    pc = r.randrange(20, 400); ec = r.randrange(5, 200)
    if r.random() < 0.5:
        return dict(text=f"A factory in {c['city']} has private costs of {money(c['ccy'], pc * 1000)} a week. The external costs of its pollution are estimated at {money(c['ccy'], ec * 1000)} a week. Calculate the social cost of the factory's production per week." + ADV,
                    working=f"{pc * 1000:,} + {ec * 1000:,}", answer=money(c["ccy"], (pc + ec) * 1000), values={"social_cost": (pc + ec) * 1000}, diff="1-3")
    pb = r.randrange(20, 300); eb = r.randrange(5, 150)
    return dict(text=f"A vaccination programme in {c['nation']} has social benefits of {c['ncy']}{pb + eb}m and private benefits of {c['ncy']}{pb}m. Calculate the external benefits of the programme." + ADV,
                working=f"{pb + eb} - {pb}", answer=f"{c['ncy']}{eb}m", values={"external_benefit": eb}, diff="1-3")


# ---------------------------------------------------------------- Topic 2

def productivity_calc(r, c):
    w = r.randrange(20, 400); per = r.randrange(50, 500)
    out = w * per
    if r.random() < 0.5:
        return dict(text=f"A firm employing {w} workers has a total output of {out:,} units each month. Calculate the labour productivity per worker per month." + ADV,
                    working=f"{out} ÷ {w}", answer=f"{per} units per worker", values={"productivity": per}, diff="1-3")
    w2 = w + r.randrange(-10, 30); out2 = out + r.randrange(-out // 10, out // 3)
    p1 = F(out, w); p2 = F(out2, w2); ch = (p2 - p1) / p1 * 100
    return dict(text=f"Figure 1 shows output and employment at {c['firm']} in two years. Calculate, to two decimal places, the percentage change in labour productivity." + ADV,
                table=T("Figure 1", ["Year", "Output (units)", "Number of workers"], [["Year 1", f"{out:,}", w], ["Year 2", f"{out2:,}", w2]]),
                working=f"Year 1: {out} ÷ {w} = {d2(p1)}; Year 2: {out2} ÷ {w2} = {d2(p2)}; ({d2(p2)} - {d2(p1)}) ÷ {d2(p1)} × 100", answer=pct(ch),
                values={"pct_change": float(ch)}, diff="7-9")


def costs_calc(r, c):
    k = r.randrange(6)
    cur = c["ccy"]
    if k == 0:
        fc = r.randrange(500, 9000, 50); vc = F(r.randrange(50, 2000), 100); q = r.randrange(100, 3000, 10)
        tc = fc + vc * q
        return dict(text=f"{c['firm']} has fixed costs of {money(cur, fc)} per month and variable costs of {money(cur, vc)} per unit. In March it produced {q:,} units. Calculate its total costs for March." + ADV,
                    working=f"{fc} + ({d2(vc)} × {q})", answer=money(cur, tc), values={"tc": float(tc)}, diff="4-6")
    if k == 1:
        tc = r.randrange(5000, 90000, 100); vc = r.randrange(1000, tc - 500, 100)
        return dict(text=f"In March, {c['firm']} had total costs of {money(cur, tc)} and total variable costs of {money(cur, vc)}. Work out the value of the firm's fixed costs in March." + ADV,
                    working=f"{tc} - {vc}", answer=money(cur, tc - vc), values={"fc": tc - vc}, diff="1-3")
    if k == 2:
        q = r.randrange(200, 5000, 10); p = F(r.randrange(100, 5000), 100); tc = r.randrange(int(p * q * F(6, 10)), int(p * q * F(13, 10)))
        prof = p * q - tc
        return dict(text=f"{c['name']} sold {q:,} items at {money(cur, p)} each. Total costs were {money(cur, tc)}. Calculate {c['name']}'s profit or loss." + ADV,
                    working=f"({q} × {d2(p)}) - {tc}", answer=f"{'profit' if prof >= 0 else 'loss'} of {money(cur, abs(prof))}", values={"profit": float(prof)}, diff="4-6")
    if k == 3:
        q = r.randrange(100, 2000, 10); tc = q * r.randrange(8, 250) + r.randrange(0, 990, 10)
        ac = F(tc, q)
        return dict(text=f"{c['firm']} produced {q:,} units at a total cost of {money(cur, tc)}. Calculate, to two decimal places, the average cost per unit." + ADV,
                    working=f"{tc} ÷ {q}", answer=money(cur, ac), values={"ac": float(ac)}, diff="1-3")
    if k == 4:
        p1 = r.randrange(10, 500) * 100; p2 = p1 + r.randrange(-p1 // 2, p1 // 2, 50)
        ch = F(p2 - p1, p1) * 100
        return dict(text=f"Figure 1 shows the annual profit of {c['firm']}. Calculate, to two decimal places, the percentage change in profit between {int(c['year']) - 1} and {c['year']}." + ADV,
                    table=T("Figure 1", ["Year", f"Profit ({cur.strip()})"], [[int(c['year']) - 1, f"{p1:,}"], [c['year'], f"{p2:,}"]]),
                    working=f"({p2} - {p1}) ÷ {p1} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")
    hire = r.randrange(40, 150, 5); fuel = F(r.randrange(10, 60), 100); km = r.randrange(30, 400, 5); ins = r.randrange(10, 40)
    tot = hire + fuel * km + ins
    return dict(text="Figure 1 shows the daily costs of hiring a van to deliver goods to a customer. Calculate the daily total cost of making the delivery." + ADV,
                table=T("Figure 1", [f"Van hire ({cur.strip()} per day)", f"Fuel ({cur.strip()} per km)", "Distance (km)", f"Insurance ({cur.strip()} per day)"], [[hire, d2(fuel), km, ins]]),
                working=f"{hire} + ({d2(fuel)} × {km}) + {ins}", answer=money(cur, tot), values={"tc": float(tot)}, diff="4-6")


def scale_calc(r, c):
    q1 = r.randrange(1, 20) * 1000; q2 = q1 * r.choice([2, 3, 4]); tc1 = q1 * r.randrange(5, 40); tc2 = int(q2 * (tc1 / q1) * r.uniform(0.6, 0.95))
    a1 = F(tc1, q1); a2 = F(tc2, q2); ch = (a2 - a1) / a1 * 100
    return dict(text=f"Figure 1 shows output and total costs for {c['firm']} before and after it expanded. Calculate, to two decimal places, the percentage change in average cost." + ADV,
                table=T("Figure 1", ["", "Output (units)", f"Total cost ({c['ccy'].strip()})"], [["Before", f"{q1:,}", f"{tc1:,}"], ["After", f"{q2:,}", f"{tc2:,}"]]),
                working=f"AC before = {tc1} ÷ {q1} = {d2(a1)}; AC after = {tc2} ÷ {q2} = {d2(a2)}; ({d2(a2)} - {d2(a1)}) ÷ {d2(a1)} × 100",
                answer=pct(ch), values={"pct_change_ac": float(ch)}, diff="7-9")


def labour_calc(r, c):
    k = 0 if "mw" in c else r.randrange(3)
    n = c["ncy"]
    if k == 0:
        w = F(c["mw"]) if "mw" in c else F(r.randrange(400, 1500), 100); h = r.randrange(20, 45)
        return dict(text=f"{c['nation']} has a minimum wage of {money(n, w)} per hour. Calculate the lowest weekly wage a worker can earn for a {h}-hour week." + ADV,
                    working=f"{d2(w)} × {h}", answer=money(n, w * h), values={"weekly": float(w * h)}, diff="1-3")
    if k == 1:
        w1 = F(r.randrange(500, 1500), 100); w2 = w1 + F(r.randrange(10, 150), 100)
        ch = (w2 - w1) / w1 * 100
        return dict(text=f"The minimum wage in {c['nation']} rose from {money(n, w1)} to {money(n, w2)} per hour. Calculate, to two decimal places, the percentage increase." + ADV,
                    working=f"({d2(w2)} - {d2(w1)}) ÷ {d2(w1)} × 100", answer=pct(ch), values={"pct": float(ch)}, diff="4-6")
    base = r.randrange(300, 900, 10); ot = r.randrange(2, 10); rate = F(r.randrange(1200, 3000), 100)
    tot = base + ot * rate * F(3, 2)
    return dict(text=f"{c['name']} earns a basic wage of {money(c['ccy'], base)} a week plus overtime paid at 1.5 times the hourly rate of {money(c['ccy'], rate)}. Calculate {c['name']}'s total pay in a week with {ot} hours of overtime." + ADV,
                working=f"{base} + ({ot} × {d2(rate)} × 1.5)", answer=money(c["ccy"], tot), values={"pay": float(tot)}, diff="4-6")


# ---------------------------------------------------------------- Topic 3

def growth_calc(r, c):
    n = c["ncy"]
    g1 = r.randrange(200, 2000); g2 = g1 + r.randrange(-g1 // 20, g1 // 12)
    if r.random() < 0.6:
        ch = F(g2 - g1, g1) * 100
        return dict(text=f"Figure 1 shows the real GDP of {c['nation']}. Calculate, to two decimal places, the rate of economic growth between {int(c['year']) - 1} and {c['year']}." + ADV,
                    table=T("Figure 1", ["Year", f"Real GDP ({n}bn)"], [[int(c['year']) - 1, g1], [c['year'], g2]]),
                    working=f"({g2} - {g1}) ÷ {g1} × 100", answer=pct(ch), values={"growth": float(ch)}, diff="4-6")
    pop = r.randrange(5, 90)
    pc = F(g1 * 1000, pop)
    return dict(text=f"{c['nation']} has a GDP of {n}{g1}bn and a population of {pop} million. Calculate, to two decimal places, GDP per capita." + ADV,
                working=f"({g1} × 1,000,000,000) ÷ ({pop} × 1,000,000) = {g1 * 1000:,} ÷ {pop}", answer=f"{n}{float(pc):,.2f}", values={"gdp_per_capita": float(pc)}, diff="4-6")


def unemployment_calc(r, c):
    lf = r.randrange(2000, 40000) * 1000; u = r.randrange(int(lf * 0.02), int(lf * 0.15))
    rate = F(u, lf) * 100
    if r.random() < 0.6:
        return dict(text=f"{c['nation']} has a labour force of {lf:,} people, of whom {u:,} are unemployed. Work out the unemployment rate as a percentage, to two decimal places." + ADV,
                    working=f"{u:,} ÷ {lf:,} × 100", answer=pct(rate), values={"rate": float(rate)}, diff="1-3")
    rt = F(r.randrange(25, 150), 10); lf2 = r.randrange(5, 60) * 100000
    num = rt * lf2 / 100
    return dict(text=f"The unemployment rate in {c['nation']} is {fmt_num(float(rt))}% and the labour force is {lf2:,}. Work out how many people are out of work." + ADV,
                working=f"{fmt_num(float(rt))} ÷ 100 × {lf2:,}", answer=f"{float(num):,.0f} people", values={"unemployed": float(num)}, diff="1-3")


def inflation_calc(r, c):
    k = r.randrange(3)
    if k == 0:
        i1 = F(r.randrange(1000, 1500), 10); i2 = i1 + F(r.randrange(-20, 120), 10)
        ch = (i2 - i1) / i1 * 100
        return dict(text=f"The consumer price index (CPI) in {c['nation']} rose from {fmt_num(float(i1))} to {fmt_num(float(i2))} over a year. Calculate, to two decimal places, the rate of inflation." + ADV,
                    working=f"({fmt_num(float(i2))} - {fmt_num(float(i1))}) ÷ {fmt_num(float(i1))} × 100", answer=pct(ch), values={"inflation": float(ch)}, diff="4-6")
    if k == 1:
        cats = r.sample(["Food", "Transport", "Housing", "Clothing", "Energy", "Leisure"], 4)
        vals = [F(r.randrange(-10, 120), 10) for _ in cats]
        avg = sum(vals) / len(vals)
        return dict(text=f"Figure 1 shows the annual percentage change in prices of four categories of goods in {c['nation']}. Calculate, to two decimal places, the average percentage change in prices across the four categories." + ADV,
                    table=T("Figure 1", ["Category", "Annual change in prices (%)"], [[a, fmt_num(float(v))] for a, v in zip(cats, vals)]),
                    working=f"({' + '.join(fmt_num(float(v)) for v in vals)}) ÷ 4", answer=pct(avg), values={"avg": float(avg)}, diff="1-3")
    b = r.randrange(40, 200); n = b + r.randrange(-5, 30)
    idx = F(n, b) * 100
    return dict(text=f"A basket of goods cost {money(c['ncy'], b)} in the base year and {money(c['ncy'], n)} this year. Calculate, to two decimal places, the price index for this year." + ADV,
                working=f"{n} ÷ {b} × 100", answer=d2(idx), values={"index": float(idx)}, diff="4-6")


def bop_calc(r, c):
    n = c["ncy"]
    xg, mg, xs, ms = (F(r.randrange(50, 900), 10) for _ in range(4))
    pi, si = F(r.randrange(-100, 100), 10), F(r.randrange(-50, 30), 10)
    if r.random() < 0.5:
        bal = xg - mg + xs - ms
        return dict(text=f"Figure 1 shows trade data for {c['nation']}. Calculate the balance of trade in goods and services in {n}bn." + ADV,
                    table=T("Figure 1", ["", f"{n}bn"], [["Exports of goods", fmt_num(float(xg))], ["Imports of goods", fmt_num(float(mg))], ["Exports of services", fmt_num(float(xs))], ["Imports of services", fmt_num(float(ms))]]),
                    working=f"({fmt_num(float(xg))} + {fmt_num(float(xs))}) - ({fmt_num(float(mg))} + {fmt_num(float(ms))})", answer=f"{'surplus' if bal >= 0 else 'deficit'} of {n}{d2(abs(bal))}bn",
                    values={"balance": float(bal)}, diff="4-6")
    bal = xg - mg + xs - ms + pi + si
    return dict(text=f"Figure 1 shows the components of the current account of {c['nation']}. Calculate the current account balance in {n}bn." + ADV,
                table=T("Figure 1", ["Component", f"Net balance ({n}bn)"], [["Trade in goods", fmt_num(float(xg - mg))], ["Trade in services", fmt_num(float(xs - ms))], ["Primary income", fmt_num(float(pi))], ["Secondary income", fmt_num(float(si))]]),
                working=f"{fmt_num(float(xg - mg))} + {fmt_num(float(xs - ms))} + {fmt_num(float(pi))} + {fmt_num(float(si))}", answer=f"{'surplus' if bal >= 0 else 'deficit'} of {n}{d2(abs(bal))}bn",
                values={"balance": float(bal)}, diff="4-6")


def redistribution_calc(r, c):
    n = c["ncy"]
    t1 = r.randrange(8, 20) * 1000; t2 = t1 + r.randrange(20, 50) * 1000
    r1, r2 = r.choice([(10, 25), (15, 30), (20, 40), (12, 35)])
    inc = r.randrange(t2 // 1000 + 5, t2 // 1000 + 60) * 1000
    tax = F(t2 - t1) * r1 / 100 + F(inc - t2) * r2 / 100
    tab = T("Figure 1", ["Annual income band", "Tax rate"], [[f"0 - {t1:,}", "0%"], [f"{t1 + 1:,} - {t2:,}", f"{r1}%"], [f"above {t2:,}", f"{r2}%"]])
    if r.random() < 0.5:
        return dict(text=f"Figure 1 shows the income tax bands in {c['nation']} (in {n}). Calculate the income tax paid by a worker earning {money(n, inc)} a year." + ADV,
                    table=tab, working=f"({t2} - {t1}) × {r1}% + ({inc} - {t2}) × {r2}%", answer=money(n, tax), values={"tax": float(tax)}, diff="7-9")
    avg = tax / inc * 100
    return dict(text=f"Figure 1 shows the income tax bands in {c['nation']} (in {n}). A worker earning {money(n, inc)} a year pays {money(n, tax)} in income tax. Calculate, to two decimal places, the average rate of tax paid." + ADV,
                table=tab, working=f"{d2(tax)} ÷ {inc} × 100", answer=pct(avg), values={"avg_rate": float(avg)}, diff="4-6")


def fiscal_calc(r, c):
    n = c["ncy"]
    if r.random() < 0.5:
        rev = F(r.randrange(20000, 90000), 1000); exp = rev + F(r.randrange(-8000, 12000), 1000)
        bal = rev - exp
        return dict(text=f"Figure 1 shows government revenue and expenditure for {c['nation']} in {c['year']}. Calculate the fiscal deficit or surplus in {n}bn." + ADV,
                    table=T("Figure 1", ["", f"{n}bn"], [["Total revenue", f"{float(rev):.3f}"], ["Total expenditure", f"{float(exp):.3f}"]]),
                    working=f"{float(rev):.3f} - {float(exp):.3f}", answer=f"{'surplus' if bal >= 0 else 'deficit'} of {n}{float(abs(bal)):.3f}bn",
                    values={"balance": float(bal)}, diff="1-3")
    taxes = {"Income tax": F(r.randrange(100, 300), 10), "Sales tax (VAT)": F(r.randrange(60, 200), 10), "Corporation tax": F(r.randrange(30, 100), 10),
             "Excise duties": F(r.randrange(10, 50), 10), "Customs duties": F(r.randrange(1, 10), 10)}
    direct = taxes["Income tax"] + taxes["Corporation tax"]
    return dict(text=f"Figure 1 shows selected tax receipts for the government of {c['nation']} in one month. Calculate the total revenue in {n}bn raised by direct taxes." + ADV,
                table=T("Figure 1", ["Tax", f"{n}bn"], [[k, fmt_num(float(v), dp=1)] for k, v in taxes.items()]),
                working=f"income tax {fmt_num(float(taxes['Income tax']), dp=1)} + corporation tax {fmt_num(float(taxes['Corporation tax']), dp=1)}",
                answer=f"{n}{fmt_num(float(direct), dp=1)}bn", values={"direct": float(direct)}, diff="4-6")


def monetary_calc(r, c):
    if r.random() < 0.5:
        a = F(r.randrange(5, 120), 10); b = a + F(r.choice([-1, 1]) * r.randrange(1, 30), 10)
        if b <= 0:
            b = a + 1
        ch = (b - a) / a * 100
        return dict(text=f"The central bank of {c['nation']} changed its interest rate from {fmt_num(float(a))}% in January to {fmt_num(float(b))}% in December. Calculate, to two decimal places, the percentage change in the interest rate." + ADV,
                    working=f"({fmt_num(float(b))} - {fmt_num(float(a))}) ÷ {fmt_num(float(a))} × 100", answer=pct(ch), values={"pct_change": float(ch)}, diff="4-6")
    loan = r.randrange(5, 300) * 1000; a = F(r.randrange(20, 80), 10); b = a + F(r.randrange(5, 25), 10)
    d = loan * (b - a) / 100
    return dict(text=f"{c['firm']} has a loan of {money(c['ccy'], loan)} on which it pays interest each year. The interest rate rises from {fmt_num(float(a))}% to {fmt_num(float(b))}%. Calculate the increase in the firm's annual interest payment." + ADV,
                working=f"{loan} × ({fmt_num(float(b))}% - {fmt_num(float(a))}%)", answer=money(c["ccy"], d), values={"increase": float(d)}, diff="4-6")


# ---------------------------------------------------------------- Topic 4

def glob_calc(r, c):
    n = c["ncy"]
    a = F(r.randrange(10, 400), 10); b = a + F(r.randrange(-50, 150), 10)
    if b <= 0:
        b = a + 1
    ch = (b - a) / a * 100
    return dict(text=f"Inflows of foreign direct investment (FDI) into {c['nation']} changed from {n}{fmt_num(float(a))}bn in {int(c['year']) - 1} to {n}{fmt_num(float(b))}bn in {c['year']}. Calculate, to two decimal places, the percentage change in FDI inflows." + ADV,
                working=f"({fmt_num(float(b))} - {fmt_num(float(a))}) ÷ {fmt_num(float(a))} × 100", answer=pct(ch), values={"pct": float(ch)}, diff="4-6")


def trade_calc(r, c):
    n = c["ncy"]
    x = r.randrange(20, 500); gdp = x * r.randrange(2, 8) + r.randrange(0, 50)
    if r.random() < 0.5:
        s = F(x, gdp) * 100
        return dict(text=f"{c['nation']} exported goods and services worth {n}{x}bn in a year when its GDP was {n}{gdp}bn. Calculate, to two decimal places, exports as a percentage of GDP." + ADV,
                    working=f"{x} ÷ {gdp} × 100", answer=pct(s), values={"share": float(s)}, diff="1-3")
    goods = r.sample(["Coffee", "Copper", "Textiles", "Machinery", "Tea", "Fish", "Timber"], 4)
    vals = [r.randrange(5, 80) for _ in goods]
    s = F(vals[0], sum(vals)) * 100
    return dict(text=f"Figure 1 shows the value of {c['nation']}'s main exports. Calculate, to two decimal places, the percentage of these exports accounted for by {goods[0].lower()}." + ADV,
                table=T("Figure 1", ["Export", f"Value ({n}bn)"], [[g, v] for g, v in zip(goods, vals)]),
                working=f"{vals[0]} ÷ ({' + '.join(map(str, vals))}) × 100", answer=pct(s), values={"share": float(s)}, diff="4-6")


def protection_calc(r, c):
    n = c["ncy"]
    if r.random() < 0.5:
        p = F(r.randrange(200, 9000), 100); t = r.choice([5, 8, 10, 12, 15, 20, 25, 30])
        new = p * (100 + t) / 100
        return dict(text=f"An imported product sells for {money(n, p)} in {c['nation']}. The government introduces {'an' if str(t).startswith('8') or t in (11, 18) else 'a'} {t}% tariff on its import price. Calculate the new price, assuming the whole tariff is passed on to consumers." + ADV,
                    working=f"{d2(p)} + ({d2(p)} × {t}%)", answer=money(n, new), values={"new_price": float(new)}, diff="1-3")
    t = r.randrange(1, 20); q = r.randrange(10, 500) * 1000
    return dict(text=f"{c['nation']} charges a tariff of {money(n, t)} per tonne on imported {r.choice(['rice', 'steel', 'sugar', 'wheat'])}. Imports are {q:,} tonnes a year. Calculate the annual tariff revenue." + ADV,
                working=f"{t} × {q:,}", answer=money(n, t * q), values={"revenue": t * q}, diff="1-3")


CURR = [("£", "€", "pound", "euro"), ("\\$", "£", "US dollar", "pound"), ("€", "\\$", "euro", "US dollar"), ("£", "¥", "pound", "yen"),
        ("\\$", "₹", "US dollar", "rupee"), ("€", "R", "euro", "rand")]


def exchange_calc(r, c, mcq=False):
    a, b, an, bn = r.choice(CURR)
    rate = F(r.randrange(50, 250), 100) if b not in ("¥", "₹", "R") else F(r.randrange(1500, 18000), 100)
    k = r.randrange(3)
    if k == 0:
        amt = r.randrange(50, 5000, 10)
        res = amt * rate
        return dict(text=f"The exchange rate is {a}1 = {b}{d2(rate)}. Calculate how many {bn}s ({b}) would be received in exchange for {a}{amt:,}." + ADV,
                    working=f"{amt} × {d2(rate)}", answer=f"{b}{float(res):,.2f}", values={"result": float(res)}, diff="1-3")
    if k == 1:
        amt = r.randrange(50, 5000, 10)
        res = F(amt) / rate
        return dict(text=f"The exchange rate is {a}1 = {b}{d2(rate)}. Calculate, to two decimal places, how many {an}s ({a}) are needed to buy {b}{amt:,}." + ADV,
                    working=f"{amt} ÷ {d2(rate)}", answer=f"{a}{float(res):,.2f}", values={"result": float(res)}, diff="4-6")
    r2 = rate * F(r.randrange(80, 120), 100)
    ch = (r2 - rate) / rate * 100
    return dict(text=f"The exchange rate of the {an} changed from {a}1 = {b}{d2(rate)} to {a}1 = {b}{d2(r2)}. Calculate, to two decimal places, the percentage change in the value of the {an} against the {bn}." + ADV,
                working=f"({d2(r2)} - {d2(rate)}) ÷ {d2(rate)} × 100", answer=pct((F(d2(r2)) - F(d2(rate))) / F(d2(rate)) * 100),
                values={"pct_change": float((F(d2(r2)) - F(d2(rate))) / F(d2(rate)) * 100)}, diff="4-6")


GEN = {"ppc": ppc_oc, "demand": demand_calc, "supply": supply_calc, "price": price_calc, "ped": ped_calc, "pes": pes_calc,
       "intervention": intervention_calc, "externalities": ext_calc, "productivity": productivity_calc, "costs": costs_calc,
       "scale": scale_calc, "labour": labour_calc, "growth": growth_calc, "unemployment": unemployment_calc, "inflation": inflation_calc,
       "bop": bop_calc, "redistribution": redistribution_calc, "fiscal": fiscal_calc, "monetary": monetary_calc,
       "globalisation": glob_calc, "trade": trade_calc, "protection": protection_calc, "exchange": exchange_calc}
