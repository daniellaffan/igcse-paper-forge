"""Simplified 4PM1 specification (our own wording) -> data/spec/further-maths.json,
plus the formulae page -> data/reference/further-maths-formulae.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

QTYPES = [
    {"id": "short", "label": "Short structured question", "marks": "3-6",
     "description": "One idea tested in one or two parts: solve, find, evaluate or simplify with full working."},
    {"id": "multi-part", "label": "Multi-part problem", "marks": "7-16",
     "description": "A longer question whose parts (a), (b), (c) build on each other, often ending with a 'hence'."},
    {"id": "show-that", "label": "Show that / proof", "marks": "3-8",
     "description": "A printed result must be established with every step shown; usually followed by a part that uses it."},
    {"id": "graph", "label": "Graph sketching / graphical solution", "marks": "4-12",
     "description": "Sketch a curve with asymptotes and intercepts, complete a table and draw a graph, or shade a region."},
    {"id": "applied", "label": "Applied problem", "marks": "5-12",
     "description": "Calculus or trigonometry in a context: kinematics, connected rates, optimisation, 3D shapes, linear programming."},
]

# topic: (ref, title, [subtopic tuples]) ; subtopic: (id, ref, title, summary, qtypes, [(point ref, summary)])
TOPICS = [
    ("logs", "1", "Logarithmic functions and indices", [
        ("logs.graphs", "1A", "Exponential and logarithmic graphs",
         "Know the shapes of y = a^x and y = log_b x and use them to sketch and solve.",
         ["graph", "short"],
         [("1A", "Recognise and sketch exponential and logarithmic curves, including where they cross the axes and their asymptotes.")]),
        ("logs.laws", "1B", "Laws of indices and logarithms",
         "Combine and simplify logs, change the base, and solve equations with unknown powers.",
         ["short", "show-that", "multi-part"],
         [("1B", "Use the multiplication, division and power laws of logs, change of base, and solve a^x = b type equations.")]),
        ("logs.surds", "1C/1D", "Surds",
         "Simplify surds and remove surds from the denominator of a fraction.",
         ["short", "show-that"],
         [("1C", "Simplify and combine simple surds, using them to keep answers exact."),
          ("1D", "Rationalise denominators, including denominators of the form a + b√c.")]),
    ]),
    ("quadratics", "2", "The quadratic function", [
        ("quad.manip", "2A", "Factorising and completing the square",
         "Factorise quadratics and write them in completed-square form to find turning points.",
         ["short", "multi-part"],
         [("2A", "Factorise quadratic expressions and rewrite them in completed-square form.")]),
        ("quad.discriminant", "2B", "The discriminant",
         "Use b² − 4ac to decide whether roots are real and distinct, equal, or not real.",
         ["short", "show-that"],
         [("2B", "Use the discriminant to classify roots and to find unknown coefficients.")]),
        ("quad.roots", "2C", "Sums and products of roots",
         "Work with α + β and αβ, evaluate symmetric expressions and form new equations from given roots.",
         ["short", "multi-part", "show-that"],
         [("2C", "Use α + β = −b/a and αβ = c/a to evaluate expressions in the roots and form equations with related roots.")]),
    ]),
    ("identities", "3", "Identities and inequalities", [
        ("ident.factor", "3A/3B", "Algebraic division, factor and remainder theorems",
         "Divide polynomials, use the factor and remainder theorems and factorise cubics.",
         ["short", "show-that", "multi-part"],
         [("3A", "Divide a polynomial by a linear expression to find the quotient and remainder."),
          ("3B", "Use f(a) to test for factors and find remainders, and fully factorise cubic expressions.")]),
        ("ident.simul", "3C", "Simultaneous and cubic equations",
         "Solve one linear and one quadratic equation together, and solve cubics with a rational root.",
         ["short", "multi-part"],
         [("3C", "Solve a linear and a quadratic equation simultaneously, and solve cubic equations.")]),
        ("ident.ineq", "3D", "Linear and quadratic inequalities",
         "Solve linear and quadratic inequalities and combine solution sets.",
         ["short", "multi-part"],
         [("3D", "Solve linear and quadratic inequalities, giving the answer as a set of values.")]),
        ("ident.regions", "3E", "Regions and linear programming",
         "Show inequalities as regions on a graph and find the best value of an expression in a region.",
         ["graph", "applied"],
         [("3E", "Represent linear inequalities in two variables graphically and solve simple linear programming problems.")]),
    ]),
    ("graphs", "4", "Graphs", [
        ("graphs.sketch", "4A", "Polynomial and rational graphs",
         "Sketch cubics and curves like y = (ax + b)/(cx + d), showing intercepts and asymptotes.",
         ["graph", "multi-part"],
         [("4A", "Sketch graphs of polynomials and rational functions with linear denominators, including asymptotes parallel to the axes.")]),
        ("graphs.solve", "4B", "Solving equations graphically",
         "Complete a table, draw a curve and add a suitable straight line to estimate roots.",
         ["graph", "short"],
         [("4B", "Solve equations (including ones with exponentials or trig) by drawing graphs and reading intersections.")]),
    ]),
    ("series", "5", "Series", [
        ("series.sigma", "5A", "Sigma notation",
         "Read and use ∑ notation for sums of terms.",
         ["short", "show-that"],
         [("5A", "Interpret and evaluate sums written with ∑ notation.")]),
        ("series.ap", "5B", "Arithmetic series",
         "Use the nth term and the sum of an arithmetic series.",
         ["short", "multi-part", "applied"],
         [("5B", "Use the general term and the sum to n terms of arithmetic and geometric series, and the sum to infinity when |r| < 1.")]),
        ("series.gp", "5B", "Geometric series",
         "Use the nth term, the sum of n terms and the sum to infinity of a geometric series.",
         ["short", "multi-part", "applied"],
         [("5B", "Use the general term and the sum to n terms of arithmetic and geometric series, and the sum to infinity when |r| < 1.")]),
    ]),
    ("binomial", "6", "The binomial series", [
        ("binom.posint", "6A(i)", "Binomial expansion for positive integer powers",
         "Expand (a + bx)^n for whole-number n and pick out given terms.",
         ["short", "multi-part"],
         [("6A(i)", "Expand (1 + x)^n when n is a positive integer and find particular coefficients.")]),
        ("binom.rational", "6A(ii)", "Binomial series for any rational power",
         "Expand (1 + x)^n for fractional or negative n, state when it is valid, and use it to approximate.",
         ["short", "multi-part", "show-that"],
         [("6A(ii)", "Expand (1 + x)^n for rational n with |x| < 1, stating the range of validity, and use it for approximations.")]),
    ]),
    ("vectors", "7", "Scalar and vector quantities", [
        ("vec.basic", "7A-7E", "Vector arithmetic, magnitude and unit vectors",
         "Add and scale vectors, use i and j, find magnitudes, position vectors and unit vectors.",
         ["short", "multi-part"],
         [("7A", "Add, subtract and scale coplanar vectors and compare coefficients of non-parallel vectors."),
          ("7B", "Work with components and the unit vectors i and j."),
          ("7C", "Find the magnitude of a vector."),
          ("7D", "Use position vectors, with AB = b − a."),
          ("7E", "Find a unit vector in a given direction.")]),
        ("vec.geometry", "7F", "Vectors in geometry",
         "Use vectors to prove points are collinear, lines are parallel, and find where lines meet.",
         ["show-that", "multi-part"],
         [("7F", "Use vectors to show collinearity and parallel lines, find intersection ratios, and divide a line in a ratio.")]),
    ]),
    ("coordinates", "8", "Rectangular Cartesian coordinates", [
        ("coord.points", "8A/8B", "Distance and dividing a line in a ratio",
         "Find the length of a line segment and the point that splits it in a given ratio.",
         ["short", "multi-part"],
         [("8A", "Find the distance between two points."),
          ("8B", "Find the coordinates of the point dividing a line segment in the ratio m : n.")]),
        ("coord.lines", "8C-8E", "Straight lines, parallel and perpendicular",
         "Find gradients and equations of lines and use the conditions for parallel and perpendicular lines.",
         ["short", "multi-part", "show-that"],
         [("8C", "Find the gradient of the line joining two points."),
          ("8D", "Find and use equations of straight lines in the forms y = mx + c, y − y₁ = m(x − x₁) and ax + by = c."),
          ("8E", "Use m₁ = m₂ for parallel lines and m₁m₂ = −1 for perpendicular lines.")]),
    ]),
    ("calculus", "9", "Calculus", [
        ("calc.diff", "9A", "Differentiating powers, trig and exponentials",
         "Differentiate sums of powers of x, sin ax, cos ax and e^(ax).",
         ["short", "show-that"],
         [("9A", "Differentiate and integrate sums of multiples of powers of x, sin ax, cos ax and e^(ax) (not 1/x for integration).")]),
        ("calc.rules", "9B", "Product, quotient and chain rules",
         "Differentiate products, quotients and composite functions.",
         ["short", "show-that"],
         [("9B", "Differentiate products, quotients and simple functions of a function.")]),
        ("calc.integration", "9A", "Integration",
         "Integrate powers of x, sin ax, cos ax and e^(ax), with limits or a given point.",
         ["short"],
         [("9A", "Differentiate and integrate sums of multiples of powers of x, sin ax, cos ax and e^(ax) (not 1/x for integration).")]),
        ("calc.area", "9C", "Areas under and between curves",
         "Use definite integrals to find areas bounded by curves, lines and the axes.",
         ["multi-part", "short"],
         [("9C", "Apply calculus to straight-line kinematics, to areas, and to volumes of revolution about the coordinate axes.")]),
        ("calc.volume", "9C", "Volumes of revolution",
         "Find the volume when a region is rotated through 360° about the x-axis or the y-axis.",
         ["short", "multi-part"],
         [("9C", "Apply calculus to straight-line kinematics, to areas, and to volumes of revolution about the coordinate axes.")]),
        ("calc.kinematics", "9C", "Kinematics",
         "Move between displacement, velocity and acceleration by differentiating and integrating.",
         ["applied", "multi-part"],
         [("9C", "Apply calculus to straight-line kinematics, to areas, and to volumes of revolution about the coordinate axes.")]),
        ("calc.stationary", "9D/9E", "Stationary points, maxima and minima",
         "Find turning points, decide their nature and solve optimisation problems.",
         ["short", "multi-part", "applied"],
         [("9D", "Find stationary points and turning points of a curve."),
          ("9E", "Find and justify maxima and minima, including in practical problems.")]),
        ("calc.tangents", "9F", "Tangents and normals",
         "Find equations of tangents and normals to curves.",
         ["short", "multi-part"],
         [("9F", "Find the equations of tangents and normals to y = f(x).")]),
        ("calc.rates", "9G", "Rates of change and small changes",
         "Link rates with the chain rule and use δy ≈ (dy/dx)δx.",
         ["applied", "short"],
         [("9G", "Use calculus for rates of change, connected rates of change and small-change approximations.")]),
    ]),
    ("trigonometry", "10", "Trigonometry", [
        ("trig.radians", "10A", "Radians, arcs and sectors",
         "Use radians with s = rθ and A = ½r²θ for arcs, sectors and segments.",
         ["short", "multi-part", "show-that"],
         [("10A", "Use radian measure, including arc length and sector area.")]),
        ("trig.ratios", "10B", "Trig ratios of any angle and their graphs",
         "Use exact values and the graphs of sin, cos and tan for any angle.",
         ["short", "graph"],
         [("10B", "Find sine, cosine and tangent of any angle in degrees or radians, use exact values and sketch the graphs.")]),
        ("trig.3d", "10C", "Problems in two and three dimensions",
         "Find lengths and angles in 3D shapes, including line–plane and plane–plane angles.",
         ["applied", "multi-part"],
         [("10C", "Solve 2D and 3D problems, including the angle between a line and a plane and between two planes.")]),
        ("trig.triangles", "10D", "Sine rule, cosine rule and area",
         "Use the sine rule, cosine rule and ½ab sin C in any triangle.",
         ["short", "multi-part"],
         [("10D", "Use the sine and cosine rules and the area formula ½ab sin C.")]),
        ("trig.identities", "10E-10G", "Identities and addition formulae",
         "Use sin² + cos² = 1, tan = sin/cos and the addition formulae to simplify and prove.",
         ["show-that", "short"],
         [("10E", "Use the identity cos²θ + sin²θ = 1."),
          ("10F", "Use tan θ = sin θ / cos θ."),
          ("10G", "Use the addition formulae for sin(A ± B), cos(A ± B) and tan(A ± B).")]),
        ("trig.equations", "10H", "Trigonometric equations",
         "Solve trig equations in a given interval, including ones that need an identity first.",
         ["short", "multi-part"],
         [("10H", "Solve simple trigonometric equations in a stated interval, in degrees or radians.")]),
    ]),
]

COVER = {
    "instructions": [
        "Use black ink or ball-point pen.",
        "Fill in the boxes at the top of this page with your name, centre number and candidate number.",
        "Answer all questions.",
        "Correct answers given without enough working may be awarded no marks.",
        "Answer the questions in the spaces provided; there may be more space than you need.",
        "Do not write on the formulae page: anything written there will gain no credit.",
    ],
    "information": [
        "The total mark for this paper is 100.",
        "The marks for each question are shown in brackets; use them as a guide to how much time to spend on each question.",
        "Calculators may be used.",
    ],
    "advice": [
        "Read each question carefully before you start to answer it.",
        "Check your answers if you have time at the end.",
    ],
}


def build():
    papers = []
    for pid, num, code in (("p1", 1, "4PM1/01"), ("p2", 2, "4PM1/02")):
        papers.append({
            "id": pid, "name": f"Paper {num}", "paper_code": code, "minutes": 120, "marks": 100,
            "calculator": True, **COVER,
            "materials": "You must have: ruler graduated in centimetres and millimetres, protractor, compasses, pen, HB pencil, eraser, calculator.",
            "reference_sheet": "further-maths-formulae", "answer_style": "in-booklet",
            "sections": [{"id": "main", "title": "Answer all questions",
                          "instructions": "Write your answers in the spaces provided. You must write down all the stages in your working.",
                          "marks": 100}],
        })
    topics = []
    for tid, ref, title, subs in TOPICS:
        st = []
        for sid, sref, stitle, summ, qts, pts in subs:
            st.append({"id": "fm." + sid, "ref": sref, "title": stitle, "summary": summ, "papers": ["p1", "p2"],
                       "qtypes": qts, "points": [{"ref": r, "summary": s} for r, s in pts]})
        topics.append({"id": "fm." + tid, "ref": ref, "title": title, "papers": ["p1", "p2"], "subtopics": st})
    spec = {
        "subject": "further-maths", "code": "4PM1", "board": "Pearson Edexcel",
        "title": "International GCSE Further Pure Mathematics", "short": "Further Pure Maths",
        "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-further-pure-mathematics-2017.html",
        "spec_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-further-pure-mathematics-2017.html#%2Ftab-1",
        "papers": papers, "qtypes": QTYPES, "topics": topics,
    }
    (ROOT / "data" / "spec" / "further-maths.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    build_reference()
    return spec


def _b(label, text):
    return {"type": "source", "label": label, "text": text}


def build_reference():
    ref = {
        "id": "further-maths-formulae",
        "title": "Formulae page – Further Pure Mathematics",
        "blocks": [
            _b("Mensuration", "Surface area of a sphere $= 4\\pi r^2$\n\nCurved surface area of a cone $= \\pi r \\times \\text{slant height}$\n\nVolume of a sphere $= \\dfrac{4}{3}\\pi r^3$"),
            _b("Series: arithmetic", "Sum of the first $n$ terms: $S_n = \\dfrac{n}{2}\\left[2a + (n - 1)d\\right]$"),
            _b("Series: geometric", "Sum of the first $n$ terms: $S_n = \\dfrac{a(1 - r^n)}{1 - r}$\n\nSum to infinity: $S_\\infty = \\dfrac{a}{1 - r}$, valid for $|r| < 1$"),
            _b("Binomial series", "$(1 + x)^n = 1 + nx + \\dfrac{n(n-1)}{2!}x^2 + \\dots + \\dfrac{n(n-1)\\dots(n-r+1)}{r!}x^r + \\dots$ for $|x| < 1$, $n \\in \\mathbb{Q}$"),
            _b("Calculus: quotient rule", "$\\dfrac{\\mathrm{d}}{\\mathrm{d}x}\\left(\\dfrac{\\mathrm{f}(x)}{\\mathrm{g}(x)}\\right) = \\dfrac{\\mathrm{f}'(x)\\mathrm{g}(x) - \\mathrm{f}(x)\\mathrm{g}'(x)}{[\\mathrm{g}(x)]^2}$"),
            _b("Trigonometry", "Cosine rule, triangle $ABC$: $a^2 = b^2 + c^2 - 2bc\\cos A$\n\n$\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$\n\n"
               "$\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B$\n\n$\\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B$\n\n"
               "$\\tan(A \\pm B) = \\dfrac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}$"),
            _b("Logarithms", "Change of base: $\\log_a x = \\dfrac{\\log_b x}{\\log_b a}$"),
        ],
    }
    (ROOT / "data" / "reference" / "further-maths-formulae.json").write_text(json.dumps(ref, ensure_ascii=False, indent=1))
