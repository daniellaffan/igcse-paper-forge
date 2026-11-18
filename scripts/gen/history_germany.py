"""Original content for Paper 1 depth study 3: Germany: development of dictatorship, 1918-45.

All extracts below were written for this project in the style of modern history
textbooks; none is taken from a published work.  Knowledge points are written in
our own words.

EXTRACTS[sub] = list of (source line, text, [ (focus, impression, [quotes...], selection note) ])
EFFECTS[sub]  = list of (event phrase, [ (effect, example) ... ])
ISSUES[sub]   = list of {"stems": [...], "factors": [(name, [points...]), ...]}
"""

EXTRACTS = {
"weimar": [
("From a history of Germany, published in 2006.",
"In November 1918 the old imperial order collapsed with astonishing speed. Sailors at Kiel refused "
"to put to sea, and within days councils of workers and soldiers had taken control of towns across "
"the country. The Kaiser, abandoned by his generals, slipped across the border into the Netherlands. "
"Ordinary Germans, exhausted by hunger and four years of slaughter, did little to save him. The "
"monarchy simply melted away, leaving politicians in Berlin scrambling to fill the empty space.",
[("the end of the monarchy in Germany in 1918",
  "the monarchy collapsed suddenly and with very little support from the German people",
  ["astonishing speed", "abandoned by his generals", "did little to save him", "simply melted away"],
  "The author emphasises the speed of the collapse and the lack of loyalty, and says little about the pressure from the Allies, such as President Wilson's demand for an end to the Kaiser's rule."),
 ("the situation facing German politicians in November 1918",
  "politicians were unprepared and struggling to control a chaotic situation",
  ["scrambling to fill the empty space", "councils of workers and soldiers had taken control"],
  "The author selects the spread of the councils to suggest a power vacuum, but does not mention that Ebert quickly made agreements with the army and the trade unions to restore order."),
]),
("From a study of the Weimar Republic, published in 2011.",
"On paper, the constitution of 1919 was one of the most advanced in the world. Every man and woman "
"over twenty could vote, and seats in the Reichstag were shared out exactly in proportion to the votes "
"cast. Yet this fairness came at a price. Dozens of small parties won seats, no single party ever came "
"close to a majority and coalition governments rose and fell at bewildering speed. Article 48, meant "
"only for emergencies, handed the President a dangerous power to rule by decree.",
[("the Weimar Constitution",
  "the constitution was democratic in theory but contained serious weaknesses",
  ["one of the most advanced in the world", "came at a price", "bewildering speed", "a dangerous power"],
  "The author balances praise with criticism but gives more weight to the weaknesses, such as Article 48, and does not mention protections such as the Bill of Rights for citizens."),
 ("coalition government in the Weimar Republic",
  "coalition governments were unstable and short-lived",
  ["no single party ever came close to a majority", "rose and fell at bewildering speed"],
  "The author links instability directly to proportional representation, ignoring other causes such as the deep divisions between the parties themselves."),
]),
("From a history of modern Germany, published in 1998.",
"When the terms of the peace treaty were published in May 1919, Germans of every class and party "
"reacted with fury. Crowds gathered in Berlin to denounce what they called the Diktat, a dictated "
"peace. Flags were flown at half-mast. The loss of territory, the shrunken army and above all the "
"clause blaming Germany for the war were seen as a deliberate humiliation. The politicians who signed "
"it were branded traitors, a label that would follow them for years.",
[("German reactions to the Treaty of Versailles",
  "Germans were united in their anger and saw the Treaty as humiliating",
  ["of every class and party", "reacted with fury", "a deliberate humiliation", "branded traitors"],
  "The author stresses the strength and unity of the anger, using emotive words such as 'fury', and does not consider that some Germans accepted that the Republic had no choice but to sign."),
]),
("From a history of Germany between the wars, published in 2003.",
"The Spartacist rising of January 1919 was brave but hopeless. Its leaders, Rosa Luxemburg and Karl "
"Liebknecht, had doubts about acting so soon, and the workers who seized newspaper offices in Berlin "
"had no clear plan. Within a week the Freikorps, bands of former soldiers who hated communism, had "
"crushed the revolt with brutal efficiency. Both leaders were captured and murdered. For the left, it "
"was a bitter lesson; for the government, a dangerous dependence on armed men it could not control.",
[("the Spartacist uprising",
  "the uprising was badly led and never had a real chance of success",
  ["brave but hopeless", "had doubts about acting so soon", "had no clear plan", "Within a week"],
  "The author focuses on the weakness of the rebels and the speed of defeat, giving little attention to the genuine anger of workers that led to the rising."),
 ("the Freikorps",
  "the Freikorps were violent and dangerous, even to the government that used them",
  ["brutal efficiency", "captured and murdered", "a dangerous dependence on armed men it could not control"],
  "The author selects the murder of the leaders to show the brutality of the Freikorps and hints at future threats, such as their part in the Kapp Putsch."),
]),
("From a study of political violence in Germany, published in 2014.",
"In March 1920 Wolfgang Kapp and a brigade of Freikorps marched into Berlin and declared a new "
"government. The army, asked to defend the Republic, refused to fire on fellow soldiers. Ministers fled "
"to Stuttgart. Yet the putsch collapsed within four days. Berlin's workers answered the government's "
"call for a general strike: trains stopped, gas and water were cut off and offices closed. Kapp found "
"that he could not govern a city that refused to work for him.",
[("the Kapp Putsch",
  "the Kapp Putsch was defeated by the workers rather than by the government or army",
  ["refused to fire on fellow soldiers", "Ministers fled", "collapsed within four days", "could not govern a city that refused to work for him"],
  "The author emphasises the general strike as the decisive factor and gives little attention to the divisions and poor planning among Kapp's own supporters."),
]),
("From a history of the Ruhr crisis, published in 2009.",
"French and Belgian troops entered the Ruhr in January 1923 to take by force the coal and goods "
"Germany had failed to deliver. The German government ordered passive resistance: miners and railway "
"workers simply stopped work. The occupiers responded harshly. More than a hundred Germans were "
"killed and thousands were expelled from their homes. But the strike also had to be paid for, and the "
"government did so by printing money, with disastrous results.",
[("the Ruhr occupation of 1923",
  "the occupation was harsh and had very damaging results for Germany",
  ["responded harshly", "More than a hundred Germans were killed", "thousands were expelled", "with disastrous results"],
  "The author selects the casualties and expulsions to show French harshness and links the crisis to hyperinflation, but does not explain the French view that Germany had deliberately avoided paying reparations."),
 ("passive resistance in the Ruhr",
  "passive resistance was united but came at a heavy cost to Germany",
  ["simply stopped work", "the strike also had to be paid for", "by printing money"],
  "The author shows the resistance as widely supported but chooses to stress its financial cost, pointing forward to hyperinflation."),
]),
("From a social history of Germany, published in 2001.",
"By the autumn of 1923 money had almost ceased to mean anything. Workers were paid twice a day and "
"rushed to the shops before prices rose again. A loaf of bread that had cost a fraction of a mark before "
"the war now cost billions. Pensioners and families who had saved carefully for years found their "
"savings would not buy a postage stamp. Yet some did well: those with debts paid them off with "
"worthless notes, and speculators bought up property cheaply.",
[("the effects of hyperinflation",
  "hyperinflation caused great hardship for many Germans, although a few benefited",
  ["almost ceased to mean anything", "paid twice a day", "would not buy a postage stamp", "Yet some did well"],
  "The author gives a balanced picture by mentioning those who gained, but uses everyday examples such as bread and stamps to emphasise the suffering of savers and pensioners."),
 ("the impact of hyperinflation on the middle classes",
  "the middle classes who had saved money were among the worst affected",
  ["saved carefully for years", "would not buy a postage stamp"],
  "The author selects savers and pensioners as victims; the extract does not mention the long-term loss of middle-class trust in the Republic."),
]),
("From a history of the German Revolution, published in 2018.",
"Friedrich Ebert, the new Chancellor, was no revolutionary. A cautious Social Democrat, he feared "
"chaos far more than he hated the old elite. Within days of taking office he agreed with General "
"Groener that the army would support the new government in return for being left alone. To many on "
"the left this was a betrayal. To Ebert it was the only way to hold the country together while the "
"armistice was signed and elections were organised.",
[("Ebert's leadership in 1918–19",
  "Ebert was a cautious leader whose main aim was to restore order",
  ["no revolutionary", "feared chaos far more", "the only way to hold the country together"],
  "The author presents Ebert's deal with the army sympathetically, from Ebert's point of view, while only briefly mentioning the left's anger at the deal."),
]),
("From a study of the early Weimar Republic, published in 2016.",
"The Republic faced enemies on both sides from the very start. Communists wanted a workers' state "
"like Lenin's Russia. Nationalists, many of them former officers, dreamed of bringing back strong "
"authoritarian rule. Between 1919 and 1922 right-wing gangs carried out more than three hundred "
"political murders, including that of the Foreign Minister Walther Rathenau. Judges, mostly appointed "
"under the Kaiser, punished left-wing rebels severely but treated right-wing killers with remarkable "
"leniency.",
[("the threats facing the Weimar Republic in the years 1919–22",
  "the Republic was threatened from both left and right, but the right was more dangerous",
  ["enemies on both sides", "more than three hundred political murders", "remarkable leniency"],
  "The author chooses statistics about right-wing murders and the bias of the judges to suggest the right was the greater threat."),
 ("the German legal system in the early 1920s",
  "the courts were biased against the left and protected right-wing extremists",
  ["mostly appointed under the Kaiser", "punished left-wing rebels severely", "remarkable leniency"],
  "The author links the judges' background to their bias and contrasts the treatment of left and right."),
]),
],
"recovery": [
("From a biography of Gustav Stresemann, published in 2002.",
"Stresemann became Chancellor in August 1923, at the lowest point in the Republic's history. In just "
"one hundred days he called off passive resistance in the Ruhr, a brave and deeply unpopular decision, "
"and backed the introduction of a new currency. Although his government soon fell, he remained Foreign "
"Minister until his death in 1929. More than any other politician he gave the Republic a chance of "
"survival.",
[("Stresemann's leadership",
  "Stresemann was a brave and highly successful leader who saved the Republic",
  ["the lowest point", "brave and deeply unpopular", "More than any other politician"],
  "The author is admiring throughout and focuses on Stresemann's achievements; the extract does not mention that his government lasted only a few months or that recovery depended on American loans."),
 ("the decision to call off passive resistance",
  "calling off passive resistance was necessary but unpopular",
  ["a brave and deeply unpopular decision"],
  "The author praises the decision as courageous but does not explain why nationalists saw it as a surrender to France."),
]),
("From a history of the German economy, published in 2010.",
"The Rentenmark, introduced in November 1923, worked almost like magic. It was backed not by gold but "
"by a mortgage on German land and industry, and its supply was strictly limited. People trusted it, and "
"prices steadied within weeks. The following year the Dawes Plan reduced annual reparations and brought "
"a large American loan. For the first time since the war, Germany's finances looked sound.",
[("the Rentenmark",
  "the Rentenmark was a remarkably quick and effective solution to hyperinflation",
  ["worked almost like magic", "prices steadied within weeks", "People trusted it"],
  "The author's language, such as 'magic', exaggerates the speed of success and ignores the hardship of those whose savings were never restored."),
 ("the Dawes Plan",
  "the Dawes Plan helped to make Germany's finances stable",
  ["reduced annual reparations", "a large American loan", "looked sound"],
  "The author selects only the benefits of the Plan, leaving out the opposition of nationalists who said Germany should not be paying at all."),
]),
("From a study of Germany in the 1920s, published in 2007.",
"The prosperity of the later 1920s was real but shallow. New factories, roads and swimming pools were "
"built, and wages rose. But much of this was paid for with short-term loans from American banks, money "
"that could be called back at any moment. Unemployment never fell below one million, and farmers "
"suffered from falling prices throughout the period. Germany was living on borrowed time as well as "
"borrowed money.",
[("Germany's economic recovery in the years 1924–29",
  "the recovery was real but fragile and depended on American money",
  ["real but shallow", "could be called back at any moment", "living on borrowed time as well as borrowed money"],
  "The author acknowledges the achievements but chooses evidence such as unemployment and farm prices to emphasise weakness, using a memorable phrase about 'borrowed time'."),
 ("the role of American loans in the German economy",
  "German prosperity relied dangerously on American loans",
  ["short-term loans from American banks", "called back at any moment"],
  "The author stresses the short-term nature of the loans, pointing forward to the crisis after 1929."),
]),
("From a history of European diplomacy, published in 2005.",
"At Locarno in October 1925, Germany sat down as an equal with Britain, France, Italy and Belgium for "
"the first time since the war. Stresemann accepted Germany's western borders as permanent, and in return "
"France promised peace. Newspapers spoke of the 'spirit of Locarno'. Many Germans, however, noticed "
"that nothing had been agreed about the borders in the east, and nationalists accused Stresemann of "
"giving away Alsace-Lorraine for ever.",
[("the Locarno Treaties",
  "Locarno was a diplomatic success for Germany, although it was criticised at home",
  ["as an equal", "for the first time since the war", "the 'spirit of Locarno'", "nationalists accused Stresemann"],
  "The author balances the international praise with the criticism of nationalists, but selects more material on the success."),
]),
("From a study of Weimar foreign policy, published in 2012.",
"Joining the League of Nations in 1926 was a quiet triumph. Germany was given a permanent seat on the "
"Council, a sign that it was once again treated as a great power. Stresemann used his place to speak "
"for German minorities abroad and to press for the early withdrawal of Allied troops from the Rhineland. "
"Two years later Germany signed the Kellogg-Briand Pact, promising with sixty other nations never to use "
"war to settle disputes.",
[("Germany's membership of the League of Nations",
  "joining the League restored Germany's status as a respected great power",
  ["a quiet triumph", "a permanent seat on the Council", "once again treated as a great power"],
  "The author presents only the advantages of membership and does not mention that many Germans saw the League as the guardian of the hated Treaty of Versailles."),
]),
("From a history of the Weimar Republic, published in 2015.",
"The Young Plan of 1929 cut the total of reparations to around a quarter of the original figure and "
"gave Germany fifty-nine years to pay. To Stresemann it was a sensible bargain that would also free the "
"Rhineland of Allied troops. To the nationalist newspaper owner Alfred Hugenberg it was slavery passed "
"down to the grandchildren of Germans not yet born. His campaign against the plan gave Hitler national "
"publicity he could never have bought.",
[("the Young Plan",
  "the Young Plan was a reasonable agreement that caused bitter division in Germany",
  ["a sensible bargain", "slavery passed down", "national publicity he could never have bought"],
  "The author sets out two contrasting views and then selects the unintended consequence, the publicity for Hitler, to show the danger of the debate."),
]),
("From a cultural history of Berlin, published in 2019.",
"For a few years in the middle of the 1920s, Berlin became the most exciting city in Europe. Cabarets "
"and jazz clubs stayed open all night, painters and architects experimented with bold new styles and "
"women cut their hair short and went out to work. To the young this was freedom. To many older and "
"rural Germans it was a sign of moral decay, proof that the Republic had lost touch with traditional "
"German values.",
[("culture in Germany in the years 1924–29",
  "Weimar culture was exciting and modern but deeply divisive",
  ["the most exciting city in Europe", "To the young this was freedom", "a sign of moral decay"],
  "The author uses lively examples of Berlin night life and contrasts the views of young and old, but focuses only on the capital."),
]),
("From a study of German politics, published in 2004.",
"The years after 1924 were the calmest the Republic ever knew. There were no attempted revolutions, "
"and the extremist parties lost ground: in the 1928 election the Nazis won just twelve seats. In 1925 "
"Germans elected Field Marshal Hindenburg as President, and to the surprise of many he respected the "
"constitution. Yet the moderate parties still found it hard to work together, and few governments "
"lasted longer than a year.",
[("political stability in Germany in the years 1924–29",
  "politics in these years was calmer and more stable, but problems remained",
  ["the calmest the Republic ever knew", "just twelve seats", "Yet the moderate parties still found it hard"],
  "The author uses the low Nazi vote as evidence of stability but adds a warning that coalition government remained weak."),
 ("Hindenburg's election as President in 1925",
  "Hindenburg's election was surprisingly good for the stability of the Republic",
  ["to the surprise of many he respected the constitution"],
  "The author stresses that Hindenburg behaved better than expected but does not explain why his election worried supporters of democracy."),
]),
],
"rise": [
("From a history of the Nazi Party, published in 2000.",
"When Hitler first attended a meeting of the German Workers' Party in September 1919, it had barely "
"fifty members and met in the back rooms of Munich beer halls. Within two years he had transformed it. "
"He gave it a new name, a twenty-five point programme and the swastika as its symbol. Above all he gave "
"it his voice: his speeches drew crowds of thousands, and in 1921 he forced the party's founders to "
"accept him as its leader with total authority.",
[("the early development of the Nazi Party",
  "Hitler rapidly turned a tiny group into a growing and organised party",
  ["barely fifty members", "Within two years he had transformed it", "crowds of thousands"],
  "The author places Hitler at the centre of every change and gives little credit to others, such as Drexler or Röhm."),
 ("Hitler's leadership of the party in the years 1919–21",
  "Hitler dominated the party through his speaking and his determination to take control",
  ["Above all he gave it his voice", "forced the party's founders", "total authority"],
  "The author emphasises Hitler's personal power with words such as 'forced' and 'total'."),
]),
("From a study of the Munich Putsch, published in 2013.",
"The putsch of November 1923 was a fiasco. Hitler burst into the Bürgerbräukeller, fired a shot into the "
"ceiling and announced a national revolution, but by the next morning the Bavarian leaders he had "
"bullied had slipped away. When about two thousand Nazis marched into the centre of Munich, police "
"opened fire. Sixteen marchers died and Hitler fled, to be arrested two days later hiding in a "
"friend's attic.",
[("the Munich Putsch",
  "the Munich Putsch was badly planned and ended in humiliating failure",
  ["was a fiasco", "had slipped away", "Hitler fled", "hiding in a friend's attic"],
  "The author selects the most embarrassing details, such as the shot into the ceiling and Hitler hiding, to make the putsch look ridiculous, and ignores its later propaganda value."),
]),
("From a biography of Hitler, published in 2008.",
"Hitler's trial in 1924 turned defeat into victory. The judges allowed him to speak for hours, and "
"newspapers across Germany reported every word. He presented himself as a patriot who had tried to save "
"the nation from traitors. The court gave him the shortest sentence it could, and in Landsberg prison he "
"lived in comfort, receiving visitors and dictating Mein Kampf. He left prison after only nine months.",
[("Hitler's trial and imprisonment",
  "Hitler gained far more than he lost from his trial and imprisonment",
  ["turned defeat into victory", "reported every word", "lived in comfort", "only nine months"],
  "The author focuses on the benefits for Hitler and the leniency of the court, and says little about the fact that the party was banned while he was in prison."),
]),
("From a history of the Nazi movement, published in 2006.",
"After prison, Hitler decided that the Nazis would win power through the ballot box rather than by "
"force. The years 1925 to 1928 were spent quietly building. The party was organised into regions, each "
"under a loyal Gauleiter. Youth and women's sections were set up, and the SS was formed as Hitler's "
"personal guard. Membership grew steadily, but in 1928 the voters were still not listening: the party "
"won less than three per cent of the vote.",
[("the reorganisation of the Nazi Party in the years 1925–28",
  "the reorganisation made the party stronger but did not bring electoral success",
  ["quietly building", "Membership grew steadily", "the voters were still not listening"],
  "The author lists the organisational changes in detail but ends with the poor election result to show their limits."),
]),
("From a history of the Great Depression in Germany, published in 2011.",
"No country was hit harder by the Depression than Germany. When American banks demanded their loans "
"back, German businesses collapsed. By early 1932 six million people were out of work, and many more "
"were on short hours. Queues stretched outside soup kitchens and labour exchanges. Chancellor Brüning "
"cut wages and unemployment benefit, earning the nickname 'the hunger Chancellor'. Desperate people "
"began to listen to those who promised radical answers.",
[("the impact of the Great Depression on Germany",
  "the Depression caused desperate suffering that pushed people towards extremists",
  ["No country was hit harder", "six million people were out of work", "Desperate people began to listen"],
  "The author selects unemployment figures and images of queues to show suffering and links this directly to the rise of radical parties."),
 ("Brüning's response to the Depression",
  "Brüning's policies made the suffering worse and were deeply unpopular",
  ["cut wages and unemployment benefit", "'the hunger Chancellor'"],
  "The author uses Brüning's nickname to show his unpopularity but does not explain that he believed cuts were needed to protect the currency."),
]),
("From a study of Nazi propaganda, published in 2003.",
"Joseph Goebbels understood that elections were won by emotion, not argument. The Nazis flooded towns "
"with posters, held torchlit parades and sent speakers to the smallest villages. In 1932 Hitler flew from "
"city to city in a hired aeroplane, sometimes speaking at four rallies in a single day. The message was "
"simple and endlessly repeated: the Republic had failed, and only Hitler could rescue Germany from "
"communism and despair.",
[("Nazi methods of winning support",
  "Nazi campaigning was modern, energetic and highly effective",
  ["elections were won by emotion", "flooded towns with posters", "four rallies in a single day", "endlessly repeated"],
  "The author focuses on propaganda techniques and gives Goebbels great credit, but does not consider other reasons for support, such as economic despair."),
]),
("From a history of street violence in Germany, published in 2017.",
"By 1932 the SA had over four hundred thousand members, more men than the German army. Many were young "
"and unemployed, attracted by a uniform, a hot meal and a sense of purpose. They protected Nazi meetings "
"and broke up those of their opponents. Street battles with communists left hundreds dead. For some "
"voters the brown-shirted columns were frightening; for others they were a sign of the discipline and "
"strength Germany needed.",
[("the role of the SA",
  "the SA was large, violent and important to the Nazi rise, with mixed effects on voters",
  ["more men than the German army", "broke up those of their opponents", "left hundreds dead", "frightening"],
  "The author balances the fear the SA caused against its appeal and selects its size to show its importance."),
]),
("From a study of the end of the Weimar Republic, published in 2009.",
"Hitler did not seize power in January 1933; he was handed it. After the Nazis lost votes in the "
"November 1932 election, Franz von Papen persuaded President Hindenburg that Hitler could be controlled "
"if he was made Chancellor with only a few Nazis in the cabinet. Hindenburg, who disliked Hitler, gave "
"way. Papen boasted that within two months they would have pushed Hitler into a corner. It was one of "
"the great misjudgements of history.",
[("how Hitler became Chancellor in January 1933",
  "Hitler became Chancellor because of a mistaken deal by the political elite, not because of his own strength",
  ["he was handed it", "Hitler could be controlled", "gave way", "one of the great misjudgements of history"],
  "The author stresses the role of Papen and Hindenburg and the Nazi loss of votes, and plays down the fact that the Nazis were still the largest party in the Reichstag."),
 ("the role of von Papen",
  "Papen was over-confident and badly misjudged Hitler",
  ["persuaded President Hindenburg", "Papen boasted", "great misjudgements"],
  "The author chooses Papen's boast to show his arrogance."),
]),
("From a history of German elections, published in 2014.",
"In July 1932 the Nazis won thirty-seven per cent of the vote, making them by far the largest party in "
"the Reichstag. Their support came from every region and class, but it was strongest among Protestant "
"farmers, small shopkeepers and the middle classes of small towns. Industrial workers were more likely "
"to stay loyal to the Social Democrats or the Communists. Catholics, too, mostly kept voting for their "
"own Centre Party.",
[("support for the Nazis in 1932",
  "the Nazis had wide support, but it was stronger in some groups than others",
  ["by far the largest party", "from every region and class", "strongest among Protestant farmers"],
  "The author uses election evidence carefully, showing which groups were less attracted to the Nazis."),
]),
],
"nazi": [
("From a history of the Third Reich, published in 2005.",
"On the night of 27 February 1933 the Reichstag building went up in flames. A young Dutch communist, "
"Marinus van der Lubbe, was found inside. Hitler declared that the fire was the signal for a communist "
"revolution, and the next day Hindenburg signed an emergency decree suspending basic rights. Thousands "
"of communists were arrested. Whether or not the Nazis started the fire, they could hardly have wished "
"for a more useful event.",
[("the Reichstag Fire",
  "the fire was extremely useful to the Nazis in increasing their power",
  ["the signal for a communist revolution", "suspending basic rights", "Thousands of communists were arrested", "could hardly have wished for a more useful event"],
  "The author deliberately leaves open who started the fire but emphasises how the Nazis exploited it."),
]),
("From a study of the Nazi seizure of power, published in 2010.",
"The Enabling Act of March 1933 was passed in a theatre ringed by SA and SS men. Communist deputies "
"were already in prison or in hiding. The Centre Party voted in favour after Hitler promised to respect "
"the rights of the Catholic Church. Only the Social Democrats voted against. With this law the Reichstag "
"gave away its own power, allowing Hitler to make laws for four years without its consent.",
[("the Enabling Act",
  "the Enabling Act was passed through intimidation and trickery",
  ["ringed by SA and SS men", "already in prison or in hiding", "Hitler promised", "gave away its own power"],
  "The author selects the threatening atmosphere and Hitler's promises, implying the vote was not truly free."),
]),
("From a biography of Ernst Röhm, published in 2012.",
"By the summer of 1934 Röhm's SA had nearly three million members and Röhm wanted it to swallow the "
"army. The generals were alarmed, and Hitler needed their support. On 30 June SS squads arrested Röhm and "
"other SA leaders; many were shot without trial. Old enemies such as von Schleicher were murdered too. "
"Hitler told the Reichstag that he had acted as the supreme judge of the German people. The army thanked "
"him.",
[("the purge of the SA in June 1934",
  "the Night of the Long Knives was a ruthless act that strengthened Hitler's position",
  ["shot without trial", "Old enemies", "the supreme judge of the German people", "The army thanked him"],
  "The author emphasises the brutality and the army's approval, but gives little attention to the reaction of ordinary Germans."),
]),
("From a history of the police state, published in 2007.",
"The Gestapo was never as large as Germans imagined. In some cities a few dozen officers watched over "
"hundreds of thousands of people. Its power came from fear and from the willingness of ordinary citizens "
"to denounce neighbours, colleagues and even relatives. Many denunciations were made out of spite or "
"jealousy rather than loyalty to the regime. The result was a society in which people were careful about "
"everything they said.",
[("the Gestapo",
  "the Gestapo was powerful mainly because of fear and help from ordinary Germans",
  ["never as large as Germans imagined", "a few dozen officers", "willingness of ordinary citizens to denounce"],
  "The author challenges the idea of an all-seeing Gestapo and selects evidence about denunciations to shift attention to ordinary people."),
 ("everyday life under the Nazi police state",
  "people lived in constant fear and were careful about what they said",
  ["careful about everything they said", "even relatives"],
  "The author suggests fear touched every relationship, which may exaggerate its effect on Germans who supported the regime."),
]),
("From a study of Nazi propaganda, published in 2016.",
"Goebbels believed that radio was the most powerful weapon of all. The government made cheap sets, the "
"People's Receiver, and by 1939 seventy per cent of homes had one. Loudspeakers were put up in streets "
"and factories so that nobody could miss Hitler's speeches. Newspapers were told each day what to print. "
"Yet propaganda worked best when it reinforced what people already believed, and it struggled to win over "
"committed opponents.",
[("Nazi propaganda",
  "propaganda was widespread and well organised, but it had limits",
  ["the most powerful weapon of all", "seventy per cent of homes", "so that nobody could miss", "Yet propaganda worked best"],
  "The author gives detailed evidence of the reach of propaganda before adding a qualification about its limits."),
]),
("From a history of German women, published in 2004.",
"Nazi leaders believed that a woman's place was in the home. Women doctors and civil servants were "
"dismissed, and loans were offered to couples who married if the wife gave up work. Mothers of large "
"families received a medal, the Mother's Cross. Yet the policy was never fully carried out. As the economy "
"recovered and rearmament began, factories needed workers, and by 1939 more women were in paid work than "
"in 1933.",
[("Nazi policies towards women",
  "the Nazis tried hard to keep women at home but did not fully succeed",
  ["a woman's place was in the home", "were dismissed", "the policy was never fully carried out", "more women were in paid work"],
  "The author describes the policies and then selects employment figures to show they were contradicted by economic needs."),
]),
("From a study of youth in Nazi Germany, published in 2008.",
"The Hitler Youth offered boys camping, sport and adventure, and many joined with enthusiasm. From 1936 "
"membership was expected, and from 1939 it was compulsory. Boys were trained to be tough and obedient "
"soldiers; girls in the League of German Maidens were prepared for motherhood. But as the activities "
"became more military and rigid, some teenagers grew bored, and a minority drifted into rebellious youth "
"gangs.",
[("the Hitler Youth",
  "the Hitler Youth was popular at first but became less attractive as it became compulsory and military",
  ["joined with enthusiasm", "compulsory", "tough and obedient", "some teenagers grew bored"],
  "The author shows change over time, moving from enthusiasm to boredom and rebellion."),
]),
("From a history of education in Germany, published in 2013.",
"Every school subject was bent to serve Nazi ideas. Biology lessons taught race theory, history lessons "
"celebrated German heroes and blamed Jews for defeat in 1918, and even mathematics problems were written "
"about the cost of caring for the disabled. Teachers had to join the Nazi Teachers' League, and those "
"thought unreliable were sacked. Physical education was given far more time, while the standard of "
"academic work fell.",
[("Nazi education policy",
  "education was completely used to spread Nazi ideas, at the cost of academic standards",
  ["Every school subject was bent", "even mathematics problems", "were sacked", "the standard of academic work fell"],
  "The author uses examples from several subjects to suggest total control and ends with a negative judgement about standards."),
]),
("From a history of the Churches in Germany, published in 2011.",
"Hitler signed a Concordat with the Pope in 1933, promising to leave the Catholic Church alone if it "
"kept out of politics. He soon broke his word. Catholic youth groups were closed and priests were "
"arrested. Among Protestants, the regime created a Reich Church under a Nazi bishop. Some pastors, led "
"by Martin Niemöller, set up a rival Confessing Church. Niemöller spent seven years in concentration "
"camps for his defiance.",
[("Nazi policy towards the Churches",
  "the Nazis tried to control the Churches through deals and persecution, which led to some resistance",
  ["He soon broke his word", "priests were arrested", "a rival Confessing Church", "seven years in concentration camps"],
  "The author shows the Nazis as untrustworthy and selects Niemöller as an example of courage, but does not suggest how many churchgoers accepted the regime."),
]),
("From a history of the persecution of the Jews, published in 2006.",
"The persecution of Germany's half a million Jews grew step by step. In 1933 there was a boycott of "
"Jewish shops. In 1935 the Nuremberg Laws took away citizenship and banned marriages between Jews and "
"other Germans. Then, in November 1938, came Kristallnacht: synagogues were burned, thousands of shops "
"were smashed and around thirty thousand Jewish men were sent to camps. Many Jews now tried desperately "
"to leave the country.",
[("Nazi persecution of the Jews in the years 1933–38",
  "persecution grew steadily worse until it became violent and terrifying",
  ["grew step by step", "synagogues were burned", "thirty thousand Jewish men", "tried desperately to leave"],
  "The author arranges events in order of increasing severity, building to Kristallnacht."),
 ("Kristallnacht",
  "Kristallnacht was a violent and organised attack on Germany's Jews",
  ["synagogues were burned", "thousands of shops were smashed", "sent to camps"],
  "The author selects the scale of destruction and arrests to show how serious the attack was."),
]),
("From a history of the Nazi economy, published in 2009.",
"Hitler promised work and bread, and unemployment fell from six million in 1933 to almost nothing by "
"1939. Young men were drafted into the National Labour Service to dig ditches and plant forests. Huge "
"motorways were built. Rearmament created hundreds of thousands of jobs. But the figures were also "
"massaged: women and Jews who lost their jobs were not counted, and the labour service paid little more "
"than pocket money.",
[("Nazi policies to reduce unemployment",
  "Nazi policies reduced unemployment, but the success was exaggerated",
  ["fell from six million", "almost nothing by 1939", "the figures were also massaged", "little more than pocket money"],
  "The author first gives impressive figures and then undermines them with evidence that some groups were not counted."),
]),
("From a study of workers in the Third Reich, published in 2015.",
"Trade unions were abolished in May 1933 and replaced by the German Labour Front. Workers lost the right "
"to strike and their hours grew longer. To keep them content, the Strength Through Joy organisation "
"offered cheap theatre tickets, sports clubs and holidays, even cruises to Norway. Workers saved for a "
"People's Car, the Volkswagen, though not a single one was delivered to them before the war.",
[("the Labour Front and Strength Through Joy",
  "workers lost their rights and were offered rewards that were sometimes empty promises",
  ["lost the right to strike", "hours grew longer", "To keep them content", "not a single one was delivered"],
  "The author describes the benefits but selects the Volkswagen scheme to suggest that workers were deceived."),
]),
],
"war": [
("From a history of the Holocaust, published in 2008.",
"After the invasion of Poland in 1939, millions of Jews came under German rule. They were forced into "
"ghettos, sealed districts of cities such as Warsaw and Łódź, where hunger and disease killed thousands "
"every month. In Warsaw, over four hundred thousand people were crammed into an area of a few square "
"kilometres. Food rations were set far below what was needed to stay alive.",
[("the ghettos",
  "life in the ghettos was deliberately made unbearable and deadly",
  ["forced into ghettos", "killed thousands every month", "crammed into", "far below what was needed to stay alive"],
  "The author selects figures about overcrowding and starvation to show that suffering was intentional, but does not describe how ghetto inhabitants tried to survive or resist."),
]),
("From a study of the war in the East, published in 2012.",
"When German armies invaded the Soviet Union in June 1941 they were followed by four Einsatzgruppen, "
"special SS units with orders to kill Jews and communist officials. Victims were rounded up, marched to "
"the edge of towns and shot beside pits. At Babi Yar near Kiev more than thirty thousand people were "
"murdered in two days. By the end of 1941 the units had killed around half a million people.",
[("the Einsatzgruppen",
  "the Einsatzgruppen carried out mass murder on a huge and organised scale",
  ["special SS units with orders to kill", "rounded up", "more than thirty thousand people", "around half a million"],
  "The author uses precise figures and a matter-of-fact tone, letting the scale of the killing speak for itself."),
]),
("From a history of Nazi Germany, published in 2003.",
"At the Wannsee Conference in January 1942, senior officials met over lunch to organise the 'Final "
"Solution of the Jewish Question'. The meeting lasted barely ninety minutes. Jews from every corner of "
"Europe were to be transported east to camps such as Auschwitz-Birkenau and Treblinka. There, gas chambers "
"would make killing faster and less disturbing for the killers. Around six million Jews were murdered "
"by 1945.",
[("the Final Solution",
  "the Final Solution was planned in a cold, bureaucratic way",
  ["met over lunch", "barely ninety minutes", "faster and less disturbing for the killers"],
  "The author contrasts the ordinary setting of the meeting with the horror of its decisions to shock the reader."),
]),
("From a social history of wartime Germany, published in 2010.",
"For the first two years of the war, life at home was surprisingly normal. Rationing began in 1939, but "
"victories in Poland and France brought in food and loot from the conquered lands. Cinemas and cafés "
"stayed open. It was only after the defeat at Stalingrad in early 1943 that Germans began to feel the "
"full weight of the war, as rations were cut and Goebbels called for total war.",
[("the German home front in the years 1939–42",
  "life at home was relatively comfortable in the early years of the war",
  ["surprisingly normal", "food and loot from the conquered lands", "stayed open"],
  "The author contrasts the early war with the period after Stalingrad, emphasising how little ordinary Germans suffered at first."),
 ("the impact of Stalingrad on the home front",
  "Stalingrad was a turning point after which life at home became much harder",
  ["It was only after the defeat at Stalingrad", "the full weight of the war", "rations were cut"],
  "The author uses Stalingrad as the dividing line, which may simplify a more gradual change."),
]),
("From a study of the 'total war' economy, published in 2014.",
"In February 1943, in a speech at the Berlin Sports Palace, Goebbels asked the crowd if they wanted total "
"war. They roared their approval. Albert Speer, the armaments minister, had already begun to reorganise "
"industry, and weapons production tripled despite the bombing. Luxury shops were closed, theatres shut "
"and millions of foreign forced labourers were brought in to work in German factories.",
[("total war",
  "total war was enthusiastically supported and led to a big increase in war production",
  ["roared their approval", "weapons production tripled", "despite the bombing"],
  "The author takes the reaction of a hand-picked crowd as evidence of support and stresses Speer's success, mentioning forced labour only briefly."),
]),
("From a history of German women in the war, published in 2007.",
"The regime was slow to call on women to work in war industries. Hitler disliked the idea, and soldiers' "
"wives received generous allowances which meant many had no need to work. Only in 1943 were women aged "
"seventeen to forty-five required to register for work, and even then many found ways to avoid it. "
"Germany relied far more on foreign forced labour than on its own women.",
[("the role of women in the German war effort",
  "the Nazi regime was reluctant and slow to use women in the war economy",
  ["slow to call on women", "Hitler disliked the idea", "found ways to avoid it", "relied far more on foreign forced labour"],
  "The author focuses on official reluctance and selects evidence of avoidance, but does not mention women's work in auxiliary services or on farms."),
]),
("From a history of the bombing war, published in 2006.",
"In July 1943 British bombers created a firestorm in Hamburg. Winds of hurricane force sucked people "
"into the flames, and around forty thousand died in a single week. Nearly a million people fled the "
"city. Yet the bombing did not break German morale as the Allies had hoped. Many people blamed the "
"Allies rather than their own government, and factories were often working again within months.",
[("the Allied bombing of Germany",
  "the bombing caused terrible suffering but failed to break German morale",
  ["a firestorm", "forty thousand died in a single week", "did not break German morale", "working again within months"],
  "The author describes the horror of Hamburg in vivid language and then argues that the bombing's aims were not achieved."),
]),
("From a study of youth opposition, published in 2011.",
"The Edelweiss Pirates were working-class teenagers who refused to fit in. They wore check shirts and "
"badges, went hiking on weekends, sang banned songs and beat up Hitler Youth patrols. Most were simply "
"rebels against boredom and discipline. During the war some groups went further, sheltering deserters and "
"attacking officials. In November 1944, thirteen members were publicly hanged in Cologne.",
[("the Edelweiss Pirates",
  "the Edelweiss Pirates were mainly rebellious young people, though some became real resisters",
  ["refused to fit in", "simply rebels against boredom", "some groups went further", "publicly hanged"],
  "The author distinguishes between ordinary rebels and active resisters and ends with the public executions to show the regime's response."),
]),
("From a history of German resistance, published in 2009.",
"The White Rose group was tiny: a handful of students in Munich, led by Hans and Sophie Scholl, and their "
"professor. Between 1942 and 1943 they wrote and distributed six leaflets calling on Germans to resist "
"the crimes of the regime. In February 1943 the Scholls were caught throwing leaflets in the university. "
"Within four days they had been tried and beheaded. Their courage was remarkable, but their impact on "
"the regime was very small.",
[("the White Rose group",
  "the White Rose members were very brave but had little effect on the Nazi regime",
  ["was tiny", "Within four days", "Their courage was remarkable", "very small"],
  "The author admires the group's courage but makes a clear negative judgement about its effectiveness."),
]),
("From a study of the July Plot, published in 2015.",
"On 20 July 1944 Colonel Claus von Stauffenberg placed a bomb in a briefcase under the table at Hitler's "
"headquarters in East Prussia. It exploded, but a heavy table leg shielded Hitler, who suffered only cuts "
"and burns. In Berlin, the plotters hesitated and failed to seize control. Within hours Stauffenberg was "
"shot. Some five thousand people were later executed in the regime's revenge.",
[("the July Bomb Plot",
  "the July Plot was a near miss that failed through bad luck and hesitation",
  ["a heavy table leg shielded Hitler", "the plotters hesitated", "Within hours", "five thousand people"],
  "The author stresses chance and the plotters' indecision, and uses the number of executions to show the scale of the revenge."),
]),
("From a history of the fall of Berlin, published in 2002.",
"By April 1945 Hitler was living in a concrete bunker beneath Berlin, moving armies on maps that no "
"longer existed. Soviet shells were falling on the city. Old men and boys of the Volkssturm were sent to "
"fight tanks with hand-held weapons. On 30 April, with Soviet troops a few hundred metres away, Hitler "
"shot himself. A week later Germany surrendered unconditionally.",
[("the last days of the Third Reich",
  "the Third Reich ended in chaos, desperation and total defeat",
  ["armies on maps that no longer existed", "Old men and boys", "a few hundred metres away", "surrendered unconditionally"],
  "The author selects details that make the regime appear deluded and desperate in its final weeks."),
 ("Hitler's leadership in 1945",
  "Hitler had lost touch with reality by the end of the war",
  ["moving armies on maps that no longer existed", "living in a concrete bunker"],
  "The author's image of imaginary armies suggests Hitler was no longer in control of events."),
]),
],
}

