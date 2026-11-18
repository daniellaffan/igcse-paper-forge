"""Direction fixes for extended-writing items: indicative content that matches what each prompt asks.

a_points: AO2/AO3 content for the analyse prompt (used instead of `pro`).
j_pro / j_con: AO2/AO3 and AO4 content for the assess/evaluate prompt (used instead of `pro` / `con`).
Keys are (subtopic key, issue number starting at 1). All wording is original.
"""

FIX = {
    ("bop", 1): dict(
        a_points=["Strong demand for imported electronics and cars means more money flows out on the current account",
                  "Falling exports mean less money flows in from abroad",
                  "Exports may be uncompetitive because of high production costs or low quality compared with foreign goods",
                  "A strong exchange rate makes exports dearer abroad and imports cheaper at home",
                  "Rising incomes in {nation} raise spending on imports faster than foreign demand for its exports grows"],
        j_pro=["A deficit of {d}% of GDP must be financed by borrowing from abroad or selling assets, increasing foreign debt",
               "Spending on imports is a leakage, so demand for domestic output and jobs is lower",
               "Export industries may shrink, causing structural unemployment",
               "Pressure on the currency may lead to depreciation, raising import prices and inflation",
               "Foreign currency reserves may run down, making the economy vulnerable"]),
    ("inflation", 1): dict(
        a_points=["Rising energy and food prices raise firms' costs, causing cost-push inflation",
                  "Higher import prices feed through into the prices of many goods",
                  "Workers demand higher wages to keep up with prices, raising costs again (wage-price spiral)",
                  "Strong consumer spending relative to output may add demand-pull pressure",
                  "Expectations of further price rises lead firms to raise prices in advance"],
        j_pro=["Inflation of {i}% reduces real incomes if wages rise more slowly than prices",
               "Savers lose because the real value of their savings falls",
               "Firms face menu costs and uncertainty, which can reduce investment",
               "Exports from {nation} become less price competitive",
               "Low-income households suffer most because necessities make up a large share of their spending"]),
    ("competition", 3): dict(
        j_pro=["Local shops face lower prices from the online rival, so their revenue and profit margins fall",
               "Some firms close: {c}% of shops in the centre have shut",
               "Surviving firms must cut costs, improve service or move online to compete",
               "The online retailer gains market share and economies of scale",
               "Firms are pushed to innovate, for example with click-and-collect or loyalty schemes"],
        j_con=["Efficient local shops may gain customers as weaker rivals close",
               "Shops offering personal service or products that are hard to buy online are less affected",
               "Falling demand for city-centre property may reduce rents, lowering costs for remaining firms",
               "The impact depends on how quickly firms adapt and on the type of product sold"]),
    ("government", 1): dict(
        a_points=["Private owners aim to make a profit, so they may cut labour costs",
                  "Some workers at the airport may lose their jobs or face less secure contracts",
                  "Pay and conditions may be reduced, which explains union opposition",
                  "Productive workers may gain if new owners invest and offer bonuses or training",
                  "If the airport expands to attract more passengers, new jobs may be created"]),
    ("costs", 3): dict(
        j_pro=["{firm} could raise prices; if demand is price inelastic, total revenue rises",
               "It could cut costs, for example by finding cheaper suppliers or using less energy",
               "Increasing productivity lowers average costs",
               "Growing sales could bring economies of scale such as bulk-buying discounts",
               "It could stop selling loss-making products and focus on the most profitable lines"]),
    ("globalisation", 3): dict(
        a_points=["Low wages keep workers' living standards down even though {w} million people are employed",
                  "Poor working conditions and long hours may harm workers' health and productivity",
                  "{nation} depends on foreign brands that could move orders to cheaper countries, causing sudden job losses",
                  "Most profit flows to foreign owners, so less income stays in {nation} to be spent or invested",
                  "Textile production can pollute rivers and land, creating external costs for local communities"]),
    ("growth", 2): dict(
        j_pro=["Lower consumer spending reduces demand-pull inflation",
               "Rising unemployment weakens wage growth, so cost pressures ease",
               "Firms may cut prices to sell unsold stock",
               "Lower demand for imports and raw materials may reduce cost-push pressure"]),
    ("growth", 3): dict(
        j_pro=["Growth creates jobs and reduces unemployment", "Higher incomes raise living standards and reduce poverty",
               "More tax revenue funds public services without raising tax rates", "Firms gain confidence and invest more"]),
    ("unemployment", 1): dict(
        a_points=["Vacancies existing alongside unemployment suggest a skills mismatch (structural unemployment)",
                  "Decline of older industries leaves workers with skills that are no longer demanded",
                  "Workers may be unable to move to areas where jobs are available (geographical immobility)",
                  "Lower demand in the economy may cause cyclical unemployment",
                  "Some workers are between jobs while they search (frictional unemployment)"]),
    ("unemployment", 2): dict(
        j_pro=["Higher government spending raises demand, so firms need more workers",
               "Spending on infrastructure creates jobs directly in construction",
               "Extra income is spent again, so the effect on demand is multiplied",
               "Lower unemployment reduces spending on benefits and raises tax revenue over time"]),
    ("redistribution", 1): dict(
        j_pro=["Higher taxes on the rich raise revenue to fund benefits for the {p}% in relative poverty",
               "Progressive taxes narrow the gap between after-tax incomes",
               "Richer households save more of their income, so total spending falls only a little",
               "Revenue can fund education and healthcare that help poorer families"]),
    ("environment", 1): dict(
        a_points=["Air pollution is a negative externality that harms third parties", "Illness raises healthcare costs for the government and households",
                  "Workers' productivity falls through illness and days off work", "Tourism may fall, reducing income and jobs",
                  "Damage to crops and buildings raises costs for firms"],
        j_pro=["A carbon or pollution tax makes polluters pay and raises revenue", "Regulation sets legal limits that act directly on emissions",
               "Subsidies for clean energy and public transport encourage cleaner choices", "Pollution permits cap total emissions while letting firms trade"]),
    ("fiscal", 1): dict(
        a_points=["A higher sales tax raises prices, reducing consumers' real incomes", "Cuts to public services harm users of health and education",
                  "Lower disposable income reduces consumer spending", "Low-income consumers are hit hardest because sales tax is regressive"],
        j_pro=["A smaller deficit reduces future interest payments on debt of {n}% of GDP", "Lower borrowing may improve confidence among lenders and firms",
               "Reducing demand may help bring inflation down", "Less debt now means less need for higher taxes in future"]),
    ("trade", 2): dict(
        a_points=["Manufacturers gain access to a larger market", "Cheaper imported inputs lower firms' costs",
                  "Selling more allows firms to gain economies of scale", "Competition encourages firms to become more efficient and innovative"]),
    ("pes", 2): dict(
        j_pro=["When demand rises, inelastic supply means prices rise sharply while the number of homes changes little",
               "Housing becomes less affordable, especially for first-time buyers and renters",
               "Shortages may lead to overcrowding and longer waiting lists",
               "Existing owners and landlords gain from rising prices, widening inequality"]),
    ("productivity", 2): dict(
        j_pro=["Spending on education and training raises workers' skills", "Better infrastructure cuts firms' transport costs and wasted time",
               "Grants or tax relief for investment in machinery raise capital per worker", "Support for research spreads new technology"],
        j_con=["These policies are expensive and have an opportunity cost", "Training takes years to raise productivity",
               "Firms may not invest even with support if demand is weak", "Success depends on matching skills to what employers need"]),
    ("objectives", 2): dict(
        j_pro=["Economies of scale may lower costs, which could be passed on as lower prices",
               "A larger firm may invest more in new products", "Removing duplicated costs could make the firm more efficient",
               "A stronger firm may be more reliable and offer a wider range"]),
    ("labour", 1): dict(
        a_points=["Low-paid workers who keep their jobs receive {ncy}{mw} per hour, increasing their income",
                  "Higher incomes reduce poverty and inequality and may raise workers' motivation and productivity",
                  "Higher pay may attract more people into the labour force",
                  "If the minimum wage is above the equilibrium wage, the supply of labour exceeds demand, so some workers become unemployed",
                  "Small firms in retail and hospitality may cut staff or reduce workers' hours, so some workers' weekly pay may fall",
                  "Firms may replace workers with machines or cut training and other benefits to offset higher wage costs"]),
    ("scale", 2): dict(
        j_pro=["Decentralising decisions to local managers can speed up decisions", "Better communication systems reduce mistakes between layers",
               "Smaller teams with clear targets can improve morale and productivity", "Incentives such as bonuses can motivate the {b} staff"],
        j_con=["Decentralisation may lead to inconsistent decisions", "New IT systems are costly", "Restructuring can lower morale in the short run",
               "Some diseconomies may be hard to avoid at this size"]),
}


def apply(KB):
    for (k, n), extra in FIX.items():
        KB[k]["issues"][n - 1].update(extra)
