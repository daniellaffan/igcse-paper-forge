"""Longer extracts for the 9-mark (assess) and 12-mark (evaluate) questions.

Real 4EC1 assess/evaluate questions sit under an extract the candidate is expected to use for AO2/AO3:
a short narrative full of figures, and often a table of data that changes over time. Each issue in the
knowledge base keeps its short opening context (`ctx`); this module adds, per issue, further paragraphs
of narrative with numbers and, for many issues, a time-series table (printed as a Figure).

Templates use the same syntax as economics_util.fill and may reuse any variable set by the issue's ctx.
A separate RNG (seeded from the question's own text) is used so other questions in the bank do not change.
All data are fictional.
"""
import hashlib
import random
import re

from economics_util import fill


def rng_for(*bits):
    h = hashlib.sha256("|".join(bits).encode()).hexdigest()
    return random.Random(int(h[:12], 16))


_ARITH = re.compile(r"^[0-9.+\-*/() ]+$")


def calc(expr):
    """Evaluate a filled arithmetic expression such as "25*0.9" (digits and + - * / only)."""
    e = expr.replace(",", "").replace("–", "-").strip()
    if not _ARITH.match(e):
        raise ValueError(f"not arithmetic: {expr!r}")
    return float(eval(e, {"__builtins__": {}}, {}))  # noqa: S307 - restricted to arithmetic by the regex


def _num(v, c, rx):
    if isinstance(v, str):
        return calc(fill(v, c, rx))
    return float(v)


def cell(x, c, rx):
    """Fill a table cell; a cell starting with '=' is arithmetic, printed as a whole number."""
    if x.startswith("="):
        return _fmt(calc(fill(x[1:], c, rx)), 0)
    return fill(x, c, rx)


def _fmt(x, dp):
    s = f"{x:,.{dp}f}"
    return s


def series(rx, start, end, n, dp, wobble=0.12):
    """n values from start to end with a little noise; the first and last are exact."""
    if n == 1:
        return [end]
    out = []
    for i in range(n):
        t = i / (n - 1)
        v = start + (end - start) * t
        if 0 < i < n - 1:
            v += (rx.random() - 0.5) * wobble * (abs(end - start) + abs(end) * 0.05)
        out.append(v)
    return out


def T(caption, cols, n=5, first="Year", labels=None, note=None):
    """A table spec. cols: list of (header, start, end, dp). Values may be templates such as "{i}"."""
    def build(c, rx):
        last = int(c.get("year", "2025"))
        lab = labels or [str(last - n + 1 + k) for k in range(n)]
        vals = []
        for h, s, e, dp in cols:
            a, b = _num(s, c, rx), _num(e, c, rx)
            vals.append([_fmt(v, dp) for v in series(rx, a, b, len(lab), dp)])
        rows = [[lab[k]] + [vals[j][k] for j in range(len(cols))] for k in range(len(lab))]
        return {"type": "table", "caption": fill(caption, c, rx), "headers": [first] + [fill(h, c, rx) for h, *_ in cols],
                "rows": rows, **({"note": note} if note else {})}
    return build


def S(caption, headers, rows, note=None):
    """A static (non-time-series) table; cells are templates."""
    def build(c, rx):
        return {"type": "table", "caption": fill(caption, c, rx), "headers": [fill(h, c, rx) for h in headers],
                "rows": [[cell(x, c, rx) for x in r] for r in rows], **({"note": note} if note else {})}
    return build


def X(*paras, table=None):
    return {"paras": list(paras), "table": table}