EFFECTS = {
"weimar": [
("the Treaty of Versailles on Germany in the years 1919–23", [
 ("it weakened Germany's economy", "the loss of the Saar coalfields and of about 13 per cent of its territory, together with reparations of £6,600 million set in 1921, put a huge strain on the economy"),
 ("it made the new Republic unpopular from the start", "nationalists blamed the 'November Criminals' who signed the treaty and the 'stab in the back' myth spread"),
 ("it reduced Germany's military power", "the army was limited to 100,000 men, conscription was banned and the Rhineland was demilitarised, which angered officers and encouraged groups such as the Freikorps")]),
("the abdication of the Kaiser on Germany", [
 ("it ended the monarchy and led to the creation of a republic", "Scheidemann proclaimed a republic from the Reichstag on 9 November 1918 and Ebert led the new government"),
 ("it left a power vacuum that encouraged revolutionary groups", "workers' and soldiers' councils took control in many towns and the Spartacists hoped to follow the Bolshevik example"),
 ("it allowed the new government to sign the armistice", "the armistice was signed on 11 November 1918, which led many Germans to link the new politicians with defeat")]),
("the Spartacist uprising (1919) on the Weimar Republic", [
 ("it made the government depend on the Freikorps", "Ebert used the Freikorps to crush the rising, which strengthened right-wing ex-soldiers who were hostile to democracy"),
 ("it left the left deeply divided", "the murder of Luxemburg and Liebknecht left communists bitter towards the Social Democrats, so the left never united against the Nazis later"),
 ("it showed that the Republic faced a serious threat from the left", "the government had to move to Weimar to draw up the constitution because Berlin was unsafe")]),
("the Kapp Putsch (1920) on the Weimar Republic", [
 ("it showed that the army could not be relied on", "General von Seeckt refused to fire on the Freikorps, saying soldiers do not fire on soldiers"),
 ("it showed the power of the workers to defend the Republic", "a general strike stopped transport, water and power in Berlin and the putsch collapsed in four days"),
 ("it revealed the leniency shown to the right", "most of those involved were not punished, and Kapp fled to Sweden, which encouraged further right-wing violence")]),
("the French occupation of the Ruhr (1923) on Germany", [
 ("it led to a collapse in German industrial production", "the Ruhr produced most of Germany's coal and steel, and passive resistance stopped much of it"),
 ("it caused hyperinflation", "the government printed money to pay striking workers, and by November 1923 one US dollar was worth over four trillion marks"),
 ("it united Germans in anger against France", "over 130 civilians were killed and about 150,000 people were expelled from the region, which created resentment")]),
("hyperinflation (1923) on the German people", [
 ("it destroyed the savings of the middle classes", "people with money in the bank or on pensions found it worthless, and many never trusted the Republic again"),
 ("it caused hardship because wages could not keep up with prices", "a loaf of bread cost 201 billion marks by November 1923 and workers took wages home in wheelbarrows"),
 ("it benefited some groups", "people with debts or mortgages paid them off cheaply and businessmen such as Hugo Stinnes bought up firms")]),
("the Weimar Constitution on German politics in the years 1919–23", [
 ("it led to weak coalition governments", "proportional representation meant many small parties won seats, and there were nine governments between 1919 and 1923"),
 ("it gave the President strong emergency powers", "Ebert used Article 48 more than 130 times to deal with crises"),
 ("it gave Germans more democratic rights than before", "all men and women over 20 could vote and there was a bill of rights including freedom of speech")]),
("right-wing political violence on the Weimar Republic in the years 1919–22", [
 ("it removed leading politicians who supported the Republic", "Erzberger, who signed the armistice, was killed in 1921 and Foreign Minister Rathenau in 1922"),
 ("it showed that the courts favoured the right", "of over 350 political murders by right-wing groups, very few led to severe punishment"),
 ("it led the government to pass laws to protect the Republic", "after Rathenau's murder the Law for the Protection of the Republic was passed in 1922")]),
("the 'stab in the back' myth on the Weimar Republic", [
 ("it made the Republic's leaders appear to be traitors", "nationalists called the politicians who signed the armistice the 'November Criminals'"),
 ("it encouraged opposition from the army and the right", "former officers such as Ludendorff spread the claim and later backed the Munich Putsch"),
 ("it weakened support for democracy among ordinary Germans", "many people believed the army had not been defeated in battle, so they saw the Republic as the cause of the humiliation")]),
("the German Revolution of 1918–19 on Germany", [
 ("it ended the rule of the Kaiser and the princes", "all the German royal families gave up their thrones in November 1918"),
 ("it led to elections for a National Assembly", "elections in January 1919 produced an assembly that met at Weimar to write a new constitution"),
 ("it created divisions that weakened the new Republic", "Ebert's deal with the army and the use of force against left-wing workers angered socialists")]),
("reparations on Germany in the years 1921–23", [
 ("they damaged the German economy", "the payments took money and goods that Germany needed for recovery"),
 ("they led to the occupation of the Ruhr", "when Germany fell behind with deliveries of coal and timber in 1922, France and Belgium sent troops into the Ruhr"),
 ("they increased hostility to the Republic", "nationalists blamed the government for agreeing to pay and said Germany was being enslaved")]),
("the creation of the Freikorps on the Weimar Republic", [
 ("it gave the government a force to crush left-wing revolts", "the Freikorps defeated the Spartacists in Berlin and the Bavarian Soviet Republic in 1919"),
 ("it created a dangerous armed group that opposed democracy", "Freikorps units took part in the Kapp Putsch in 1920"),
 ("it increased political violence", "former Freikorps members carried out political murders, including that of Rathenau")]),
("the Munich Putsch (1923) on the Weimar Republic", [
 ("it showed that the Republic could defeat a challenge from the right", "the Bavarian police stopped the march and the leaders were arrested"),
 ("it showed that the courts were lenient to right-wing rebels", "Hitler received only five years, served nine months, and Ludendorff was acquitted"),
 ("it gave publicity to a new enemy of the Republic", "Hitler's trial was reported across Germany and made him a national figure")]),
],
"recovery": [
("the Rentenmark (1923) on Germany", [
 ("it ended hyperinflation", "the supply of the new currency was strictly controlled and prices quickly became stable"),
 ("it restored confidence in German money", "the Rentenmark was backed by German land and industry, and in 1924 the Reichsmark, backed by gold, replaced it"),
 ("it did not restore lost savings", "those who had lost their savings in 1923 received little compensation, so middle-class resentment continued")]),
("the Dawes Plan (1924) on Germany", [
 ("it reduced the burden of reparations", "annual payments were lowered to £50 million a year at first and rose gradually as the economy recovered"),
 ("it brought American loans into Germany", "an initial loan of 800 million marks was followed by billions more by 1929"),
 ("it led to the French leaving the Ruhr", "French and Belgian troops left in 1925, which allowed industry to recover")]),
("American loans on the German economy in the years 1924–29", [
 ("they helped industry to recover", "by 1928 industrial production was higher than before the war"),
 ("they paid for public projects", "local councils built schools, hospitals, housing and swimming pools"),
 ("they made Germany dependent on the USA", "when American banks recalled the short-term loans after 1929, the German economy collapsed")]),
("the Young Plan (1929) on Germany", [
 ("it reduced the total of reparations", "the figure was cut from £6,600 million to £2,000 million to be paid over 59 years"),
 ("it led to the withdrawal of Allied troops from the Rhineland", "the remaining troops left in 1930, five years earlier than planned"),
 ("it gave publicity to the Nazis", "Hitler joined Hugenberg's campaign for a referendum against the plan, which brought him national attention")]),
("the Locarno Treaties (1925) on Germany", [
 ("they improved Germany's relations with France and Britain", "Germany accepted its western borders and France promised not to attack Germany"),
 ("they increased Germany's international status", "Germany was treated as an equal and the treaties led to an invitation to join the League of Nations"),
 ("they angered German nationalists", "nationalists said Stresemann had accepted the loss of Alsace-Lorraine and the Treaty of Versailles")]),
("Germany joining the League of Nations (1926) on Germany", [
 ("it confirmed Germany's return as a great power", "Germany was given a permanent seat on the Council"),
 ("it gave Germany a voice in international affairs", "Stresemann used the League to argue for German minorities and for changes to the peace settlement"),
 ("it was criticised by nationalists", "many Germans saw the League as part of the Treaty of Versailles which they wanted to destroy")]),
("the Kellogg-Briand Pact (1928) on Germany", [
 ("it improved Germany's international reputation", "Germany was one of the original signatories, alongside the USA and France"),
 ("it made Germany appear a peaceful nation", "the countries that signed promised not to use war to settle disputes"),
 ("it increased confidence in the Republic at home", "together with Locarno it was seen as evidence that Stresemann's policies were working")]),
("the work of Stresemann on the Weimar Republic", [
 ("it ended the crisis of 1923", "he called off passive resistance and backed the Rentenmark"),
 ("it improved Germany's relations with other countries", "his diplomacy led to Locarno, League membership and the Kellogg-Briand Pact"),
 ("it increased political stability", "support for extremist parties fell, and in 1928 the Nazis won only 12 seats")]),
("the economic recovery of 1924–29 on the German people", [
 ("it improved living standards for many workers", "real wages rose and in 1927 unemployment insurance was introduced"),
 ("it left farmers in difficulty", "world food prices fell in the late 1920s, so many farmers fell into debt"),
 ("it increased the number of people working in modern industry", "firms such as IG Farben and Siemens expanded and new jobs were created in chemicals and electrical goods")]),
("the 'Golden Age' of Weimar culture on Germany", [
 ("it made Berlin a centre of new art and entertainment", "the Bauhaus school of design and cabaret clubs attracted artists from across Europe"),
 ("it gave more freedom to women", "many young women took jobs in offices and shops and had more social freedom"),
 ("it angered conservative Germans", "many older and rural Germans saw the new culture as immoral and blamed the Republic")]),
("the election of Hindenburg as President (1925) on the Weimar Republic", [
 ("it reassured conservatives and the army", "Hindenburg was a respected war hero, so the right were more willing to accept the Republic"),
 ("it helped political stability in the short term", "Hindenburg kept to the constitution in the years 1925–29"),
 ("it put an opponent of democracy in a powerful position", "Hindenburg later used Article 48 to appoint and support chancellors who ruled without the Reichstag")]),
("the economic recovery of the years 1924–29 on support for extremist parties", [
 ("it reduced support for the Nazis", "the Nazi vote fell to 2.6 per cent in the 1928 election"),
 ("it increased support for moderate parties", "the Social Democrats won over 150 seats in 1928 and led a broad coalition under Müller"),
 ("it ended attempts to overthrow the Republic by force", "there were no putsches or uprisings in the years 1924–29")]),
],
"rise": [
("Hitler joining the German Workers' Party (1919) on the party", [
 ("it gave the party a powerful speaker", "Hitler's speeches in Munich beer halls attracted large crowds and new members"),
 ("it led to changes in the party's name and programme", "in 1920 it became the National Socialist German Workers' Party and published its 25-point programme"),
 ("it led to Hitler becoming leader", "in 1921 Hitler replaced Drexler and took total control of the party")]),
("the setting up of the SA (1921) on the Nazi Party", [
 ("it protected Nazi meetings", "SA men guarded speakers and threw out hecklers"),
 ("it was used to attack opponents", "the SA broke up meetings of rival parties, especially the Communists"),
 ("it gave the party a disciplined and military image", "the brown-shirted uniforms and parades made the Nazis look strong and organised")]),
("the Munich Putsch (1923) on the Nazi Party in the years 1923–28", [
 ("it led to the party being banned and Hitler imprisoned", "the party was banned and Hitler was sentenced to five years in Landsberg prison"),
 ("it gave Hitler national publicity", "his trial was reported in newspapers across Germany"),
 ("it led Hitler to change tactics", "he decided to win power legally through elections rather than by force")]),
("Hitler's imprisonment in Landsberg (1924) on the Nazi Party", [
 ("it gave Hitler time to set out his ideas", "he dictated Mein Kampf to Rudolf Hess"),
 ("it left the party divided while he was away", "without Hitler the movement split into rival groups"),
 ("it helped Hitler decide on a new strategy", "he concluded that the party must use the ballot box to gain power")]),
("the reorganisation of the Nazi Party in the years 1925–28 on the party", [
 ("it made the party a national organisation", "Germany was divided into regions, each run by a Gauleiter"),
 ("it increased membership", "membership rose from about 27,000 in 1925 to over 100,000 by 1928"),
 ("it increased Hitler's control of the party", "at the Bamberg Conference in 1926 Hitler defeated the northern wing led by Strasser")]),
("the Great Depression on Germany in the years 1929–32", [
 ("it caused mass unemployment", "unemployment rose to about six million by 1932"),
 ("it led to the collapse of parliamentary government", "the coalition fell in 1930 and Chancellor Brüning ruled using Article 48 decrees"),
 ("it increased support for extremist parties", "the Nazis rose from 12 seats in 1928 to 230 seats in July 1932 and the Communists also gained")]),
("the Great Depression on the Nazi Party", [
 ("it increased the Nazi vote", "the party won 107 seats in 1930 and 230 in July 1932"),
 ("it increased membership of the SA", "many unemployed young men joined the SA, which had about 400,000 members by 1932"),
 ("it gave the Nazis a chance to attack the Republic", "Nazi propaganda blamed the Weimar politicians for the crisis and promised work and bread")]),
("Nazi propaganda on support for the party in the years 1929–32", [
 ("it spread the Nazi message across Germany", "Goebbels used posters, leaflets, rallies and films aimed at different groups"),
 ("it built up Hitler's image as a national saviour", "in 1932 Hitler toured by aeroplane in the 'Hitler over Germany' campaign"),
 ("it played on fear of communism", "the Nazis presented themselves as the only party that could stop a communist revolution")]),
("the activities of the SA on Germany in the years 1930–32", [
 ("they increased violence on the streets", "in July 1932 a clash in Altona left 18 people dead"),
 ("they frightened opponents and voters", "SA men broke up rival meetings and intimidated people at election time"),
 ("they made the Nazis seem a force for order to some Germans", "the discipline of SA marches impressed people who feared communist disorder")]),
("the presidential election of 1932 on Hitler", [
 ("it increased his national profile", "Hitler won 37 per cent of the vote in the second round against Hindenburg"),
 ("it showed the limits of his support", "Hindenburg still defeated him with 53 per cent of the vote"),
 ("it showed the Nazis' campaigning skill", "the Nazis used modern techniques such as flying Hitler to rallies across the country")]),
("the July 1932 Reichstag election on German politics", [
 ("it made the Nazis the largest party", "they won 230 seats and 37 per cent of the vote"),
 ("it made it impossible to form a majority government without them", "the Nazis and Communists together held a majority of seats"),
 ("it strengthened Hitler's claim to be Chancellor", "Hitler refused to join a government unless he led it")]),
("the role of von Papen on Hitler's appointment as Chancellor", [
 ("he persuaded Hindenburg to appoint Hitler", "Papen argued that Hitler could be controlled in a cabinet dominated by conservatives"),
 ("he helped bring down von Schleicher", "Papen negotiated secretly with Hitler in January 1933, leaving Schleicher without support"),
 ("he made Hitler's appointment look safe", "Papen became Vice-Chancellor and only three Nazis were in the first cabinet")]),
("the November 1932 Reichstag election on the Nazi Party", [
 ("it reduced the Nazi vote", "the Nazis lost two million votes and fell to 196 seats"),
 ("it caused financial and morale problems for the party", "the party was short of money and some members talked of leaving"),
 ("it encouraged the elite to try to use Hitler", "Papen and Hindenburg believed a weakened Hitler would be easier to control")]),
],
"nazi": [
("the Reichstag Fire (1933) on the Nazi Party", [
 ("it allowed the Nazis to attack the Communists", "around 4,000 Communists were arrested and their newspapers were closed"),
 ("it led to emergency powers", "Hindenburg issued the Decree for the Protection of People and State, suspending civil rights"),
 ("it helped the Nazis in the March 1933 election", "the Nazis used fear of a Communist revolution to win 288 seats")]),
("the Enabling Act (1933) on Germany", [
 ("it gave Hitler the power to make laws without the Reichstag", "the cabinet could pass laws for four years without the Reichstag's approval"),
 ("it led to the banning of other political parties", "by July 1933 the Nazis were the only legal party"),
 ("it led to the abolition of trade unions", "unions were banned in May 1933 and replaced by the German Labour Front")]),
("the Night of the Long Knives (1934) on Hitler's position", [
 ("it removed the threat from the SA", "Röhm and other SA leaders were shot and the SA lost its power"),
 ("it won the support of the army", "the army leaders, who feared the SA, agreed to swear an oath of loyalty to Hitler"),
 ("it showed that Hitler would use terror against anyone", "around 200 people were killed, including the former Chancellor von Schleicher")]),
("the death of Hindenburg (1934) on Germany", [
 ("it allowed Hitler to become Führer", "Hitler combined the posts of President and Chancellor"),
 ("it gave Hitler control of the armed forces", "soldiers swore a personal oath of loyalty to Hitler"),
 ("it removed the last check on Hitler's power", "there was no longer anyone with the authority to dismiss him")]),
("the Gestapo on the German people in the years 1933–39", [
 ("it created fear of speaking against the regime", "the Gestapo could arrest people and hold them without trial"),
 ("it led to many people being sent to concentration camps", "by 1939 around 150,000 people were held in 'protective custody'"),
 ("it encouraged people to inform on others", "many arrests came from denunciations by neighbours or workmates")]),
("Nazi censorship on Germany in the years 1933–39", [
 ("it controlled what Germans could read", "newspapers were controlled and books by Jewish and left-wing authors were burned in 1933"),
 ("it controlled culture", "the Reich Chamber of Culture decided which artists, writers and musicians could work"),
 ("it made it harder to organise opposition", "people heard only the Nazi point of view, so criticism found little audience")]),
("Nazi propaganda on the German people in the years 1933–39", [
 ("it increased support for Hitler", "rallies such as those at Nuremberg created an image of a strong, united Germany"),
 ("it spread Nazi racial ideas", "films and posters presented Jews as enemies of Germany"),
 ("it reached most homes through radio", "cheap People's Receivers meant about 70 per cent of households had a radio by 1939")]),
("Nazi policies towards women on German women in the years 1933–39", [
 ("they pushed women out of professions", "women doctors, teachers and civil servants were dismissed"),
 ("they encouraged women to have more children", "marriage loans were offered and the Mother's Cross was awarded to women with large families"),
 ("they restricted women's education and opportunities", "the number of women in universities was limited")]),
("the Hitler Youth on young people in Germany", [
 ("it spread Nazi ideas among the young", "members were taught loyalty to Hitler and Nazi racial ideas"),
 ("it prepared boys for war", "activities included marching, map reading and shooting"),
 ("it led some young people to rebel", "groups such as the Swing Youth and the Edelweiss Pirates rejected its discipline")]),
("Nazi education policies on German schools", [
 ("they changed what was taught", "race studies were introduced and history focused on German greatness"),
 ("they controlled teachers", "teachers had to join the Nazi Teachers' League and Jewish teachers were dismissed"),
 ("they increased the importance of physical education", "PE took up to five hours a week, and boys could be expelled for failing fitness tests")]),
("Nazi policies towards the Churches on Germany in the years 1933–39", [
 ("they reduced the influence of the Catholic Church", "Catholic schools and youth groups were closed despite the Concordat"),
 ("they divided the Protestant Church", "the Reich Church was set up, but the Confessing Church broke away"),
 ("they led to persecution of church leaders", "Pastor Niemöller was sent to a concentration camp and hundreds of priests were arrested")]),
("the Nuremberg Laws (1935) on Jews in Germany", [
 ("they took away the citizenship of German Jews", "Jews became 'subjects' rather than citizens"),
 ("they banned marriages between Jews and non-Jews", "the Law for the Protection of German Blood and Honour banned mixed marriages"),
 ("they encouraged emigration", "many Jews decided to leave Germany after 1935")]),
("Kristallnacht (1938) on Jews in Germany", [
 ("it caused widespread destruction of Jewish property", "about 7,500 Jewish shops were damaged and hundreds of synagogues burned"),
 ("it led to mass arrests", "around 30,000 Jewish men were sent to concentration camps"),
 ("it led to more restrictions", "Jews were fined one billion marks and were banned from owning businesses")]),
("Nazi policies to reduce unemployment on Germany in the years 1933–39", [
 ("they reduced unemployment", "official unemployment fell from about 6 million to fewer than 500,000"),
 ("they increased Germany's military strength", "rearmament and conscription from 1935 created jobs and expanded the army"),
 ("they improved Germany's roads and public buildings", "the National Labour Service built autobahns and public works")]),
("the German Labour Front (DAF) on German workers", [
 ("it removed workers' rights", "strikes were banned and wages were set by the state"),
 ("it controlled working conditions", "working hours rose to around 60 a week in some industries"),
 ("it offered rewards to keep workers loyal", "its Strength Through Joy section provided cheap holidays and leisure activities")]),
],
"war": [
("the invasion of Poland (1939) on Nazi policy towards the Jews", [
 ("it brought millions more Jews under Nazi control", "about two million Polish Jews came under German rule"),
 ("it led to the setting up of ghettos", "Jews were forced into sealed ghettos in cities such as Łódź and Warsaw"),
 ("it led to more violent persecution", "SS units carried out shootings of Jews and Polish leaders")]),
("the ghettos on Jews in occupied Poland", [
 ("they caused starvation and disease", "rations in the Warsaw ghetto were far below what was needed and thousands died each month"),
 ("they separated Jews from the rest of society", "the ghettos were sealed with walls and guarded"),
 ("they made later deportations easier", "from 1942 Jews were taken from the ghettos to death camps such as Treblinka")]),
("the Einsatzgruppen on the occupied Soviet Union", [
 ("they carried out the mass murder of Jews", "around one million Jews were shot by 1943"),
 ("they killed communist officials and others the Nazis saw as enemies", "commissars, Roma and partisans were also murdered"),
 ("they led the Nazis to look for other methods of killing", "SS leaders worried about the effect of mass shootings on their own men")]),
("the Wannsee Conference (1942) on Nazi policy towards the Jews", [
 ("it organised the Final Solution", "officials agreed how to coordinate the deportation of Europe's Jews"),
 ("it led to the use of death camps", "camps such as Treblinka, Sobibor and Auschwitz-Birkenau used gas chambers"),
 ("it led to deportations from across Europe", "Jews were transported by train from countries such as France, the Netherlands and Hungary")]),
("rationing on the German home front", [
 ("it reduced the food available to Germans", "meat, butter and sugar were rationed from 1939 and rations were cut after 1942"),
 ("it led to a black market", "people traded goods illegally to get extra food"),
 ("it treated groups unequally", "Jews and foreign workers received much lower rations")]),
("the defeat at Stalingrad (1943) on the German home front", [
 ("it led to the policy of total war", "Goebbels announced total war in February 1943"),
 ("it damaged morale", "the loss of the Sixth Army was the first defeat that propaganda could not hide"),
 ("it led to more pressure on the economy", "more men were conscripted and luxury businesses were closed")]),
("total war on Germany", [
 ("it increased weapons production", "under Speer, production of weapons tripled between 1942 and 1944"),
 ("it increased the use of forced labour", "about seven million foreign workers were working in Germany by 1944"),
 ("it reduced living standards", "shops selling luxuries were closed and working hours were increased")]),
("Allied bombing on Germany during the Second World War", [
 ("it caused heavy civilian casualties", "around 40,000 died in the Hamburg firestorm in 1943 and many thousands in Dresden in 1945"),
 ("it made many Germans homeless", "millions of people lost their homes and many were evacuated from the cities"),
 ("it disrupted industry and transport", "attacks on oil plants and railways in 1944–45 caused severe shortages")]),
("the Second World War on German women", [
 ("it increased the number of women doing war work", "from 1943 women aged 17 to 45 had to register for work"),
 ("it brought new responsibilities", "women ran homes alone, coped with bombing and worked in auxiliary services"),
 ("it showed the limits of Nazi ideas about women", "the regime had to call on women to work despite its belief that they belonged at home")]),
("the activities of the Edelweiss Pirates on Nazi Germany", [
 ("they challenged Nazi control of young people", "they rejected the Hitler Youth and attacked its patrols"),
 ("they helped people the regime wanted to catch", "some groups sheltered deserters and escaped prisoners"),
 ("they led to harsh punishments", "thirteen members were publicly hanged in Cologne in 1944")]),
("the White Rose group on Nazi Germany", [
 ("it spread criticism of the regime", "the group distributed six leaflets condemning Nazi crimes"),
 ("it led to the execution of its members", "Hans and Sophie Scholl were executed in February 1943"),
 ("it showed that some Germans were prepared to resist", "the leaflets were later dropped over Germany by the Allies")]),
("the July Bomb Plot (1944) on Nazi Germany", [
 ("it led to a wave of executions", "around 5,000 people were executed after the plot"),
 ("it increased the power of the SS", "Himmler was given greater control over the army reserve"),
 ("it showed that opposition had spread to the army", "senior officers, including Field Marshal Rommel, were linked to the plot")]),
("the advance of the Allied armies in 1944–45 on Germany", [
 ("it led to the collapse of the Nazi regime", "Soviet forces reached Berlin in April 1945 and Germany surrendered on 8 May"),
 ("it caused a refugee crisis", "millions of Germans fled west from the advancing Red Army"),
 ("it led to desperate measures", "the Volkssturm called up old men and boys to defend German towns")]),
],
}

