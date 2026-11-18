"""Simplified 4EC1 specification tree + paper structure for the economics generator.

Summaries are our own one-line paraphrases. Reference numbers follow the 4EC1 content
numbering (topic.subtopic.point); see docs/notes/economics.md for the caveat on verification.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

QTYPES = [
    {"id": "mcq", "label": "Multiple choice", "marks": "1", "description": "One correct answer from four options (A-D)."},
    {"id": "state", "label": "State / identify", "marks": "1", "description": "Give one fact, example or feature; no development needed."},
    {"id": "define", "label": "Define / What is meant by", "marks": "1-2", "description": "Precise definition of a key term (1 mark Define, 2 marks What is meant by)."},
    {"id": "describe", "label": "Describe", "marks": "2", "description": "One point plus one linked development."},
    {"id": "calculate", "label": "Calculate", "marks": "2", "description": "Numerical answer with working and correct units."},
    {"id": "diagram", "label": "Draw / label a diagram", "marks": "3", "description": "Draw a shift or curve on the axes given, or label a diagram."},
    {"id": "explain", "label": "Explain", "marks": "3", "description": "Identify, develop and apply one reason, effect or advantage to the context."},
    {"id": "analyse", "label": "Analyse (6 marks)", "marks": "6", "description": "One-sided developed chains of reasoning using the data; levels marked AO2/AO3."},
    {"id": "assess", "label": "Assess (9 marks)", "marks": "9", "description": "Analysis plus counter-argument; levels marked AO2/AO3/AO4."},
    {"id": "evaluate", "label": "Evaluate (12 marks)", "marks": "12", "description": "Balanced argument with a supported judgement; levels marked AO2/AO3/AO4."},
    {"id": "data-response", "label": "Data response (Question 4 style)", "marks": "20", "description": "Data table and extract with a calculation, a 6-mark analyse and a 12-mark evaluate."},
]

A = ["mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"]


def q(*names):
    return [n for n in A if n in names]


# topic id, ref, title, paper, [subtopics: (id, ref, title, summary, qtypes, [(ref, summary)])]
TOPICS = [
    ("market-system", "1", "The market system", "p1", [
        ("economic-problem", "1.1", "The economic problem", "Why scarcity forces choices, the four factors of production and their rewards, and opportunity cost.",
         q("mcq", "state", "define", "describe", "explain", "analyse"),
         [("1.1.1", "Wants are unlimited but resources are finite, so societies must decide what, how and for whom to produce."),
          ("1.1.2", "Land, labour, capital and enterprise, the reward each earns (rent, wages, interest, profit) and how their quantity and quality can change."),
          ("1.1.3", "The next best alternative given up when a choice is made, for consumers, workers, firms and governments.")]),
        ("ppc", "1.1.4", "Production possibility curves", "Drawing and interpreting PPCs: efficiency, opportunity cost, and shifts caused by growth or loss of resources.",
         q("mcq", "define", "calculate", "diagram", "explain"),
         [("1.1.4", "Use a PPC to show efficient, inefficient and unattainable output, the opportunity cost of moving along it and causes of shifts.")]),
        ("assumptions", "1.2", "Economic assumptions", "What economists assume each economic agent is trying to achieve.",
         q("mcq", "state", "describe", "explain"),
         [("1.2.1", "Consumers aim to maximise satisfaction, workers their rewards, firms their profits and governments the welfare of society.")]),
        ("demand", "1.3", "Demand", "The demand curve, movements along it and the factors that shift it.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse"),
         [("1.3.1", "Demand slopes downwards; a price change causes a movement along the curve (extension or contraction)."),
          ("1.3.2", "Income, prices of substitutes and complements, tastes, advertising, population and other non-price factors shift demand.")]),
        ("supply", "1.4", "Supply", "The supply curve, movements along it and the factors that shift it.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse"),
         [("1.4.1", "Supply slopes upwards; a price change causes a movement along the curve (extension or contraction)."),
          ("1.4.2", "Costs of production, technology, weather, indirect taxes, subsidies and the number of firms shift supply.")]),
        ("price", "1.5", "Price and market equilibrium", "How the interaction of demand and supply sets the equilibrium price and how it changes.",
         q("mcq", "define", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("1.5.1", "Equilibrium is where quantity demanded equals quantity supplied; excess demand and excess supply push price towards it."),
          ("1.5.2", "Shifts in demand and/or supply change the equilibrium price and quantity, shown on a diagram."),
          ("1.5.3", "Price acts as a signal and an incentive that allocates scarce resources.")]),
        ("ped", "1.6", "Price and income elasticity of demand", "Measuring how responsive demand is to price and income changes, what affects it and why firms and governments care.",
         q("mcq", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("1.6.1", "PED = % change in quantity demanded / % change in price; interpret elastic, inelastic, unitary, perfectly elastic and perfectly inelastic values."),
          ("1.6.2", "Substitutes, necessity versus luxury, share of income, habit and time period affect PED."),
          ("1.6.3", "How PED links price changes to total revenue, and its use by firms and governments (e.g. choosing what to tax)."),
          ("1.6.4", "YED = % change in quantity demanded / % change in income; normal and inferior goods.")]),
        ("pes", "1.7", "Price elasticity of supply", "Measuring how responsive supply is to a price change and why it differs between products.",
         q("mcq", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess"),
         [("1.7.1", "PES = % change in quantity supplied / % change in price; elastic and inelastic supply."),
          ("1.7.2", "Time, spare capacity, stocks, availability of factors and the production process affect PES.")]),
        ("mixed", "1.8", "The mixed economy", "How markets and the state share the job of allocating resources, and public goods.",
         q("mcq", "state", "define", "describe", "explain", "analyse", "assess", "evaluate"),
         [("1.8.1", "The roles of the private and public sectors in a mixed economy and the strengths and weaknesses of markets."),
          ("1.8.2", "Public goods are non-rival and non-excludable, causing the free-rider problem; why the state provides them.")]),
        ("intervention", "1.8.3", "Government intervention in markets", "How taxes, subsidies, maximum and minimum prices and state provision change market outcomes.",
         q("mcq", "define", "calculate", "diagram", "explain", "analyse", "assess", "evaluate"),
         [("1.8.3", "Indirect taxes, subsidies, maximum and minimum prices, regulation and state provision; their effects shown on diagrams and their drawbacks.")]),
        ("externalities", "1.9", "Externalities", "Costs and benefits that spill over to third parties and how governments respond.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("1.9.1", "Private, external and social costs and benefits; social = private + external."),
          ("1.9.2", "Negative and positive externalities of production and consumption."),
          ("1.9.3", "Taxes, subsidies, fines, regulation, bans, education and information used to correct externalities, and their limitations.")]),
    ]),
    ("business", "2", "Business economics", "p1", [
        ("production", "2.1", "Production and the sectors of the economy", "What production means and how output and jobs are split between primary, secondary and tertiary sectors.",
         q("mcq", "state", "define", "describe", "explain", "analyse"),
         [("2.1.1", "Production adds value by turning inputs into goods and services."),
          ("2.1.2", "Primary, secondary and tertiary sectors and the reasons their share of an economy changes over time.")]),
        ("productivity", "2.2", "Productivity and division of labour", "Output per input, what raises it, and the gains and costs of specialisation.",
         q("mcq", "define", "describe", "calculate", "explain", "analyse", "assess"),
         [("2.2.1", "Labour productivity = output / number of workers (or hours); factors that raise productivity."),
          ("2.2.2", "Division of labour and specialisation: advantages and disadvantages for workers, firms and consumers.")]),
        ("costs", "2.3", "Business costs, revenue and profit", "Fixed, variable, total and average costs, revenue and profit calculations and what they mean for firms.",
         q("mcq", "define", "calculate", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("2.3.1", "Fixed, variable, total and average costs and how to calculate them."),
          ("2.3.2", "Total and average revenue; profit = total revenue - total costs; loss."),
          ("2.3.3", "How changes in costs and revenue affect a firm's decisions.")]),
        ("objectives", "2.4", "Business objectives and the growth of firms", "Why firms have different aims, why some grow and others stay small, and the ways they grow.",
         q("mcq", "state", "define", "describe", "explain", "analyse", "assess", "evaluate"),
         [("2.4.1", "Profit maximisation, sales and growth, survival, market share and social or environmental objectives; owners and managers may differ."),
          ("2.4.2", "Organic growth and external growth (horizontal, vertical and conglomerate mergers and takeovers)."),
          ("2.4.3", "Reasons why firms grow (spreading risk, economies of scale, market power) and why some stay small.")]),
        ("scale", "2.5", "Economies and diseconomies of scale", "Why average costs fall and then rise as a firm grows.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess"),
         [("2.5.1", "Internal economies of scale: purchasing, technical, financial, managerial, marketing, risk-bearing."),
          ("2.5.2", "External economies of scale from the growth of the industry or area."),
          ("2.5.3", "Diseconomies of scale: communication, coordination and motivation problems; the average cost curve.")]),
        ("competition", "2.6", "Business competition and market structure", "Competitive markets, monopoly and oligopoly and what each means for consumers.",
         q("mcq", "state", "define", "describe", "explain", "analyse", "assess", "evaluate"),
         [("2.6.1", "Features of competitive markets and the benefits of competition for consumers and firms."),
          ("2.6.2", "Monopoly: one dominant firm, price maker, high barriers to entry; advantages and disadvantages."),
          ("2.6.3", "Oligopoly: a few large interdependent firms, branding, non-price competition and the risk of collusion.")]),
        ("labour", "2.7", "The labour market", "How wages are set by the demand for and supply of labour and how unions and minimum wages affect them.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("2.7.1", "Demand for labour is derived demand; factors that shift the demand for and supply of labour."),
          ("2.7.2", "Wage determination on a diagram and reasons why wages differ between occupations."),
          ("2.7.3", "Trade unions and collective bargaining; the national minimum wage and its effects.")]),
        ("government", "2.8", "Government and firms", "Privatisation, nationalisation and the regulation of business behaviour.",
         q("mcq", "define", "describe", "explain", "analyse", "assess", "evaluate"),
         [("2.8.1", "Privatisation and nationalisation: meaning, reasons and effects on consumers, workers and government."),
          ("2.8.2", "Regulation of firms and monopolies to protect consumers and promote competition.")]),
    ]),
    ("government", "3", "Government and the economy", "p2", [
        ("growth", "3.1.1", "Economic growth", "Measuring growth with GDP, the economic cycle, and the causes, benefits and costs of growth.",
         q("mcq", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("3.1.1", "GDP and real GDP, GDP per capita, growth rates, the economic cycle (boom, recession, slump, recovery), causes, benefits and costs of growth.")]),
        ("unemployment", "3.1.2", "Employment and unemployment", "Measuring unemployment, its types and causes, and its costs.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("3.1.2", "Unemployment rate, claimant count and labour force survey; frictional, structural, cyclical and seasonal unemployment; costs for individuals, firms and government.")]),
        ("inflation", "3.1.3", "Inflation", "Measuring changes in the price level, the causes of inflation and who gains or loses.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("3.1.3", "Consumer price index, demand-pull and cost-push inflation, deflation, and effects on consumers, savers, firms and competitiveness.")]),
        ("bop", "3.1.4", "Balance of payments", "The current account, why a country may have a deficit or surplus and the consequences.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess"),
         [("3.1.4", "Trade in goods and services, primary and secondary income, current account deficit and surplus, causes and consequences.")]),
        ("redistribution", "3.1.5", "Redistribution of income", "Why incomes are unequal, absolute and relative poverty, and how governments redistribute.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess"),
         [("3.1.5", "Causes of inequality, absolute and relative poverty, progressive, proportional and regressive taxes, benefits and the effects of redistribution.")]),
        ("environment", "3.1.6", "Protection of the environment", "How economic activity damages the environment and why protecting it is a government objective.",
         q("mcq", "state", "define", "describe", "explain", "analyse", "assess"),
         [("3.1.6", "Pollution, resource depletion and climate change from business activity; sustainable growth; policies such as taxes, regulation and subsidies for clean technology.")]),
        ("fiscal", "3.2.1", "Fiscal policy", "Using taxation and government spending to influence the economy, and the government budget.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("3.2.1", "Direct and indirect taxes, government spending, budget deficit and surplus, national debt, expansionary and contractionary fiscal policy and their effects.")]),
        ("monetary", "3.2.2", "Monetary policy", "How the central bank uses interest rates and the money supply to meet macroeconomic objectives.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess", "evaluate"),
         [("3.2.2", "Interest rates, money supply and the exchange rate as monetary tools; effects on spending, borrowing, saving, inflation and growth.")]),
        ("supply-side", "3.2.3", "Supply-side policies", "Policies that raise the productive capacity of the economy.",
         q("mcq", "state", "define", "describe", "explain", "analyse", "assess", "evaluate"),
         [("3.2.3", "Education and training, infrastructure, tax incentives, deregulation, privatisation and labour market reforms; their benefits, costs and time lags.")]),
        ("conflicts", "3.3", "Relationships between objectives", "Why governments face trade-offs between macroeconomic objectives.",
         q("mcq", "describe", "explain", "analyse", "assess", "evaluate"),
         [("3.3.1", "Trade-offs such as growth versus inflation, unemployment versus inflation, growth versus the environment and growth versus the current account.")]),
    ]),
    ("global", "4", "The global economy", "p2", [
        ("globalisation", "4.1", "Globalisation", "The growing interconnection of economies, multinational corporations and foreign direct investment.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess", "evaluate"),
         [("4.1.1", "Meaning and causes of globalisation (transport, communications, trade liberalisation)."),
          ("4.1.2", "Multinational corporations and FDI: advantages and disadvantages for host countries, consumers, workers and firms.")]),
        ("trade", "4.2.1", "International trade", "Why countries specialise and trade, and the gains and risks of free trade.",
         q("mcq", "state", "define", "describe", "calculate", "explain", "analyse", "assess"),
         [("4.2.1", "Specialisation, imports and exports, free trade and its benefits and drawbacks for consumers, producers and economies.")]),
        ("protection", "4.2.2", "Protectionism and trading blocs", "Tariffs, quotas and subsidies, free trade areas, customs unions and the WTO.",
         q("mcq", "state", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("4.2.2", "Tariffs, quotas, subsidies to domestic firms and other barriers: reasons, diagrams and consequences."),
          ("4.2.3", "Free trade areas, customs unions, common markets and the role of the World Trade Organization.")]),
        ("exchange", "4.3", "Exchange rates", "How floating exchange rates are set, why they change and the effects of appreciation and depreciation.",
         q("mcq", "define", "describe", "calculate", "diagram", "explain", "analyse", "assess", "evaluate", "data-response"),
         [("4.3.1", "Demand for and supply of a currency on a diagram; causes of appreciation and depreciation."),
          ("4.3.2", "Effects of exchange-rate changes on exporters, importers, consumers, inflation and the current account; currency calculations.")]),
    ]),
]


# ---- Official 4EC1 numbering (checked against the specification, Issue 3).
# Topic areas are 1.1, 1.2 (Paper 1) and 2.1, 2.2 (Paper 2); content sections are x.x.x and
# learning points are lettered, written here as e.g. "1.1.3(a)". Summaries are our own words.
TOPIC_REFS = {"market-system": ("1.1", "The market system"), "business": ("1.2", "Business economics"),
              "government": ("2.1", "Government and the economy"), "global": ("2.2", "The global economy")}

OFFICIAL = {
    "economic-problem": ("1.1.1", [("1.1.1(a)", "Scarcity: unlimited wants and finite resources force choices."),
                                   ("1.1.1(b)", "Opportunity cost for consumers, producers and government."),
                                   ("1.2.1(a)", "The four factors of production.")]),
    "ppc": ("1.1.1", [("1.1.1(c)", "Drawing production possibility curves."),
                      ("1.1.1(d)", "Using the PPC to show potential output, unused resources, opportunity cost, shifts and unattainable points."),
                      ("1.1.1(e)", "What causes an economy to grow or shrink.")]),
    "assumptions": ("1.1.2", [("1.1.2(a)", "The assumed aims of consumers and businesses."),
                              ("1.1.2(b)", "Why consumers may not get the most benefit from their choices."),
                              ("1.1.2(c)", "Why producers may not aim purely for maximum profit.")]),
    "demand": ("1.1.3", [("1.1.3(a)", "What demand means."), ("1.1.3(b)", "Movements along and shifts of the demand curve."),
                         ("1.1.3(c)", "Non-price factors that shift demand.")]),
    "supply": ("1.1.3", [("1.1.3(d)", "What supply means."), ("1.1.3(e)", "Movements along and shifts of the supply curve."),
                         ("1.1.3(f)", "Non-price factors that shift supply.")]),
    "price": ("1.1.3", [("1.1.3(g)", "How equilibrium price and quantity are set."),
                        ("1.1.3(h)", "Diagrams of shifts, excess demand and excess supply."),
                        ("1.1.3(i)", "Defining, calculating and drawing excess demand and supply."),
                        ("1.1.3(j)", "How market forces clear a shortage or surplus.")]),
    "ped": ("1.1.4", [("1.1.4(a)", "Meaning of PED."), ("1.1.4(b)", "The PED formula."), ("1.1.4(c)", "Calculating PED from percentage changes."),
                      ("1.1.4(d)", "Diagrams of elastic and inelastic demand."), ("1.1.4(e)", "Interpreting PED values."),
                      ("1.1.4(f)", "What makes demand more or less price elastic."), ("1.1.4(g)", "PED and total revenue."),
                      ("1.1.4(o)", "Meaning of YED."), ("1.1.4(p)", "The YED formula."), ("1.1.4(q)", "Calculating YED."),
                      ("1.1.4(r)", "Interpreting YED for luxury, normal and inferior goods."),
                      ("1.1.4(s)", "Why elasticities matter to firms and government.")]),
    "pes": ("1.1.4", [("1.1.4(h)", "Meaning of PES."), ("1.1.4(i)", "The PES formula."), ("1.1.4(j)", "Calculating PES."),
                      ("1.1.4(k)", "Diagrams of elastic and inelastic supply."), ("1.1.4(l)", "Interpreting PES values."),
                      ("1.1.4(m)", "What makes supply more or less price elastic."), ("1.1.4(n)", "Likely PES of manufactured versus primary goods.")]),
    "mixed": ("1.1.5", [("1.1.5(a)", "Meaning of a mixed economy."), ("1.1.5(b)", "Public and private sectors."),
                        ("1.1.5(c)", "How the two sectors differ in ownership, control and aims."),
                        ("1.1.5(d)", "How a mixed economy answers what, how and for whom."),
                        ("1.1.5(e)", "Market failure as a misallocation of resources."), ("1.1.5(f)", "Why market failure may justify intervention."),
                        ("1.1.5(g)", "Public goods and the free-rider problem."), ("1.1.5(h)", "Roles of each sector in production."),
                        ("1.1.5(i)", "How the balance between sectors varies across economies.")]),
    "intervention": ("1.2.6", [("1.2.6(a)", "Policies to correct externalities (taxes, subsidies, fines, regulation, permits)."),
                               ("1.2.6(b)", "Strengths and weaknesses of each policy.")]),
    "externalities": ("1.1.6", [("1.1.6(a)", "Meaning of external costs."), ("1.1.6(b)", "Examples of external costs."),
                                ("1.1.6(c)", "Meaning of external benefits."), ("1.1.6(d)", "Examples of external benefits."),
                                ("1.1.6(e)", "Social cost and social benefit formulae.")]),
    "production": ("1.2.1", [("1.2.1(a)", "The four factors of production."), ("1.2.1(b)", "Primary, secondary and tertiary sectors."),
                             ("1.2.1(c)", "How the sectors' shares of jobs and output change as economies develop.")]),
    "productivity": ("1.2.2", [("1.2.2(a)", "Meaning of productivity."), ("1.2.2(b)", "What raises the productivity of land, labour and capital."),
                               ("1.2.2(c)", "Meaning of division of labour."), ("1.2.2(d)", "Gains and drawbacks of division of labour.")]),
    "costs": ("1.2.3", [("1.2.3(a)", "Revenue, cost and profit formulae and calculations.")]),
    "objectives": ("1.2.4", [("1.2.4(b)", "Pros and cons of large and small firms."), ("1.2.4(c)", "What drives firms to grow."),
                             ("1.2.4(d)", "Why some firms stay small.")]),
    "scale": ("1.2.3", [("1.2.3(b)", "Internal and external economies of scale."),
                        ("1.2.3(c)", "Diseconomies of scale and the LRAC curve.")]),
    "competition": ("1.2.4", [("1.2.4(a)", "Effects of competition on firms, consumers and the economy."),
                              ("1.2.4(e)", "Meaning of monopoly."), ("1.2.4(f)", "Features of monopoly, including barriers to entry."),
                              ("1.2.4(g)", "Pros and cons of monopoly."), ("1.2.4(h)", "Meaning of oligopoly."),
                              ("1.2.4(i)", "Features of oligopoly."), ("1.2.4(j)", "Pros and cons of oligopoly.")]),
    "labour": ("1.2.5", [("1.2.5(a)", "What affects the demand for labour."), ("1.2.5(b)", "What affects the supply of labour."),
                         ("1.2.5(c)", "Why labour quantity and quality matter to firms."), ("1.2.5(d)", "Education, training and human capital."),
                         ("1.2.5(e)", "Labour market diagrams and shifts."), ("1.2.5(f)", "The role of trade unions."),
                         ("1.2.6(d)", "Minimum wages and their effects.")]),
    "government": ("1.2.6", [("1.1.5(j)", "Meaning of privatisation."), ("1.1.5(k)", "Who gains and loses from privatisation."),
                             ("1.2.6(c)", "Regulating competition, monopoly power and mergers.")]),
    "growth": ("2.1.1", [("2.1.1(a)", "Economic growth: GDP, its limits, the economic cycle and the effects of growth.")]),
    "unemployment": ("2.1.1", [("2.1.1(c)", "Unemployment: measurement, types and effects.")]),
    "inflation": ("2.1.1", [("2.1.1(b)", "Inflation and deflation: CPI, causes, links to interest rates and effects.")]),
    "bop": ("2.1.1", [("2.1.1(d)", "The current account: deficits, surpluses, their causes and effects.")]),
    "redistribution": ("2.1.1", [("2.1.1(f)", "Inequality, absolute and relative poverty, and policies to reduce them.")]),
    "environment": ("2.1.1", [("2.1.1(e)", "Environmental damage from business and government responses."),
                              ("2.1.2(d)", "Pros and cons of regulation, legislation, fines and permits.")]),
    "fiscal": ("2.1.2", [("2.1.2(a)", "Fiscal policy: taxes, spending, deficits, surpluses and effects on objectives.")]),
    "monetary": ("2.1.2", [("2.1.2(b)", "Monetary policy: interest rates, the central bank and transmission to households and firms.")]),
    "supply-side": ("2.1.2", [("2.1.2(c)", "Supply-side policies and their effects on output and objectives.")]),
    "conflicts": ("2.1.3", [("2.1.3(a)", "Trade-offs between macroeconomic objectives.")]),
    "globalisation": ("2.2.1", [("2.2.1(a)", "Meaning of globalisation."), ("2.2.1(b)", "Why globalisation has happened."),
                                ("2.2.1(c)", "Effects of globalisation on different groups."), ("2.2.1(d)", "Multinational corporations and their effects on host countries.")]),
    "trade": ("2.2.2", [("2.2.2(a)", "Pros and cons of free trade."), ("2.2.2(f)", "Trade patterns of developed and developing countries.")]),
    "protection": ("2.2.2", [("2.2.2(b)", "Why countries protect industries."), ("2.2.2(c)", "Tariffs, quotas, subsidies and other methods."),
                             ("2.2.2(d)", "Trading blocs."), ("2.2.2(e)", "The role of the WTO.")]),
    "exchange": ("2.2.3", [("2.2.3(a)", "Meaning of an exchange rate."), ("2.2.3(b)", "What shifts currency demand and supply."),
                           ("2.2.3(c)", "Appreciation and its effects."), ("2.2.3(d)", "Depreciation and its effects.")]),
}

TOPICS = [(tid, TOPIC_REFS[tid][0], TOPIC_REFS[tid][1], paper,
           [(s[0], OFFICIAL[s[0]][0], s[2], s[3], s[4], OFFICIAL[s[0]][1]) for s in subs])
          for tid, _ref, _title, paper, subs in TOPICS]


def sid(topic, sub):
    return f"economics.{topic}.{sub}"


def paper_of(topic):
    for t in TOPICS:
        if t[0] == topic:
            return t[3]


def sub_index():
    out = {}
    for tid, tref, ttitle, paper, subs in TOPICS:
        for s in subs:
            out[sid(tid, s[0])] = {"topic": tid, "ref": s[1], "qtypes": s[4], "points": [p[0] for p in s[5]], "paper": paper}
    return out


COVER = {
    "instructions": [
        "Use black ink or ball-point pen.",
        "Fill in the boxes at the top of this page with your name, centre number and candidate number.",
        "Answer all questions.",
        "Answer the questions in the spaces provided - there may be more space than you need.",
        "Calculators may be used.",
        "Show all your working, with your final answer clearly identified.",
    ],
    "information": [
        "The total mark for this paper is 80.",
        "The marks for each question are shown in brackets - use them as a guide to how long to spend on each question.",
    ],
    "advice": [
        "Read each question carefully before you start to answer it.",
        "Try to answer every question.",
        "Check your answers if you have time at the end.",
    ],
}

SEC_INSTR = "Answer ALL questions. Write your answers in the spaces provided. Some questions must be answered with a cross in a box. If you change your mind, put a line through the box and mark your new answer with a cross."


def slot(label, qt, marks):
    return {"label": label, "qtypes": [qt], "marks": marks}


def paper_sections(p):
    if p == "p1":
        q1 = [("(a)", "mcq", 1), ("(b)", "mcq", 1), ("(c)", "define", 2), ("(d)", "state", 1), ("(e)", "define", 1),
              ("(f)", "calculate", 2), ("(g)", "diagram", 3), ("(h)", "explain", 3), ("(i)", "analyse", 6)]
        q2 = [("(a)", "mcq", 1), ("(b)", "mcq", 1), ("(c)", "calculate", 2), ("(d)", "define", 2), ("(e)", "describe", 2),
              ("(f)", "explain", 3), ("(g)", "assess", 9)]
    else:
        q1 = [("(a)", "mcq", 1), ("(b)", "mcq", 1), ("(c)", "define", 2), ("(d)", "describe", 2), ("(e)", "calculate", 2),
              ("(f)", "diagram", 3), ("(g)", "explain", 3), ("(h)", "analyse", 6)]
        q2 = [("(a)", "mcq", 1), ("(b)", "mcq", 1), ("(c)", "state", 1), ("(d)", "define", 2), ("(e)", "explain", 3),
              ("(f)", "diagram", 3), ("(g)", "assess", 9)]
    q3 = [("(a)", "mcq", 1), ("(b)", "mcq", 1), ("(c)", "diagram", 3), ("(d)", "analyse", 6), ("(e)", "assess", 9)]
    q4 = [("(a)-(c)", "data-response", 20)]
    secs = []
    for i, parts in enumerate([q1, q2, q3, q4], 1):
        secs.append({"id": f"q{i}", "title": f"Question {i}", "marks": 20,
                     "instructions": SEC_INSTR if i == 1 else None,
                     "slots": [slot(f"{i}{lab}", qt, m) for lab, qt, m in parts]})
        if i != 1:
            del secs[-1]["instructions"]
    return secs


def build_spec():
    topics = []
    for tid, tref, ttitle, paper, subs in TOPICS:
        topics.append({
            "id": tid, "ref": tref, "title": ttitle, "papers": [paper],
            "subtopics": [{"id": sid(tid, s[0]), "ref": s[1], "title": s[2], "summary": s[3], "papers": [paper],
                           "qtypes": s[4], "points": [{"ref": r, "summary": sm} for r, sm in s[5]]} for s in subs]})
    papers = []
    for pid, name, code in (("p1", "Paper 1: Microeconomics and Business Economics", "4EC1/01"),
                            ("p2", "Paper 2: Macroeconomics and the Global Economy", "4EC1/02")):
        papers.append({"id": pid, "name": name, "paper_code": code, "minutes": 90, "marks": 80, "calculator": True,
                       "materials": "You do not need any other materials.", "answer_style": "in-booklet",
                       **COVER, "sections": paper_sections(pid)})
    spec = {
        "subject": "economics", "code": "4EC1", "board": "Pearson Edexcel International GCSE",
        "title": "Economics", "short": "Economics",
        "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-economics-2017.html",
        "spec_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-economics-2017.html",
        "papers": papers, "qtypes": QTYPES, "topics": topics,
    }
    out = ROOT / "data" / "spec" / "economics.json"
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    return spec


if __name__ == "__main__":
    build_spec()
    print("wrote spec")