EXT = {
    "economic-problem": [
        X("Last year the government collected {ncy}{#x_rev:8-15}bn in tax. The health ministry says it needs an extra {ncy}{#x_h:2-4}bn to cut hospital waiting lists, which now average {#x_wait:14-30} weeks. The education ministry wants {ncy}{#x_e:1-3}bn to build new secondary schools because class sizes have risen to an average of {#x_cs:38-48} pupils.",
          "The transport minister points out that only {#x_road:30-55}% of rural roads are paved, which raises costs for farmers taking crops to market. One adviser has suggested raising sales tax by {#x_st:2-4} percentage points, but consumer groups say households are already struggling with rising prices.",
          table=T("Figure 1: Population and government revenue in {nation}", [("Population (millions)", "{pop}*0.9", "{pop}", 1), ("Tax revenue ({ncy}bn)", "{x_rev}*0.92", "{x_rev}", 1)])),
        X("{firm} employs {#x_w:120-400} people and has {#x_vac:15-40} vacancies for machine operators and engineers that have been open for more than three months. Local colleges train only about {#x_col:20-60} engineers a year. The firm is paying overtime, which costs {#x_ot:40-60}% more per hour than normal wages.",
          "Its main raw material is steel. The firm buys about {#x_t:500-2000} tonnes a year and has been told that suppliers may not be able to meet orders on time because mines abroad have cut output. Managers are considering buying machinery that would need fewer workers, at a cost of {ccy}{#x_m:1-4} million.",
          table=T("Figure 1: Steel price paid by {firm} ({ccy} per tonne)", [("Price ({ccy} per tonne)", 600, "600*(1+{rise}/100)", 0)], n=4)),
        X("Graduates in engineering in {country} earn on average {ccy}{#x_g:700-1100} a week five years after finishing their degree. The course lasts {=x_y:three|four} years and tuition and living costs are about {ccy}{#x_fee:9-15},000 a year, although {name} could apply for a loan.",
          "{name}'s friends who started work at 18 have received pay rises of about {#x_pr:3-5}% a year. However, the job {name} has been offered is in a warehouse where the employer is planning to introduce automated picking machines over the next few years.",
          table=S("Figure 1: Average weekly pay in {country} by age ({ccy})", ["Age", "Left school at 18", "Engineering graduate"],
                  [["22", "{wage}", "–"], ["25", "{#x_a:420-560}", "{#x_b:620-760}"], ["30", "{#x_c:480-640}", "{#x_d:800-1000}"], ["40", "{#x_e2:520-700}", "{#x_f:1050-1400}"]])),
    ],
    "demand": [
        X("{firm}'s sales rose by {#x_s:4-9}% last year to {#x_u:2-6} million units. The firm's {prod} sells for {ccy}{=x_p:2.40|2.90|3.20}, while the supermarket's own-brand version costs {ccy}{=x_p2:1.70|1.90|2.10}. Market research suggests that {#x_young:55-70}% of buyers are aged under 35.",
          "A government health campaign, \"Eat Better {country}\", has been running for {=x_m:six|nine|twelve} months. Over the same period, the number of people describing themselves as following a plant-based or low-sugar diet rose from {#x_d1:8-12}% to {#x_d2:14-19}% of adults. However, analysts warn that consumers may switch to cheaper products if a slowdown in the economy reduces incomes.",
          table=T("Figure 1: Average household income and {firm}'s sales", [("Average income index (2020=100)", 100, "100+3*{inc}", 1), ("{firm} sales (million units)", "{x_u}*0.8", "{x_u}", 2)])),
        X("The population of {city} is now about {#x_pop:400-900},000. The number of children under 10 has risen by {#x_ch:12-25}% in five years, and {#x_hh:6-15},000 new homes have been completed. Average household income in the new estates is {ccy}{#x_inc:38-55},000, above the city average.",
          "Two new primary schools have opened, but local shops report mixed results: a supermarket on the edge of the city has extended its opening hours, while some shops in the old centre say trade has fallen as families shop closer to home or online. Bus use has risen by {#x_bus:5-12}%.",
          table=T("Figure 1: Population of {city} (thousands)", [("Population (thousands)", "{x_pop}/(1+{pop}/100)", "{x_pop}", 0)], n=6)),
    ],
    "supply": [
        X("The drought reduced rainfall in the main growing region by {#x_rain:30-55}% compared with the average. Around {#x_far:40-70}% of farms in {nation} are small family farms with no irrigation. Fertiliser now costs {ncy}{#x_fert:450-800} per tonne.",
          "The irrigation subsidy pays {#x_sub:40-60}% of the cost of installing equipment, but the first systems will not be in place until next year. Meanwhile, the price of {crop} on world markets has risen, which some farmers say encourages them to plant more land.",
          table=T("Figure 1: {crop} output in {nation} (thousand tonnes)", [("Output (thousand tonnes)", 420, "420*(0.6+0.1*{f}/40)", 0)], n=5)),
        X("{firm} produces about {#x_u:1-5} million {prod} a year. The new automated lines cost {ccy}{#x_cap:20-60} million and the firm says they have cut the time to assemble each unit by {#x_t:20-40}%. Wages make up about {#x_wage:20-35}% of its total costs.",
          "The new tax on electronic goods is {ncy}{#x_tax:5-20} per unit. Some rival firms that have not automated have announced they will cut output. {firm} says it expects to raise output by about {#x_g:3-8}% next year.",
          table=T("Figure 1: {firm} average cost per unit ({ccy})", [("Average cost per unit ({ccy})", 210, 185, 0)], n=4)),
    ],
    "price": [
        X("Two of the largest producing countries reported harvests {#x_h:15-30}% below normal because of extreme weather and plant disease. Stocks held by traders have fallen to their lowest level for {#x_y:10-20} years.",
          "At the same time, consumption in {mkt} has risen by about {#x_c:4-8}% a year. Farmers in several countries have started planting new trees, but these take {=x_t:three to five|four to six} years to produce a full crop. Some food manufacturers have reduced the size of their products rather than raise prices.",
          table=T("Figure 1: Average world price of {prod} (US\\$ per tonne)", [("Price (US\\$ per tonne)", 2400, "2400*(1+{p}/100)", 0)], n=5)),
        X("The average monthly rent for a one-bedroom flat in {city} is now {ccy}{#x_r:900-1400}. The number of students at the city's two universities has risen by {#x_st:6-12},000 in three years, and a technology park has created around {#x_j:3-8},000 jobs.",
          "Only {#x_b:400-1200} new flats were completed last year. The city council has approved plans for a new housing development of {#x_n:2-5},000 homes, but builders say it will take at least four years to complete. Some landlords have converted flats into short-stay holiday lets.",
          table=T("Figure 1: Rents and new flats in {city}", [("Average monthly rent ({ccy})", "{x_r}/(1+{r}/100)/1.08", "{x_r}", 0), ("New flats completed", 1500, "{x_b}", 0)], n=4)),
        X("{firm} produced {#x_q:40-120},000 units for the launch and says it can make about {#x_w:5-15},000 more each week, but a shortage of computer chips is limiting production. Online, the product has been resold for up to {ccy}{#x_res:350-900}.",
          "Customer reviews have been very positive, and the firm's share price has risen by {#x_sp:8-20}%. However, some fans have complained on social media about resellers, and a rival firm plans to launch a similar product in {=x_m:three|four|six} months.",
          table=S("Figure 1: Stock levels of the {prod} in the first four weeks", ["Week", "Units delivered to shops", "Units in stock at end of week"],
                  [["1", "{x_q},000", "0"], ["2", "{#x_d2:6-12},000", "0"], ["3", "{#x_d3:8-14},000", "0"], ["4", "{#x_d4:9-15},000", "{#x_s4:1-3},000"]])),
    ],
    "ped": [
        X("{firm} carries about {#x_p:20-60},000 passengers a day. The single fare is {ccy}{=x_f:1.80|2.00|2.40}. A survey found that {#x_w:55-75}% of passengers use the bus to get to work and {#x_s:15-25}% are students or pensioners.",
          "Train services cover only {#x_r:3-6} of the city's {#x_rt:20-35} bus routes. The bicycle-hire scheme has {#x_b:500-2000} bikes and charges {ccy}1 for 30 minutes. When {firm} last raised fares, by 5% three years ago, passenger numbers fell by about {#x_fall:1-3}%.",
          table=T("Figure 1: {firm} passenger numbers (thousands per day)", [("Passengers (thousands per day)", "{x_p}*1.03", "{x_p}", 1), ("Average fare ({ccy})", "{x_f}*0.9", "{x_f}", 2)], n=4)),
        X("Consumers in {nation} spend {ncy}{#x_sp:2-9}bn a year on {prod}. The government estimates that illnesses linked to {prod} cost the health service {ncy}{#x_hc:1-4}bn a year.",
          "A neighbouring country introduced a similar tax {=x_y:two|three|four} years ago. Consumption there fell by about {#x_c:6-12}% in the first year, and tax revenue was higher than expected. However, some consumers began buying {prod} across the border where prices are lower, and low-income households spend a larger share of their income on {prod}.",
          table=T("Figure 1: Consumption of {prod} per person in {nation}", [("Consumption per person (units a year)", 210, 240, 0)], n=5)),
        X("The premium brand sells {#x_pq:2-6} million units a year at {ccy}{=x_pp:2.50|2.80|3.10}. There are at least {#x_comp:6-12} similar brands on supermarket shelves. The basic product sells {#x_bq:8-20} million units at {ccy}{=x_bp:0.90|1.10|1.20}.",
          "A trial in {#x_tr:20-40} shops last year cut the price of the premium brand by 10% and sales rose by {#x_rise:18-28}%. A similar trial for the basic product saw sales rise by only {#x_rise2:2-5}%.",
          table=S("Figure 1: Results of {firm}'s price trial", ["Product", "Price change", "Change in quantity sold"],
                  [["Premium brand", "–10%", "+{x_rise}%"], ["Basic product", "–10%", "+{x_rise2}%"]])),
    ],
    "pes": [
        X("The textile factories are operating at about {#x_cap:60-75}% of capacity and can add a second shift within {=x_wk:two|three|four} weeks. Cotton cloth can be stored for many months. Around {#x_tw:1-3} million people work in the textile industry.",
          "{crop} is planted once a year and takes several months to grow. Around {#x_ag:35-45}% of the workforce is employed in agriculture, mainly on small farms. Farmers have little storage, and much of the harvest must be sold within weeks.",
          table=S("Figure 1: Change in output after a 10% rise in price", ["Product", "Change in output after 1 month", "Change in output after 12 months"],
                  [["Shirts and jeans", "+{#x_t1:6-10}%", "+{#x_t2:12-18}%"], ["{crop}", "0%", "+{#x_c2:3-6}%"]])),
        X("The average house price in {city} is now {ccy}{#x_hp:250-450},000, about {#x_ratio:8-12} times average earnings. Builders completed {#x_b:1-3},000 homes last year, while the number of households grew by {#x_hh:4-7},000.",
          "Planning permission takes on average {#x_pp:12-24} months. The construction industry says it has {#x_vac:3-8},000 unfilled vacancies for bricklayers, electricians and plumbers. The city council has said it will release land it owns for building, but this will take several years.",
          table=T("Figure 1: Housing in {city}", [("Average house price ({ccy} thousand)", "{x_hp}/(1+{p}/100)/1.15", "{x_hp}", 0), ("New homes completed (thousands)", "{x_b}*1.05", "{x_b}", 1)], n=4)),
    ],
    "mixed": [
        X("Public spending in {nation} is {ncy}{#x_ps:40-90}bn a year. Healthcare and education take {#x_he:45-55}% of this. The state also owns the railway, which made a loss of {ncy}{#x_l:200-900} million last year.",
          "A business group says lower taxes would encourage investment and that private firms could run some services more efficiently. However, a survey found {#x_s:60-75}% of people want free healthcare to continue, and in areas where private schools charge fees, attendance by children from low-income families is low.",
          table=T("Figure 1: Taxes as a percentage of national income in {nation}", [("Taxes (% of national income)", "{t}-3", "{t}", 1)], n=5)),
        X("A survey found {#x_s:60-80}% of residents feel unsafe walking at night. Police figures show street crime rose by {#x_c:8-20}% last year. Installing lights would cost about {ncy}{#x_cost:15-40} million, plus {ncy}{#x_run:1-3} million a year to run.",
          "Once a street light is installed, everyone who walks along the street benefits, whether or not they have paid. Some shopkeepers say they would contribute, but most residents say they would not pay voluntarily. The government already faces a budget deficit.",
          table=T("Figure 1: Recorded street crime in {nation} (thousands)", [("Street crimes (thousands)", 42, "42*(1+{x_c}/100)*1.06", 1)], n=4)),
    ],
    "intervention": [
        X("Average rents in {city} have risen by {#x_r:12-20}% in two years, while average wages rose by {#x_w:3-6}%. The council estimates {#x_q:5-12},000 households are waiting for affordable housing.",
          "A survey of landlords found {#x_sell:15-30}% would consider selling if the maximum rent was introduced.",
          table=None),
        X("{crop} farmers produce about {#x_o:2-6} million tonnes a year.", table=None),
        X("About {#x_ev:2-6}% of new cars sold in {nation} last year were electric. Electric cars cost on average {ncy}{#x_gap:6-12},000 more than a similar petrol car. There are only {#x_ch:400-1500} public charging points in the country.",
          "The subsidy would cost the government an estimated {ncy}{#x_cost:150-600} million a year. A tax on petrol and diesel cars would raise revenue, but car dealers say it would hit rural drivers who have few alternatives. A neighbouring country that introduced a subsidy saw electric car sales rise to {#x_nb:15-25}% of new cars within four years.",
          table=T("Figure 1: Electric cars as a share of new car sales in {nation} (%)", [("Electric cars (% of new car sales)", 0.8, "{x_ev}", 1)], n=5)),
    ],
    "externalities": [
        X("Before the ban, an estimated {#x_b:3-8} billion plastic bags were used each year in {nation}. A survey of beaches found {#x_red:60-80}% less plastic waste than in the year before the ban. The ban is enforced by about {#x_ins:100-300} inspectors, at a cost of {ncy}{#x_cost:5-20} million a year.",
          "Shops caught giving out bags can be fined up to {ncy}{#x_fine:500-2000}. Inspectors found bags being given out in {#x_ill:8-20}% of market stalls they visited last year. Some shops have switched to paper bags, which cost more to produce.",
          table=T("Figure 1: Plastic waste found on beaches in {nation} (kg per km)", [("Plastic waste (kg per km)", 140, "140*(1-{x_red}/100)", 0)], n=5)),
        X("Fish catches in the river fell from {#x_f1:900-1400} tonnes to {#x_f2:400-700} tonnes in five years. About {#x_fm:300-800} families rely on fishing for their income. {firm} made a profit of {ccy}{#x_p:20-80} million last year.",
          "The proposed tax would charge {ccy}{#x_t:50-200} for each tonne of waste discharged. {firm} says the tax could force it to cut jobs, and that it already plans to spend {ccy}{#x_inv:5-15} million on cleaner equipment. Environmental groups would prefer a strict legal limit on discharges.",
          table=T("Figure 1: Fish caught in the river near {city} (tonnes)", [("Fish caught (tonnes)", "{x_f1}", "{x_f2}", 0)], n=6)),
        X("The vaccination programme costs the government {ncy}{#x_cost:40-120} million a year, about {#x_pc:1-3}% of the health budget. Hospital admissions for measles and whooping cough have fallen by {#x_adm:50-75}%.",
          "Health experts say when more than about 90% of people are vaccinated, others are also protected because diseases spread less easily. However, the government also faces growing demand for cancer treatment and mental health services, and rural clinics report shortages of nurses.",
          table=T("Figure 1: Vaccination rate and hospital admissions in {nation}", [("Children vaccinated (%)", "{v1}", "{v2}", 0), ("Hospital admissions (thousands)", 24, "24*(1-{x_adm}/100)", 1)], n=6)),
    ],
    "production": [
        X("The share of employment in agriculture has fallen steadily as farms have bought tractors and harvesters. Over the same period, average incomes in {nation} have risen about {#x_inc:3-5} times in real terms, and more young people now go to university.",
          "Tourism now employs {#x_tour:8-15}% of workers, and a financial centre has grown in the capital. However, manufacturing jobs have fallen since a peak of {#x_peak:28-35}% twenty years ago, as some factories moved to countries with lower wages.",
          table=S("Figure 1: Employment by sector in {nation} (% of workers)", ["Year", "Primary", "Secondary", "Tertiary"],
                  [["50 years ago", "{#x_p0:55-65}", "{#x_s0:15-20}", "=100-{x_p0}-{x_s0}"], ["20 years ago", "{#x_p1:28-35}", "{x_peak}", "=100-{x_p1}-{x_peak}"], ["Today", "{ag}", "{man}", "=100-{ag}-{man}"]])),
        X("{nation} exported {#x_t:200-600},000 tonnes of raw {raw} last year, earning {ncy}{#x_e:300-900} million. Processed {raw} products sell for about {#x_m:3-6} times the price per tonne of the raw crop.",
          "The new factory will cost {ncy}{#x_c:40-120} million and is expected to create {#x_j:600-2000} jobs. It will need a reliable electricity supply, but power cuts are common in the region. Unemployment in the area is {#x_u:9-16}%.",
          table=T("Figure 1: Export earnings from raw {raw} ({ncy} million)", [("Export earnings ({ncy} million)", "{x_e}*1.3", "{x_e}", 0)], n=5)),
    ],
    "productivity": [
        X("The factory produces about {#x_o:200-800},000 units a week. Before the production line was reorganised, each worker made complete products and output per worker was {#x_lo:20-35}% lower. Staff now need only {=x_tr:two|three} days of training.",
          "However, a staff survey found {#x_bored:45-65}% of workers describe their job as boring, and staff turnover has risen to {#x_to:18-30}% a year. Last month a breakdown at the sealing stage stopped the whole line for {#x_h:6-14} hours.",
          table=T("Figure 1: {firm} output per worker and staff turnover", [("Output per worker per week (units)", 280, 360, 0), ("Staff turnover (%)", 10, "{x_to}", 0)], n=4)),
        X("Only {#x_tr:15-30}% of firms in {nation} provided training for their staff last year. The average age of factory machinery is {#x_age:15-25} years. Around {#x_ed:30-45}% of workers left school without qualifications.",
          "The government has {ncy}{#x_b:1-4}bn available for new policies. Business leaders want tax relief on new machinery, while trade unions want more spending on apprenticeships and adult education.",
          table=T("Figure 1: Output per worker (US\\$ thousand per year)", [("{nation}", 18, "22", 1), ("Neighbouring countries (average)", 24, "22/(1-{g}/100)", 1)], n=5)),
    ],
    "costs": [
        X("{firm} has {#x_v:40-120} vehicles and spends about {ccy}{#x_f:1-4} million a year on fuel. Drivers' wages make up {#x_w:35-50}% of total costs. The firm's profit last year was only {ccy}{#x_p:80-250},000 on revenue of {ccy}{#x_r:6-15} million.",
          "Two rival firms operate in {city}, and a ride-hailing app has entered the market charging about {#x_cheap:10-20}% less than {firm}. Customer surveys show that reliability is the most important factor for {#x_rel:40-60}% of customers, ahead of price.",
          table=T("Figure 1: {firm} costs and revenue ({ccy} million)", [("Total revenue", "{x_r}*0.96", "{x_r}", 2), ("Fuel costs", "{x_f}/(1+{f}/100)", "{x_f}", 2)], n=4)),
        X("The business sells about {#x_q:3000-8000} items a month at an average price of {ccy}{#x_p:3-8}. Variable costs are about {ccy}{=x_vc:1.20|1.50|1.80} per item. The new machine would cost {ccy}{#x_m:20-60},000 and raise fixed costs by {ccy}{#x_fc:1-3},000 a month.",
          "{name} says orders have been turned away on busy days, but is unsure whether demand would be high enough to sell twice as much. The machine would also allow {name} to cut the time staff spend on each item.",
          table=S("Figure 1: {name}'s monthly costs ({ccy})", ["", "Now", "With new machine"],
                  [["Fixed costs", "{fc},000", "{fc},000 + {x_fc},000"], ["Variable cost per item", "{x_vc}", "{x_vc}"], ["Maximum output (items)", "{x_q}", "2 × {x_q}"]])),
        X("{firm}'s total revenue was {ccy}{#x_tr:40-120} million last year. Its biggest costs are components bought from abroad, warehouse rent and wages. A weaker currency has raised the cost of imported components by about {#x_imp:8-15}%.",
          "The firm has {#x_sh:20-60} shops and an online store. Online sales grew by {#x_on:20-35}% last year, while sales in shops fell. Some managers want to close the least profitable shops; others want to raise prices on premium models, where competition is weaker.",
          table=T("Figure 1: {firm} revenue, costs and profit ({ccy} million)", [("Total revenue", "{x_tr}/(1+{tr}/100)", "{x_tr}", 1), ("Total costs", "{x_tr}/(1+{tr}/100)*0.9", "{x_tr}*0.97", 1)], n=3)),
    ],
    "objectives": [
        X("Each class has a maximum of {#x_c:15-25} students paying {ccy}{#x_f:8-15} a session. The business made a profit of {ccy}{#x_p:20-45},000 last year. A second site would cost {ccy}{#x_rent:1-3},000 a month in rent, and {name} would need to hire {=x_s:two|three} new instructors.",
          "There is a waiting list of {#x_w:20-60} people. However, a national chain has opened a branch {#x_km:2-5} km away offering lower prices, and {name} already works more than 50 hours a week.",
          table=T("Figure 1: Number of members", [("Members", 120, 210, 0)], n=4)),
        X("The two firms together employ {#x_e:20-60},000 people and serve around {#x_cust:5-15} million customers. They say the takeover would save {ccy}{#x_sav:100-400} million a year through bulk buying and closing duplicate offices.",
          "Consumer groups say prices could rise because there would be less competition. The competition authority in {country} must approve any merger that creates a firm with more than 25% of the market. A smaller rival with {#x_r:8-15}% of the market says it would struggle to compete.",
          table=S("Figure 1: Market shares in the {ind} market in {country} (%)", ["Firm", "Market share (%)"],
                  [["{firm}", "{#x_m1:22-30}"], ["Main rival", "={ms}-{x_m1}"], ["All other firms", "=100-{ms}"]])),
        X("{firm} has {#x_e:80-250} employees and made a profit of {ccy}{#x_p:1-4} million last year. Its market share is {#x_ms:6-12}%. Sustainable materials cost about {#x_c:10-25}% more than standard materials.",
          "A survey found that {#x_s:40-60}% of customers would pay more for sustainable products. The family owners rely on profits for their income and want to pay off a loan of {ccy}{#x_l:2-6} million within three years.",
          table=T("Figure 1: {firm} profit ({ccy} million) and market share (%)", [("Profit ({ccy} million)", "{x_p}*0.85", "{x_p}", 2), ("Market share (%)", "{x_ms}+1", "{x_ms}", 1)], n=4)),
    ],
    "scale": [
        X("{firm} has a market share of {#x_ms:25-35}%. Because it buys in bulk, it says it pays suppliers about {#x_bulk:8-15}% less than smaller rivals. It has its own fleet of {#x_tr:200-600} lorries and a central warehouse.",
          "Last year it opened {#x_new:10-30} new shops, but average sales per shop fell by {#x_fall:2-5}%. Some new shops are in small towns with low population. Managers say communication between head office and shops has become slower.",
          table=T("Figure 1: {firm} number of shops and average cost per shop", [("Number of shops", "{n}*0.8", "{n}", 0), ("Average cost per shop ({ccy} million)", 3.2, 3.0, 2)], n=5)),
        X("Staff turnover has risen from {#x_t1:6-10}% to {#x_t2:18-28}% a year. There are now {#x_lay:6-9} layers of management between the chief executive and shop-floor workers. A survey found only {#x_s:25-40}% of staff feel informed about the firm's plans.",
          "Average cost per unit fell as the firm grew, but has risen by {#x_ac:5-12}% over the last two years. Managers are considering splitting the firm into separate divisions, but this would mean some jobs are duplicated.",
          table=T("Figure 1: {firm} employees and average cost per unit ({ccy})", [("Employees", "{a}", "{b}", 0), ("Average cost per unit", 12.0, 10.6, 2)], n=6)),
    ],
    "competition": [
        X("Prices of the three main firms are within {#x_p:2-5}% of each other. Together they spend about {ccy}{#x_ad:100-400} million a year on advertising. One firm cut its prices by 10% last year, but the others matched the cut within a week.",
          "The firms have each invested heavily in new products: {#x_np:15-40} new products were launched last year. A small new firm entered the market two years ago but now has only {#x_sm:2-4}% market share. The competition authority has received complaints about the firms copying each other's price rises.",
          table=T("Figure 1: Average price in the {ind} market (index, first year = 100)", [("Average price index", 100, 112, 1), ("Combined market share of three largest firms (%)", "{ms}-4", "{ms}", 0)], n=5)),
        X("{firm} made a profit of {ncy}{#x_p:200-900} million last year. Prices for customers have risen by {#x_pr:15-30}% in three years, compared with general inflation of {#x_inf:8-12}%. There are {#x_c:5-20},000 complaints a year about service.",
          "Two foreign firms have said they would enter the market if allowed. However, building a new network would cost billions, and some experts say only one network is efficient. Investment by {firm} in new equipment has fallen to {ncy}{#x_inv:50-150} million a year.",
          table=T("Figure 1: {firm} prices and investment", [("Price index (first year = 100)", 100, "100+{x_pr}", 1), ("Investment ({ncy} million)", 260, "{x_inv}", 0)], n=4)),
        X("Online sales now make up {#x_on:25-40}% of retail sales in {city}, up from {#x_on0:10-15}% five years ago. The online retailer offers delivery for {ccy}{=x_d:0|1.99|2.99} on orders over {ccy}20.",
          "Some independent shops have responded by opening their own websites or offering services that cannot be bought online, such as repairs and advice. Shop rents in the city centre have fallen by {#x_rent:10-20}%.",
          table=T("Figure 1: Online share of retail sales in {city} (%)", [("Online share (%)", "{x_on0}", "{x_on}", 0)], n=6)),
    ],
    "labour": [
        X("About {#x_mw:8-15}% of workers in {nation} are paid the minimum wage, mostly in retail, hospitality and cleaning. Average earnings across the economy rose by {#x_ae:3-5}% last year, and inflation was {#x_i:3-6}%.",
          "A survey of small firms found {#x_cut:25-40}% planned to reduce staff hours. However, unemployment is low at {#x_u:3-5}%, and some employers say a higher wage may help them recruit and keep staff. The government expects to collect more income tax.",
          table=T("Figure 1: Minimum wage in {nation} ({ncy} per hour)", [("Minimum wage ({ncy} per hour)", "{mw}*0.78", "{mw}", 2), ("Inflation (%)", 2.0, "{x_i}", 1)], n=5)),
        X("There are {#x_n:150-350},000 nurses in {nation}. Their pay has risen by {#x_p3:4-8}% in total over the last three years, while prices rose by {#x_i3:12-18}%. About {#x_l:3-8},000 nurses left last year to work abroad.",
          "The union represents {#x_u:60-80}% of nurses. The government says it cannot afford a {p}% rise, which would cost {ncy}{#x_c:1-3}bn a year, but polls show {#x_pub:60-75}% of the public support the nurses.",
          table=T("Figure 1: Nurse vacancies in {nation} (thousands)", [("Vacancies (thousands)", "{v}*0.55", "{v}", 1)], n=5)),
        X("The average software engineer in {city} earns {ccy}{#x_e:60-90},000 a year. There are about {#x_v:3-8},000 unfilled software jobs. Engineering degrees take four years, and only {#x_g:1-3},000 people graduate each year.",
          "Online coding courses lasting a few months have become popular. Shop assistant jobs often need no qualifications, and many shops are introducing self-service tills. Some engineering firms are moving work to other countries where engineers are cheaper.",
          table=T("Figure 1: Average annual pay in {city} ({ccy} thousand)", [("Software engineers", "{x_e}*0.85", "{x_e}", 1), ("Shop assistants", "{x_e}/{a}*0.9", "{x_e}/{a}", 1)], n=5)),
    ],
    "government": [
        X("The airport handled {#x_p:8-20} million passengers last year, up {#x_g:8-15}% on the year before. Government subsidies to the airport were {ncy}{#x_s:30-90} million. The airport has {#x_w:3-7},000 workers, most of whom are union members.",
          "Private investors say they would build a new terminal costing {ncy}{#x_t:300-800} million. In another country where an airport was privatised, landing charges for airlines rose by {#x_lc:20-35}%, but waiting times at security fell.",
          table=T("Figure 1: Passengers using the airport (millions)", [("Passengers (millions)", "{x_p}*0.7", "{x_p}", 1)], n=5)),
        X("Since privatisation, {ind} prices have risen by {#x_p:40-70}%, while general prices rose by {#x_i:25-40}%. The companies paid {ncy}{#x_d:1-4}bn to shareholders last year. Investment in the network has risen, but {#x_c:10-25}% of customers say service is poor.",
          "Nationalisation would cost the government an estimated {ncy}{#x_cost:10-40}bn to buy the companies. Supporters say profits could be used to cut prices; critics point to long delays and losses when the industry was state-owned.",
          table=T("Figure 1: {ind} prices and general prices in {nation} (index, first year = 100)", [("{ind} prices", 100, "100+{x_p}*0.45", 1), ("General prices", 100, "100+{x_i}*0.45", 1)], n=5)),
    ],
    "growth": [
        X("Real GDP per person in {nation} is {ncy}{#x_y:4-9},000. Employment rose by {#x_j:150-400},000 last year. However, the richest 10% of households now receive {#x_r:35-45}% of income, up from {#x_r0:28-33}% ten years ago.",
          "Air quality in the capital exceeds safe limits on {#x_d:80-160} days a year. Hospital admissions for breathing problems have risen. Tax revenue has increased, and the government has used some of it to build {#x_s:200-600} new schools.",
          table=T("Figure 1: Economic growth and pollution in {nation}", [("Real GDP growth (%)", 3.1, "{g}", 1), ("Days with unsafe air quality", 60, "{x_d}", 0)], n=5)),
        X("Energy prices have risen by {#x_e:30-60}% in a year. Consumer spending fell by {#x_c:1-3}% in the last quarter, and business investment by {#x_i:3-7}%. Unemployment has risen to {=x_u:5.4|5.9|6.3}%.",
          "Inflation is currently {=x_inf:6.5|7.2|8.0}%, mainly because of energy and food costs. Some retailers have started offering discounts to attract customers, while others say their costs are still rising.",
          table=S("Figure 1: Real GDP growth and inflation in {nation} (%)", ["Quarter", "Real GDP growth", "Inflation"],
                  [["Q1", "0.5", "{#x_q1:4-5}.2"], ["Q2", "0.1", "{#x_q2:5-6}.4"], ["Q3", "–0.{#x_q3:2-6}", "{x_inf}"], ["Q4", "–{f}", "{#x_q4:5-6}.8"]])),
        X("{#x_pov:25-40}% of people in {nation} live on less than US\\$3 a day. Average life expectancy is {#x_le:60-68} years. Only {#x_sec:40-60}% of children complete secondary school.",
          "The government plans to spend {ncy}{#x_inv:1-4}bn on roads and ports. Foreign firms say high crime and unreliable power are bigger problems than taxes. Environmental groups warn about forest clearance for new mines.",
          table=T("Figure 1: Income per person in {nation} ({ncy} thousand)", [("Income per person ({ncy} thousand)", "{y}*0.85", "{y}", 2)], n=5)),
    ],
    "unemployment": [
        X("Unemployment is highest in former mining and steel towns in the north, at up to {#x_n:10-14}%, while in the capital it is {#x_c:2-4}%. Most vacancies are in technology, healthcare and construction. Average house prices in the capital are {#x_hp:3-5} times those in the north.",
          "The training programmes will cost {ncy}{#x_cost:200-600} million over three years and aim to retrain {#x_tr:30-80},000 people. Some economists say lower taxes for firms that move to the north would also help.",
          table=T("Figure 1: Unemployment rate and job vacancies in {nation}", [("Unemployment rate (%)", "{u}", "{u}", 1), ("Job vacancies (thousands)", "{v}*0.7", "{v}", 0)], n=4)),
        X("{#x_j:200-500},000 people have lost their jobs in the past year. The budget deficit is already {#x_d:4-7}% of GDP, and national debt is {#x_n:70-95}% of GDP. Interest rates are {#x_r:1-3}%.",
          "The government is considering a {ncy}{#x_sp:5-15}bn programme of spending on roads, schools and housing. Business confidence is at its lowest for {#x_y:5-10} years.",
          table=T("Figure 1: Unemployment in {nation} (%)", [("Unemployment rate (%)", "{u1}", "{u2}", 1)], n=5, labels=["Q1 last year", "Q2", "Q3", "Q4", "Q1 this year"])),
    ],
    "inflation": [
        X("Energy prices rose by {#x_e:25-45}% and food prices by {#x_f:12-20}%. Average wages rose by {#x_w:4-7}%. Pensioners and families on low incomes spend a larger share of their income on energy and food.",
          "Firms report higher costs for raw materials and transport. Some exporters say their goods are becoming less competitive abroad. Savings accounts pay an interest rate of {#x_r:2-4}%.",
          table=T("Figure 1: Inflation and wage growth in {nation} (%)", [("Inflation", 2.1, "{i}", 1), ("Wage growth", 2.5, "{x_w}", 1)], n=5)),
        X("Most of the rise in prices has come from imported fuel and food. Household debt is high, and about {#x_m:30-45}% of mortgages have variable interest rates. House sales fell by {#x_hs:10-20}% last quarter.",
          "Some economists say the government should also cut its own spending. Others argue that inflation caused by global energy prices will fall on its own once those prices stabilise.",
          table=T("Figure 1: Inflation and interest rates in {nation} (%)", [("Inflation", 2.4, "{i}", 1), ("Central bank interest rate", 0.5, "{r}", 2)], n=5)),
        X("Prices fell by {=x_d:0.6|1.1|1.5}% over the past year. Retail sales of cars and furniture fell by {#x_c:8-15}%. Wages are rising slowly, at about {#x_w:1-2}% a year.",
          "Some prices have fallen because of cheaper technology and lower world oil prices. Firms with large debts say falling prices make repayments harder. The central bank's interest rate is already {=x_r:0.1|0.25|0.5}%.",
          table=T("Figure 1: Inflation in {nation} (%)", [("Inflation rate (%)", 1.8, "-{x_d}", 1)], n=6)),
    ],
    "bop": [
        X("Imports of electronics and cars have risen by {#x_im:8-15}% a year. Exports of manufactured goods have fallen by {#x_ex:3-8}% a year, as firms in other countries have lower costs. The deficit is financed partly by foreign investors buying government bonds.",
          "The currency of {nation} has fallen by {#x_fx:5-12}% against the US dollar this year. Unemployment in manufacturing towns has risen to {#x_u:8-12}%.",
          table=T("Figure 1: Current account balance of {nation} (% of GDP)", [("Current account balance (% of GDP)", -1.5, "-{d}", 1)], n=6)),
        X("Exports of {ex} make up {#x_sh:50-75}% of export earnings. The currency has appreciated by {#x_a:8-15}% against the US dollar. Manufacturers outside the {ex} sector say they are losing sales abroad.",
          "The government has saved part of the export earnings in a national fund worth {ncy}{#x_f:50-200}bn. However, the price of {ex} has changed by up to 30% in a single year in the past.",
          table=T("Figure 1: Current account balance of {nation} ({ncy}bn)", [("Current account balance ({ncy}bn)", "{s}*0.3", "{s}", 1)], n=5)),
    ],
    "redistribution": [
        X("The top rate of income tax is {#x_t:30-40}% on incomes above {ncy}{#x_th:80-150},000. Raising it to {#x_t2:45-50}% would raise an estimated {ncy}{#x_r:1-3}bn a year. Benefits for low-income families are {ncy}{#x_b:40-80} a week per child.",
          "Some high earners say they may move abroad or reduce their working hours. Charities say the cost of rent and food has risen faster than benefits. The government could also spend more on free school meals and training.",
          table=T("Figure 1: Relative poverty in {nation} (% of people)", [("People in relative poverty (%)", "{p}-3", "{p}", 1)], n=5)),
        X("The sales tax raises {#x_s:55-70}% of government revenue. Low-income households spend about {#x_l:90-100}% of their income, while high-income households save about {#x_h:20-35}% of theirs.",
          "A proposal would introduce income tax rates of {#x_r1:0-5}%, {#x_r2:15-20}% and {#x_r3:30-40}% on different bands of income, and cut sales tax to {#x_ns:10-12}%. Tax advisers say a more complicated system may encourage avoidance.",
          table=S("Figure 1: Tax paid as a share of income in {nation}", ["Household income group", "Share of income paid in tax (%)"],
                  [["Lowest 20%", "{#x_q1:22-28}"], ["Middle 20%", "{#x_q3:18-22}"], ["Highest 20%", "{#x_q5:12-16}"]])),
    ],
    "environment": [
        X("Air pollution levels in the capital are {#x_x:3-6} times the World Health Organization guideline. Around {#x_d:10-30},000 deaths a year are linked to air pollution. Factories and power stations produce about {#x_f:55-70}% of emissions.",
          "The proposed carbon tax would be {ncy}{#x_t:20-60} per tonne of carbon dioxide. Factory owners warn this could raise prices and cost jobs. Regulations would need inspectors, and the clean technology subsidy would cost {ncy}{#x_s:1-3}bn.",
          table=T("Figure 1: Air pollution in the capital of {nation} (micrograms per cubic metre)", [("Average air pollution", 45, "45*{x_x}/3", 0)], n=6)),
        X("The {res} industry employs {#x_j:100-400},000 people, many in rural areas with few other jobs. Production has risen by {#x_p:30-60}% in ten years. Scientists estimate stocks could run out within {#x_y:15-30} years at current rates.",
          "Tourism, which depends on forests and coastline, earns {#x_tour:8-15}% of export earnings and is growing. Some buyers abroad now pay higher prices for {res} certified as sustainable.",
          table=T("Figure 1: Production of {res} in {nation} (index, first year = 100)", [("Production index", 100, "100+{x_p}", 0)], n=6)),
    ],
    "fiscal": [
        X("Interest payments on government debt now cost {ncy}{#x_i:5-15}bn a year, more than the education budget. Credit rating agencies have warned that the country's rating may be cut. Unemployment is {#x_u:5-8}%.",
          "The government plans to cut public spending by {#x_c:3-6}% and raise sales tax from {#x_s1:15-18}% to {#x_s2:19-21}%. Trade unions say cuts will hurt public services and those on low incomes.",
          table=T("Figure 1: Budget deficit and national debt in {nation} (% of GDP)", [("Budget deficit", 2.1, "{d}", 1), ("National debt", "{n}-12", "{n}", 0)], n=5)),
        X("The government expects the subsidies to create {#x_j:30-100},000 jobs within five years. {#x_f:6-15} new battery and solar panel factories are planned. The subsidies equal about {#x_pc:1-3}% of GDP.",
          "Other countries have complained to international trade bodies and threatened retaliation. Some economists say the money could have been spent on healthcare or used to reduce the deficit.",
          table=T("Figure 1: Electricity from renewable sources in {nation} (% of total)", [("Renewable share (%)", 12, 24, 0)], n=5)),
        X("Income tax raises {#x_it:30-40}% of revenue, sales tax {#x_st:30-40}% and business tax {#x_bt:15-25}%. The basic rate of income tax is {#x_r:20-25}% and sales tax is {#x_s:12-18}%. The health service needs an extra {ncy}{#x_h:2-6}bn a year.",
          "A 1 percentage point rise in income tax would raise {ncy}{#x_i1:1-2}bn; a 2 percentage point rise in sales tax would raise {ncy}{#x_s1:2-4}bn. Unions say sales tax hits the poor hardest, while business groups say higher income tax would reduce incentives to work.",
          table=None),
    ],
    "monetary": [
        X("Inflation has fallen from {#x_i0:9-12}% to {#x_i:5-7}%. House sales fell by {#x_hs:15-30}% in a year and mortgage repayments for a typical household have risen by {ccy}{#x_m:150-400} a month. Business investment fell by {#x_inv:3-7}%.",
          "The central bank's target is 2%. Unemployment has risen slightly to {#x_u:4-6}%. Higher interest rates have also attracted foreign savings, and the currency has appreciated by {#x_fx:4-10}%.",
          table=T("Figure 1: Interest rate and inflation in {nation} (%)", [("Interest rate", 1.0, "{r}", 2), ("Inflation", "{x_i0}", "{x_i}", 1)], n=5)),
        X("The central bank's interest rate is {=x_r:2.0|2.5|3.0}%. Household debt is high, and a survey found {#x_c:55-70}% of consumers are worried about losing their jobs. Banks have tightened lending rules.",
          "Business confidence is at its lowest level for {#x_y:5-10} years. Some economists say government spending would be more effective than cutting interest rates, but the government already has a budget deficit.",
          table=T("Figure 1: Unemployment and inflation in {nation} (%)", [("Unemployment", 5.1, "{u}", 1), ("Inflation", 2.6, "{i}", 1)], n=5)),
    ],
    "supply-side": [
        X("There are {#x_v:150-400},000 job vacancies, many for engineers, nurses and electricians. Output per worker in {nation} is {#x_p:15-30}% below the regional average. Around {#x_r:40-60}% of roads need repair.",
          "The education and training spending would take about {#x_y:5-10} years to show its full effect. The government will fund the spending by borrowing, adding to a national debt of {#x_d:60-90}% of GDP.",
          table=T("Figure 1: Unemployment and job vacancies in {nation}", [("Unemployment (%)", "{u}+0.4", "{u}", 1), ("Vacancies (thousands)", "{x_v}*0.7", "{x_v}", 0)], n=5)),
        X("Business tax is currently {#x_t:25-35}%, compared with {#x_n:15-22}% in neighbouring countries. Foreign direct investment into {nation} fell by {#x_f:10-25}% last year. Firms say it takes {#x_w:3-6} months to dismiss a worker.",
          "Cutting the tax rate by 5 percentage points would reduce revenue by an estimated {ncy}{#x_r:1-3}bn a year. Trade unions warn that fewer regulations could reduce job security and working conditions.",
          table=T("Figure 1: Foreign direct investment into {nation} ({ncy}bn)", [("FDI ({ncy}bn)", 12, "12*(1-{x_f}/100)", 1)], n=5)),
    ],
    "conflicts": [
        X("Wages rose by {#x_w:8-12}% last year as firms struggled to find workers. House prices rose by {#x_hp:10-18}%. The current account deficit widened to {#x_ca:4-7}% of GDP as consumers bought more imports.",
          "The central bank's inflation target is 2%. Some economists warn that if inflation becomes expected, it will be hard to reduce. Others say slowing growth now could cost thousands of jobs.",
          table=T("Figure 1: Macroeconomic data for {nation} (%)", [("Real GDP growth", 3.5, "{g}", 1), ("Unemployment", 6.0, "{u}", 1), ("Inflation", 2.5, "{i}", 1)], n=4)),
        X("The {ind} industry contributes {#x_g:10-20}% of GDP and employs {#x_j:200-600},000 people. The planned expansion would add an estimated {#x_add:1-2}% to GDP growth each year.",
          "Forests cover {#x_f:35-55}% of {nation}, down from {#x_f0:60-70}% thirty years ago. Tourism linked to forests and wildlife employs {#x_t:150-400},000 people. Rivers near existing sites have high levels of pollution.",
          table=T("Figure 1: Forest cover in {nation} (% of land area)", [("Forest cover (%)", "{x_f0}", "{x_f}", 0)], n=4, labels=["30 years ago", "20 years ago", "10 years ago", "Today"])),
    ],
    "globalisation": [
        X("Imports make up {#x_im:25-40}% of goods bought in {country}. The average price of clothing and electronics has fallen by {#x_p:10-25}% in real terms over ten years. Online purchases from foreign websites rose by {#x_on:15-30}% last year.",
          "However, {#x_f:20-40},000 manufacturing jobs have been lost in {country} over the same period. Some local brands have closed, and consumer groups have raised concerns about the quality and safety of some cheap imports.",
          table=T("Figure 1: World trade (US\\$ trillion)", [("Value of world trade", 19, 25, 1)], n=6)),
        X("The factory would employ {#x_j:2-5},000 workers directly and up to {#x_s:5-12},000 more in supplier firms. Tax breaks would cost the government about {ncy}{#x_t:50-200} million a year for ten years.",
          "Profits made by {firm} would mostly go to shareholders abroad. In a neighbouring country, a similar factory closed after eight years when tax breaks ended. Local firms say they would also like lower taxes.",
          table=None),
        X("Clothing makes up {#x_ex:60-80}% of {nation}'s exports. Average wages in the factories are about US\\${#x_w:90-150} a month, higher than in agriculture. A factory fire {=x_y:two|three|five} years ago killed {#x_d:40-120} workers.",
          "Some international brands have since agreed to safety inspections. Other countries in the region are now attracting clothing firms with even lower wages.",
          table=T("Figure 1: Clothing exports from {nation} (US\\$bn)", [("Clothing exports (US\\$bn)", 18, 34, 1)], n=6)),
    ],
    "trade": [
        X("{prod} makes up {#x_sh:50-80}% of export earnings. The world price of {prod} has varied between US\\${#x_lo:1-3},000 and US\\${#x_hi:4-6},000 per tonne over the past ten years. {nation} has good soil and climate for producing {prod}.",
          "Manufactured goods are mostly imported because local firms cannot match the prices of foreign producers. The government wants to diversify the economy into tourism and food processing.",
          table=T("Figure 1: Value of {prod} exports from {nation} ({ncy}bn)", [("Export value ({ncy}bn)", 4.2, 3.6, 2)], n=6)),
        X("Trade between the two countries is worth {ncy}{#x_t:5-20}bn a year. Farmers in {nation} have smaller farms and higher costs than farmers in the neighbouring country, where production per hectare is {#x_y:20-40}% higher.",
          "Manufacturers in {nation} expect exports to rise by {#x_e:10-20}% within three years. The government will lose about {ncy}{#x_r:200-800} million a year in tariff revenue.",
          table=None),
    ],
    "protection": [
        X("Imports of {prod} have risen from {#x_i0:15-25}% to {#x_i1:45-60}% of the domestic market in five years. The quota limits imports to {#x_q:100-300},000 tonnes a year. Domestic producers employ about {#x_j:30-80},000 people.",
          "Since the quota was announced, the domestic price of {prod} has risen by {#x_p:8-15}%. The main exporting country has said it may place tariffs on goods from {nation} in response.",
          table=T("Figure 1: Imports of {prod} as a share of the market in {nation} (%)", [("Import share (%)", "{x_i0}", "{x_i1}", 0)], n=6)),
        X("{nation} has a population of {#x_pop:5-30} million. Exports to the free trade area were {ncy}{#x_e:2-8}bn last year. Firms from larger countries in the area have average costs up to {#x_c:15-30}% lower than firms in {nation}.",
          "Membership also allows workers to move freely between countries. Some young skilled workers from {nation} may move abroad for higher wages, but foreign firms may also invest in {nation}.",
          table=None),
        X("Imports of {prod} rose by {#x_r:30-60}% in two years. The domestic {prod} industry employs {#x_j:20-60},000 workers. Firms that use {prod}, such as builders and machine makers, employ about {#x_u:200-500},000 people.",
          "Since the tariff was introduced, the price of {prod} in {nation} has risen by {#x_p:10-20}%. The main exporting country has threatened retaliatory tariffs on {nation}'s exports of food.",
          table=T("Figure 1: Imports of {prod} into {nation} (thousand tonnes)", [("Imports (thousand tonnes)", 400, "400*(1+{x_r}/100)", 0)], n=4)),
    ],
    "exchange": [
        X("Fuel and food make up {#x_ff:25-40}% of imports. Exports are worth {#x_x:20-35}% of GDP. Inflation has risen from {#x_i0:2-3}% to {#x_i:5-8}% since the depreciation began.",
          "Tour operators report a {#x_t:10-20}% rise in bookings from abroad. Firms with loans in US dollars say repayments have become more expensive.",
          table=T("Figure 1: Value of {nation}'s currency (units per US\\$1)", [("Units per US\\$1", 10.0, "10*(1+{d}/100)", 2)], n=5)),
        X("Interest rates in {nation} are now {#x_r:5-7}%, higher than in most trading partners. Imports have become cheaper and inflation has fallen to {#x_i:2-4}%.",
          "Exporters of manufactured goods report falling orders, and some have cut jobs. Foreign investors bought {ncy}{#x_f:5-15}bn of government bonds last year.",
          table=T("Figure 1: Exchange rate and exports of {nation}", [("Units of currency per US\\$1", 8.0, "8/(1+{a}/100)", 2), ("Exports ({ncy}bn)", 52, 48, 1)], n=5)),
        X("Exports make up {#x_x:30-50}% of GDP. Around {#x_s:60-80}% of exporters are small firms that cannot afford to protect themselves against currency changes. The central bank holds {ncy}{#x_res:5-20}bn of foreign currency reserves.",
          "Intervening would use these reserves, and some economists say the central bank cannot hold the rate for long if markets disagree. Others say a stable currency would encourage foreign investment.",
          table=S("Figure 1: Monthly change in the value of {nation}'s currency against the US\\$ (%)", ["Month", "Change (%)"],
                  [["January", "+{#x_m1:2-5}"], ["February", "–{v}"], ["March", "+{#x_m3:3-8}"], ["April", "–{#x_m4:2-6}"], ["May", "+{#x_m5:1-4}"]])),
    ],
    # supplementary intervention issues (economics_kbint): regulation, permits
    "intervention-pol": [
        X("About {#x_f:30-60} factories discharge waste into the river. Fish stocks have fallen by {#x_fish:40-60}% in ten years, and water companies spend {ncy}{#x_w:10-30} million a year cleaning water for drinking.",
          "Under the permit scheme, factories that cut waste cheaply could sell spare permits to others. Fines would be {ncy}{#x_fine:5-50},000 per breach, but the environment agency has only {#x_ins:10-30} inspectors.",
          table=T("Figure 1: Fish stocks in the river near {ncity} (index, first year = 100)", [("Fish stock index", 100, "100-{x_fish}", 0)], n=6)),
        X("About {#x_old:20-35}% of cars driving into the city centre would be banned. Air pollution near main roads is {#x_x:2-4} times the safe limit. Public transport carries {#x_pt:30-45}% of journeys into the centre.",
          "Shopkeepers fear fewer customers. Low-income drivers own a larger share of older cars, and an electric car costs about {ncy}{#x_ev:20-35},000 even with the grant.",
          table=T("Figure 1: Air pollution near main roads in {ncity} (micrograms per cubic metre)", [("Average air pollution", 52, 60, 0)], n=5)),
    ],
}


def extend(key, idx, ctx_text, c, r_seed):
    """Return (paragraphs, table_or_None) for issue `idx` of subtopic `key`."""
    items = EXT.get(key)
    if not items or idx >= len(items):
        return [], None
    x = items[idx]
    rx = rng_for(key, str(idx), ctx_text, r_seed)
    paras = [fill(p, c, rx) for p in x["paras"]]
    tbl = x["table"](c, rx) if x["table"] else None
    return paras, tbl