ISSUES = {
"weimar": [
{"stems": ["‘{f} was the main reason why the Weimar Republic faced serious problems in the years 1919–23.’",
           "‘The most serious problem facing the Weimar Republic in the years 1919–23 was {f}.’"],
 "factors": [
  ("the Treaty of Versailles", [
   "The Treaty was hated as a 'Diktat' and the politicians who signed it were called the 'November Criminals', which meant the Republic lacked support from the start",
   "Reparations of £6,600 million and the loss of land such as the Saar and Upper Silesia weakened the economy",
   "Military restrictions angered the army and ex-soldiers, who joined the Freikorps and later took part in the Kapp Putsch"]),
  ("hyperinflation", [
   "By November 1923 the mark was almost worthless, and people's savings were destroyed",
   "Workers' wages could not keep up with prices, which caused hunger and anger",
   "Hyperinflation destroyed the confidence of the middle classes in the Republic"]),
  ("the threat from the left", [
   "The Spartacist uprising of January 1919 tried to create a communist state in Berlin",
   "Workers' councils and a soviet republic in Bavaria in 1919 challenged the government's authority",
   "Communist risings in the Ruhr and Saxony in 1920 and 1923 forced the government to use the army and Freikorps"]),
  ("the threat from the right", [
   "The Kapp Putsch in 1920 briefly drove the government out of Berlin",
   "Right-wing groups carried out over 350 political murders, including those of Erzberger and Rathenau",
   "Hitler's Munich Putsch in 1923 tried to seize power in Bavaria and march on Berlin"]),
  ("the French occupation of the Ruhr", [
   "The occupation of January 1923 took Germany's main industrial region",
   "Passive resistance stopped production and the government had to pay the strikers",
   "The crisis led directly to hyperinflation and nearly destroyed the Republic"]),
  ("the weaknesses of the Weimar Constitution", [
   "Proportional representation produced many small parties and unstable coalitions",
   "Article 48 gave the President power to rule by decree, which weakened the Reichstag",
   "The constitution left in place judges, civil servants and army officers who were hostile to democracy"]),
 ]},
{"stems": ["‘The main reason for the Weimar Republic's survival in the years 1919–23 was {f}.’"],
 "factors": [
  ("the support of the army", [
   "Ebert's agreement with Groener in 1918 meant the army backed the government",
   "The army and Freikorps crushed the Spartacists and communist risings",
   "The army helped stop the Munich Putsch in 1923 and communist governments in Saxony"]),
  ("the actions of German workers", [
   "The general strike in Berlin defeated the Kapp Putsch in 1920",
   "Most workers supported the Social Democrats rather than the Communists",
   "Trade unions helped keep order and backed the government in 1918–19"]),
  ("the divisions among the Republic's enemies", [
   "The left was split between Social Democrats, Independent Socialists and Communists",
   "The Spartacist rising was poorly planned and its leaders disagreed about timing",
   "Right-wing groups had no single leader and their putsches were badly organised"]),
  ("the leadership of Stresemann", [
   "In 1923 Stresemann called off passive resistance in the Ruhr",
   "He introduced the Rentenmark, which ended hyperinflation",
   "He began negotiations that led to the Dawes Plan and restored Germany's finances"]),
 ]},
{"stems": ["‘The most significant effect of the Treaty of Versailles on Germany in the years 1919–23 was {f}.’"],
 "factors": [
  ("economic damage", [
   "Reparations were fixed at £6,600 million in 1921",
   "Germany lost the Saar coalfields for 15 years and Upper Silesia's industry",
   "Failure to pay reparations led to the Ruhr occupation and hyperinflation"]),
  ("political instability", [
   "The 'stab in the back' myth made the Republic look like a traitor to Germany",
   "Right-wing groups such as the Freikorps opposed the Republic for accepting the Treaty",
   "Ministers linked to the Treaty, such as Erzberger, were assassinated"]),
  ("the loss of territory", [
   "Germany lost about 13 per cent of its land, including Alsace-Lorraine and the Polish Corridor",
   "All its colonies were taken and run as mandates",
   "Millions of German speakers now lived outside Germany, which caused anger"]),
  ("the weakening of the armed forces", [
   "The army was limited to 100,000 men and conscription was banned",
   "Germany was not allowed tanks, an air force or submarines",
   "Unemployed ex-soldiers formed the Freikorps and joined right-wing groups"]),
 ]},
],
"recovery": [
{"stems": ["‘Germany recovered between 1924 and 1929 chiefly because of {f}.’",
           "‘{f} was the most important reason for the recovery of Germany in the years 1924–29.’"],
 "factors": [
  ("the Dawes Plan", [
   "The Dawes Plan reduced annual reparations payments to a manageable level",
   "It led to American loans of 800 million marks and much more afterwards",
   "It led to the end of the occupation of the Ruhr in 1925"]),
  ("American loans", [
   "About 25 billion marks were lent to Germany between 1924 and 1930",
   "The loans paid for new factories and machinery, and industrial output passed pre-war levels by 1928",
   "Local councils used loans to build housing, schools and public facilities"]),
  ("the Rentenmark", [
   "It ended hyperinflation and stabilised prices in late 1923",
   "It restored confidence in German money and allowed trade to recover",
   "It was replaced by the gold-backed Reichsmark in 1924"]),
  ("Stresemann's foreign policy", [
   "The Locarno Treaties of 1925 improved relations with France and Britain",
   "Germany joined the League of Nations in 1926 with a permanent seat on the Council",
   "Germany signed the Kellogg-Briand Pact in 1928, which raised its standing in the world"]),
  ("the Young Plan", [
   "The Young Plan of 1929 reduced the total of reparations to £2,000 million",
   "It gave Germany 59 years to pay",
   "It led to the early withdrawal of Allied troops from the Rhineland in 1930"]),
 ]},
{"stems": ["‘The most significant success of Stresemann in the years 1923–29 was {f}.’"],
 "factors": [
  ("ending hyperinflation", [
   "Stresemann called off passive resistance in September 1923",
   "His government introduced the Rentenmark in November 1923",
   "Stable money allowed businesses and trade to recover"]),
  ("the Locarno Treaties", [
   "Germany accepted its western borders and France promised peace",
   "Germany was treated as an equal by the other great powers",
   "Stresemann shared the Nobel Peace Prize in 1926"]),
  ("membership of the League of Nations", [
   "Germany joined in 1926 and received a permanent seat on the Council",
   "It confirmed Germany's return as a great power",
   "Stresemann used the League to speak up for German minorities"]),
  ("reducing reparations", [
   "The Dawes Plan of 1924 lowered annual payments",
   "The Young Plan of 1929 cut the total and extended the period of payment",
   "Lower reparations helped the government balance its budget"]),
 ]},
{"stems": ["‘The years 1924–29 were a golden age for the Weimar Republic.’ How far do you agree? Consider {f}."],
 "factors": [],
 "skip": True},
{"stems": ["‘The main weakness of the Weimar Republic in the years 1924–29 was {f}.’"],
 "factors": [
  ("its dependence on American loans", [
   "Most of the loans were short-term and could be recalled at any time",
   "Germany used loans to pay reparations, so the debt kept growing",
   "When the Wall Street Crash came in 1929, American banks recalled the loans"]),
  ("the problems of farmers", [
   "Food prices fell in the late 1920s, so farm incomes dropped",
   "Many farmers fell into debt and some lost their land",
   "Rural areas became increasingly hostile to the Republic"]),
  ("unstable coalition governments", [
   "There were six different governments between 1924 and 1929",
   "Parties found it hard to agree on issues such as unemployment insurance",
   "The Grand Coalition under Müller collapsed in March 1930"]),
  ("continued opposition from nationalists", [
   "The Nationalists under Hugenberg campaigned against the Young Plan",
   "Hindenburg, elected President in 1925, had little loyalty to democracy",
   "Many in the army, the courts and the civil service still opposed the Republic"]),
 ]},
],
"rise": [
{"stems": ["‘The main reason why Hitler became Chancellor in January 1933 was {f}.’",
           "‘{f} was the most important reason for the Nazis' rise to power in the years 1929–33.’"],
 "factors": [
  ("the Great Depression", [
   "Unemployment reached six million by 1932, which made people desperate",
   "The Depression caused the collapse of the Müller government and rule by decree",
   "Nazi votes rose from 2.6 per cent in 1928 to 37 per cent in July 1932"]),
  ("Nazi propaganda", [
   "Goebbels ran modern campaigns using posters, films, rallies and the radio",
   "Propaganda presented Hitler as a strong leader who could save Germany",
   "Messages were aimed at specific groups, such as farmers, workers and women"]),
  ("the role of the SA", [
   "The SA had around 400,000 members by 1932",
   "It protected Nazi meetings and attacked Communists and Social Democrats",
   "Its marches and uniforms gave an image of order and strength"]),
  ("the actions of von Papen and von Hindenburg", [
   "Papen persuaded Hindenburg to appoint Hitler, believing he could be controlled",
   "Hindenburg agreed after Schleicher failed to form a stable government",
   "Only three Nazis were in the first cabinet, which made the deal seem safe"]),
  ("fear of communism", [
   "The Communist vote rose to 100 seats in November 1932",
   "Business leaders and the middle classes feared a revolution like that in Russia",
   "The Nazis presented themselves as the strongest force against communism"]),
  ("Hitler's leadership", [
   "Hitler was a powerful speaker who drew huge crowds",
   "He reorganised the party after 1924 and decided to win power legally",
   "He refused to accept the post of Vice-Chancellor in 1932, holding out for the chancellorship"]),
 ]},
{"stems": ["‘The Nazi Party held together during its lean years of 1924–28 mainly because of {f}.’"],
 "factors": [
  ("the reorganisation of the party", [
   "The party was divided into regions run by Gauleiters",
   "New organisations such as the Hitler Youth and the SS were set up",
   "Membership grew to over 100,000 by 1928"]),
  ("Hitler's leadership", [
   "Hitler was released in December 1924 and refounded the party in February 1925",
   "At the Bamberg Conference of 1926 he asserted his authority over the party",
   "Mein Kampf set out a clear set of ideas for his followers"]),
  ("the publicity from the Munich Putsch", [
   "Hitler's trial made him known across Germany",
   "The sixteen dead marchers were turned into martyrs",
   "Hitler's short, comfortable imprisonment showed the sympathy of the courts"]),
  ("the support of wealthy backers", [
   "Some industrialists and members of the elite gave money to the party",
   "Financial support paid for newspapers, rallies and staff",
   "Supporters such as the Bechstein family helped Hitler socially"]),
 ]},
{"stems": ["‘The most significant consequence of the Munich Putsch (1923) was {f}.’"],
 "factors": [
  ("the publicity it gave Hitler", [
   "Hitler's speeches at his trial were reported by newspapers throughout Germany",
   "He presented himself as a patriot who had acted against the 'November Criminals'",
   "Hitler became a national figure for the first time"]),
  ("the change in Nazi tactics", [
   "Hitler decided to win power through elections",
   "The party built a national organisation to fight elections",
   "Hitler stressed that the party must appear legal and respectable"]),
  ("the writing of Mein Kampf", [
   "In Landsberg prison Hitler wrote Mein Kampf",
   "It set out his ideas on race, living space and the Jews",
   "It gave the party a clear ideology"]),
  ("the banning of the party", [
   "The party was banned until 1925",
   "Without Hitler, the movement split into rival groups",
   "Its vote in 1924 was small and it struggled to recover"]),
 ]},
],
"nazi": [
{"stems": ["‘Hitler turned his chancellorship into a dictatorship by August 1934 mainly because of {f}.’",
           "‘{f} was the decisive step in building Hitler's dictatorship between January 1933 and August 1934.’"],
 "factors": [
  ("the Reichstag Fire", [
   "The fire allowed Hitler to claim there was a communist plot",
   "The emergency decree of February 1933 suspended civil rights",
   "Thousands of Communists were arrested before the March election"]),
  ("the Enabling Act", [
   "The Act allowed Hitler to pass laws without the Reichstag for four years",
   "It was used to ban trade unions and other political parties",
   "It gave Hitler's rule an appearance of legality"]),
  ("the Night of the Long Knives", [
   "Röhm and other SA leaders were killed, removing a rival source of power",
   "The army was reassured and backed Hitler",
   "It showed that Hitler would murder opponents"]),
  ("the death of Hindenburg", [
   "Hitler combined the posts of President and Chancellor as Führer in August 1934",
   "The army swore an oath of personal loyalty to Hitler",
   "There was no longer anyone who could dismiss Hitler"]),
  ("the use of terror by the SA and SS", [
   "The SA and SS intimidated opponents during the March 1933 election",
   "The first concentration camp opened at Dachau in March 1933",
   "Opponents were beaten and imprisoned without trial"]),
 ]},
{"stems": ["‘The most significant method of control used by the Nazis in the years 1933–39 was {f}.’",
           "‘{f} was the main reason why the Nazis faced little opposition in the years 1933–39.’"],
 "factors": [
  ("the Gestapo", [
   "The Gestapo could arrest and hold people without trial",
   "It relied on denunciations from ordinary Germans",
   "Fear of the Gestapo stopped many people from speaking out"]),
  ("the SS and concentration camps", [
   "The SS, led by Himmler, controlled the police and security services",
   "Concentration camps such as Dachau held political opponents",
   "Camps were used to frighten others into obedience"]),
  ("propaganda", [
   "Goebbels' Ministry of Propaganda controlled radio, film and newspapers",
   "Events such as the Nuremberg rallies and the 1936 Olympics celebrated the regime",
   "Propaganda created a 'Hitler myth' of a leader who was above criticism"]),
  ("censorship", [
   "Newspapers were controlled and opposition newspapers were closed",
   "Books by banned authors were burned in May 1933",
   "Art, music and films had to fit Nazi ideas"]),
  ("policies that won popular support", [
   "Unemployment fell from six million to almost nothing by 1939",
   "Strength Through Joy offered workers cheap holidays and leisure",
   "Foreign policy successes, such as the Rhineland in 1936, were popular"]),
 ]},
{"stems": ["‘Nazi policies had the most significant impact on {f} in the years 1933–39.’"],
 "factors": [
  ("young people", [
   "Membership of the Hitler Youth became compulsory in 1939",
   "Schools taught race studies and loyalty to Hitler",
   "Some young people rebelled, forming groups such as the Swing Youth"]),
  ("women", [
   "Women were encouraged to follow the 'three Ks' of children, kitchen and church",
   "Women in professions such as medicine and the civil service were dismissed",
   "Marriage loans and the Mother's Cross encouraged larger families"]),
  ("the Jews", [
   "The Nuremberg Laws of 1935 took away citizenship",
   "Kristallnacht in 1938 led to destruction of property and 30,000 arrests",
   "Jews were excluded from professions and their businesses were taken"]),
  ("workers", [
   "Trade unions were abolished and replaced by the Labour Front",
   "Unemployment fell sharply because of public works and rearmament",
   "Strength Through Joy and Beauty of Labour aimed to keep workers content"]),
  ("the Churches", [
   "The Concordat of 1933 was broken and Catholic schools and youth groups closed",
   "The Reich Church was created under Bishop Müller",
   "Pastors such as Niemöller were sent to concentration camps"]),
 ]},
],
"war": [
{"stems": ["‘The most significant impact of the Second World War on the German home front was {f}.’",
           "‘During the Second World War, {f} had the greatest effect on the lives of ordinary Germans.’"],
 "factors": [
  ("Allied bombing", [
   "Raids on cities such as Hamburg, Cologne and Dresden killed hundreds of thousands of civilians",
   "Millions of homes were destroyed and people were evacuated",
   "Bombing damaged transport and industry, especially in 1944–45"]),
  ("rationing", [
   "Food and clothing were rationed from 1939",
   "Rations were cut after 1942 and a black market developed",
   "Shortages worsened in the last year of the war"]),
  ("total war", [
   "Goebbels declared total war in 1943",
   "Luxury shops and places of entertainment were closed",
   "Speer's reorganisation increased working hours and production"]),
  ("the changing role of women", [
   "From 1943 women aged 17 to 45 had to register for war work",
   "Women ran homes and families alone while men were away",
   "Many women served in auxiliary roles, such as anti-aircraft units"]),
  ("the use of foreign forced labour", [
   "By 1944 about seven million foreign workers were in Germany",
   "Forced labourers worked in factories and on farms across the country",
   "They were treated harshly and given poor rations"]),
 ]},
{"stems": ["‘The main reason for the weakening of Nazi control in Germany in the years 1939–45 was {f}.’"],
 "factors": [
  ("opposition from young people", [
   "The Edelweiss Pirates attacked Hitler Youth patrols and sheltered deserters",
   "The Swing Youth rejected Nazi values in music and dress",
   "The White Rose students distributed leaflets against the regime"]),
  ("the July Bomb Plot", [
   "Army officers led by Stauffenberg tried to kill Hitler in July 1944",
   "The plot showed that opposition had spread to the military elite",
   "The plotters hoped to make peace with the Allies"]),
  ("military defeats", [
   "The defeat at Stalingrad in 1943 destroyed the image of German invincibility",
   "Allied armies invaded from the west and the east in 1944",
   "By April 1945 Soviet troops were fighting in Berlin"]),
  ("Allied bombing", [
   "Bombing damaged war production and transport",
   "It destroyed homes and forced millions to move",
   "It made it harder for propaganda to claim the war was going well"]),
 ]},
{"stems": ["‘The most significant development in Nazi policy towards the Jews in the years 1939–45 was {f}.’"],
 "factors": [
  ("the creation of the ghettos", [
   "Jews in Poland were forced into ghettos from 1939–40",
   "Starvation and disease killed hundreds of thousands",
   "The ghettos concentrated Jews for later deportation"]),
  ("the work of the Einsatzgruppen", [
   "Death squads followed the invasion of the Soviet Union in 1941",
   "Massacres such as Babi Yar killed tens of thousands at a time",
   "About one million Jews were shot by 1943"]),
  ("the Wannsee Conference", [
   "In January 1942 officials organised the Final Solution",
   "It coordinated the deportation of Jews from all over Europe",
   "It led to the systematic use of death camps"]),
  ("the death camps", [
   "Camps such as Auschwitz-Birkenau and Treblinka used gas chambers",
   "Around six million Jews were murdered in the Holocaust",
   "Prisoners who were not killed at once were used as slave labour"]),
 ]},
],
}
