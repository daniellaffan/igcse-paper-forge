"""Original content for Paper 2 Section A investigation: Russia and the Soviet Union, 1905-24.

Every source below is an ORIGINAL text written for this project, attributed to an invented,
unnamed person of the period (a worker, an officer, a diplomat and so on). Every extract is
an original text written in the style of a modern history book. Nothing is copied.

FEATURES[sub]  = list of (topic phrase, [(feature, supporting detail), ...])
CLUSTERS[sub]  = list of clusters:
   {"focus": phrase used in "about ...",
    "aspects": {key: {"+": what the source suggests, "-": the opposite}},
    "sources": [(attribution, text, {aspect: (stance, evidence)}), x4],
    "extracts": [(attribution, text, [view, ...]), x2]}
   view = {"view": statement, "pro": {aspect: stance}, "ext": [what the extract says],
           "alt": {aspect: stance} (optional: a source taking this stance points to a DIFFERENT factor, so it
                  challenges the view; any other stance on that aspect is irrelevant and omitted),
           "own_for": [...], "own_against": [...]}
   Only aspects that bear on the view go in "pro"/"alt"; all other source points are left out of its
   indicative content. Own knowledge "against" must not repeat a point the extract itself makes.
"""

FEATURES = {
"tsarist": [
("the Tsar's system of government before 1905", [
 ("The Tsar was an autocrat who ruled without an elected parliament", "Nicholas II believed he had been chosen by God to rule"),
 ("The Okhrana, the secret police, watched and arrested opponents", "suspected revolutionaries could be exiled to Siberia without trial"),
 ("The Tsar relied on the army, the Church and the nobility", "the Orthodox Church taught that obedience to the Tsar was a duty")]),
("Bloody Sunday (January 1905)", [
 ("It was a peaceful march of workers to the Winter Palace", "the marchers, led by Father Gapon, carried icons and pictures of the Tsar"),
 ("Troops opened fire on the crowd", "estimates of the dead range from about 100 to several hundred"),
 ("It damaged the image of the Tsar as the 'Little Father' of his people", "strikes spread across Russia in the following weeks")]),
("the October Manifesto (1905)", [
 ("It promised an elected parliament, the Duma", "no law was to be passed without the Duma's agreement"),
 ("It promised civil rights", "these included freedom of speech, assembly and religion"),
 ("It split the opposition", "liberals such as the Octobrists accepted it, while socialists rejected it")]),
("the Dumas (1906–14)", [
 ("The Tsar limited the Duma's powers with the Fundamental Laws of 1906", "the Tsar kept control of the army and foreign policy and could dissolve the Duma"),
 ("The first two Dumas were dissolved quickly", "the Tsar closed them because they were too critical of the government"),
 ("The voting system was changed to favour the wealthy", "the Third Duma was dominated by landowners and loyal parties")]),
("Stolypin's policies (1906–11)", [
 ("He crushed opposition with harsh repression", "so many rebels were hanged that the noose became known as 'Stolypin's necktie'"),
 ("He introduced land reforms", "peasants were allowed to leave the commune and own their land"),
 ("He encouraged peasants to resettle in Siberia", "around 3 million moved east with government help")]),
("the Lena Goldfields Massacre (1912)", [
 ("Miners went on strike over pay and conditions", "they complained about long hours and poor food"),
 ("Troops fired on the strikers", "around 150 to 270 miners were killed"),
 ("It led to a wave of strikes", "strikes rose sharply in 1912–14, including a general strike in St Petersburg in 1914")]),
("opposition groups in Russia before 1914", [
 ("The Social Democrats followed the ideas of Marx", "they split in 1903 into Bolsheviks and Mensheviks"),
 ("The Socialist Revolutionaries wanted land for the peasants", "some of them used terrorism, assassinating officials"),
 ("The Kadets were liberals who wanted a constitutional monarchy", "they were supported mainly by the middle class")]),
],
"war-feb": [
("the effects of the First World War on the Russian army", [
 ("The army suffered heavy defeats", "it was beaten at Tannenberg and the Masurian Lakes in 1914"),
 ("Soldiers were badly equipped", "some were sent to the front without rifles or boots"),
 ("Casualties were enormous", "by 1917 around 1.7 million Russian soldiers had been killed")]),
("the effects of the war on the Russian home front", [
 ("There were shortages of food and fuel in the cities", "the railways were used for the army, so supplies did not reach Petrograd"),
 ("Prices rose sharply", "the government printed money to pay for the war, causing inflation"),
 ("Workers faced long hours in factories", "women increasingly worked in factories while men were at the front")]),
("Rasputin", [
 ("He was a peasant holy man who claimed healing powers", "he seemed to help the Tsar's son, Alexis, who had haemophilia"),
 ("He had great influence over the Tsarina", "he was said to advise her on the appointment of ministers"),
 ("He damaged the reputation of the royal family", "he was murdered by a group of nobles in December 1916")]),
("the Tsar's decision to take command of the army (1915)", [
 ("Nicholas II went to army headquarters", "he left the Tsarina in charge of the government in Petrograd"),
 ("He was blamed personally for defeats", "he had little military experience"),
 ("Government at home became chaotic", "ministers were frequently changed, partly on Rasputin's advice")]),
("the February Revolution (1917)", [
 ("It began with protests in Petrograd", "women queuing for bread joined striking workers on International Women's Day"),
 ("Soldiers joined the protesters", "regiments in the Petrograd garrison mutinied and refused to fire on the crowds"),
 ("The Tsar abdicated", "Nicholas II gave up the throne on 2 March 1917")]),
("the setting up of the Provisional Government (1917)", [
 ("It was formed by members of the Duma", "its first leader was Prince Lvov"),
 ("It was meant to rule until elections", "elections were to be held for a Constituent Assembly"),
 ("It introduced reforms", "it allowed freedom of speech and released political prisoners")]),
],
"provisional": [
("the Petrograd Soviet (1917)", [
 ("It was elected by workers and soldiers", "it met in the Tauride Palace, the same building as the Provisional Government"),
 ("It issued Order Number One", "soldiers were to obey only orders that the Soviet approved"),
 ("It shared power with the Provisional Government", "this arrangement was known as Dual Power")]),
("the April Theses (1917)", [
 ("Lenin demanded 'All power to the Soviets'", "he refused to cooperate with the Provisional Government"),
 ("He called for an end to the war", "this appealed to soldiers and their families"),
 ("He promised 'Peace, Bread and Land'", "the slogan offered solutions to the main problems facing Russia")]),
("the July Days (1917)", [
 ("Soldiers and workers demonstrated against the government in Petrograd", "many demanded that the Soviet take power"),
 ("The government used loyal troops to restore order", "the demonstrations were broken up"),
 ("The Bolsheviks were blamed", "Lenin fled to Finland and other leaders such as Trotsky were arrested")]),
("the Kornilov Affair (1917)", [
 ("Kornilov, the army commander, marched troops towards Petrograd", "Kerensky feared a military takeover"),
 ("Kerensky armed the Red Guards to defend the city", "the Bolsheviks were given weapons"),
 ("Kornilov's troops were persuaded not to fight", "railway workers stopped trains and Bolshevik agitators talked to the soldiers")]),
("the Bolshevik seizure of power (October 1917)", [
 ("It was organised by the Military Revolutionary Committee", "Trotsky planned the takeover"),
 ("Red Guards seized key points in Petrograd", "they took bridges, railway stations and the telephone exchange"),
 ("The Winter Palace was taken", "the members of the Provisional Government were arrested")]),
("weaknesses of the Provisional Government", [
 ("It continued the war", "the June Offensive of 1917 was a disaster"),
 ("It delayed land reform", "it said the Constituent Assembly should decide"),
 ("It shared power with the Soviet", "it could not rely on the soldiers in Petrograd")]),
],
"civil-war": [
("the early decrees of the Bolshevik government (1917)", [
 ("The Decree on Land gave land to the peasants", "estates of nobles and the Church were taken without compensation"),
 ("The Decree on Peace called for an end to the war", "it proposed peace without annexations"),
 ("Workers were given more control", "an eight-hour working day was introduced")]),
("the Constituent Assembly (1918)", [
 ("Elections were held in November 1917", "the Socialist Revolutionaries won the most seats"),
 ("The Bolsheviks won only about a quarter of the seats", "they won 175 seats compared to the SRs' 370"),
 ("Lenin closed it after one day", "Red Guards prevented members from returning in January 1918")]),
("the Treaty of Brest-Litovsk (1918)", [
 ("Russia made peace with Germany", "the treaty was signed in March 1918"),
 ("Russia lost a great deal of land", "it lost Ukraine, Finland, Poland and the Baltic states"),
 ("Russia lost people and resources", "it lost about a third of its population and much of its coal and iron")]),
("the Cheka", [
 ("It was the Bolshevik secret police", "it was set up in December 1917 under Felix Dzerzhinsky"),
 ("It carried out the Red Terror", "thousands of suspected enemies were executed in 1918"),
 ("It arrested opponents of all kinds", "these included nobles, priests and rival socialists")]),
("the Whites in the Civil War", [
 ("They were a mixture of different groups", "they included monarchists, liberals and some socialists"),
 ("They had several leaders", "these included Kolchak in Siberia and Denikin in the south"),
 ("They received foreign help", "Britain, France, the USA and Japan sent troops and supplies")]),
("the Red Army", [
 ("It was built up by Trotsky", "it grew to around 5 million men by 1920"),
 ("It used former Tsarist officers", "they were watched by political commissars"),
 ("It controlled central Russia", "it held the main railways and industrial cities")]),
],
"nep": [
("War Communism (1918–21)", [
 ("Grain was taken from the peasants by force", "armed squads requisitioned food for the cities and the army"),
 ("Industry was nationalised", "the state took over all large factories"),
 ("Private trade was banned", "workers were paid partly in food rations")]),
("the Kronstadt Rising (1921)", [
 ("Sailors at the Kronstadt naval base rebelled", "they had once been strong supporters of the Bolsheviks"),
 ("They demanded more freedom", "they called for free elections to the soviets and free speech"),
 ("The rising was crushed", "the Red Army attacked across the ice and thousands were killed or executed")]),
("the New Economic Policy (1921)", [
 ("Requisitioning was replaced by a tax in kind", "peasants could sell their surplus grain"),
 ("Small businesses could be privately owned", "private shops and markets returned"),
 ("The state kept control of large industries", "Lenin called these the 'commanding heights' of the economy")]),
("opposition to the NEP", [
 ("Many Bolsheviks saw it as a betrayal of communism", "they disliked the return of private profit"),
 ("They disliked the Nepmen", "these traders became wealthy by buying and selling goods"),
 ("Lenin defended it as a temporary retreat", "he banned factions within the party to stop criticism")]),
("the famine of 1921", [
 ("It followed drought and requisitioning", "the Volga region was badly affected"),
 ("Millions died", "around 5 million people are thought to have died"),
 ("Foreign aid was accepted", "the American Relief Administration fed millions")]),
("the Bolshevik state by 1924", [
 ("Russia was a one-party state", "other parties had been banned"),
 ("The USSR was created in 1922", "it brought together Russia and other Soviet republics"),
 ("The economy had begun to recover", "grain and industrial production rose under the NEP")]),
],
}

CLUSTERS = {
"tsarist": [
{"focus": "the condition of Russian workers before 1914",
 "aspects": {
   "poor": {"+": "workers' living and working conditions were very poor", "-": "some workers were treated reasonably well"},
   "anger": {"+": "workers were discontented and some wanted to strike", "-": "workers were loyal or unwilling to protest"},
   "gov": {"+": "the authorities treated workers as a threat to be controlled", "-": "the government was trying to help workers"}},
 "sources": [
  ("From a letter written by a textile worker in St Petersburg to her brother in the countryside, 1907.",
   "We sleep twelve to a room in the barracks next to the mill, and the air is so thick you can hardly breathe. "
   "The foreman fines us for talking and for every broken thread. Some of the men say we should strike again "
   "as we did in 1905, but I am afraid. They say the police have lists of all our names.",
   {"poor": ("+", "twelve people sleep in one room and workers are fined"),
    "anger": ("+", "some men want to strike again"),
    "gov": ("+", "she has heard that the police have lists of all the workers' names")}),
  ("From a report by a factory inspector employed by the government, 1910.",
   "In the larger works of the capital there has been some improvement. Hours have been reduced in several "
   "factories, and a few owners have built schools and clinics. Nonetheless, the barracks remain crowded "
   "and dirty, and wages have not kept pace with the price of bread. I fear that discontent is growing "
   "among the younger men.",
   {"poor": ("+", "the barracks are crowded and dirty and wages are low"),
    "anger": ("+", "discontent is growing among younger workers")}),
  ("From the diary of a factory owner in Moscow, 1912.",
   "The agitators are at work again. Since the shooting at the Lena goldfields, my men talk of nothing but "
   "strikes. Yet I pay better than most, and the government has now introduced insurance for sickness and "
   "accidents. The workers do not seem grateful. I shall ask the governor to send more police.",
   {"poor": ("-", "he claims he pays better than most"),
    "anger": ("+", "the men talk of nothing but strikes"),
    "gov": ("-", "the government has introduced sickness and accident insurance")}),
  ("From a leaflet produced by a revolutionary group and handed out in St Petersburg, 1913.",
   "Comrades! While the factory owners grow fat, our children go hungry. We work eleven hours a day for "
   "wages that will not buy enough bread. The Tsar's Duma does nothing for us. The workers of Lena were "
   "shot like dogs. Join the strike! Only our own strength will change our lives.",
   {"poor": ("+", "children go hungry and wages do not buy enough bread"),
    "anger": ("+", "it calls workers to join the strike"),
    "gov": ("+", "it says the Duma does nothing for workers and that the Lena miners were shot")}),
 ],
 "extracts": [
  ("From a modern history of Russia, published in 2012.",
   "By 1914 the Tsarist regime faced a serious threat from the cities. The number of strikes had risen "
   "every year since 1911, and in the summer of 1914 barricades went up in St Petersburg. The government "
   "made a few reforms, such as sickness insurance, but relied mostly on the police and the army. Many "
   "workers had concluded that peaceful protest was useless.",
   [{"view": "by 1914 Russian workers had become a serious threat to Tsarist rule",
     "pro": {"anger": "+"},
     "ext": ["strikes rose every year after 1911", "barricades went up in St Petersburg in 1914"],
     "own_for": ["Over a million workers took part in strikes in the first half of 1914", "The Bolsheviks gained support among workers, winning control of several trade unions", "The Lena Goldfields Massacre of 1912 caused widespread anger"],
     "own_against": ["The outbreak of war in August 1914 brought a wave of patriotism and the strikes ended", "The army remained loyal and could still crush unrest", "The revolutionary parties were small and their leaders, such as Lenin, were in exile"]},
    {"view": "the government relied mainly on force rather than reform to deal with workers' discontent",
     "pro": {"gov": "+"},
     "ext": ["the government made only a few reforms", "it relied mostly on the police and the army"],
     "own_for": ["The Lena miners were shot by troops in 1912", "The Okhrana continued to arrest and exile trade union leaders", "Stolypin had used harsh repression after 1906"],
     "own_against": ["Sickness and accident insurance was introduced in 1912", "Trade unions were legalised in 1906", "The Dumas gave some limited representation"]},
    {"view": "most workers believed that peaceful protest was useless by 1914",
     "pro": {"anger": "+"},
     "ext": ["many workers had concluded that peaceful protest was useless"],
     "own_for": ["Strikes became more political after 1912", "Bolshevik support grew among workers", "Workers remembered Bloody Sunday and the Lena shootings"],
     "own_against": ["Many workers were not involved in politics", "Many joined the army enthusiastically in 1914", "Moderate parties such as the Mensheviks still had support"]}]),
  ("From a study of Russian society, published in 2006.",
   "It is easy to exaggerate the misery of Russian workers before the war. Industry was growing fast, and "
   "wages in some trades rose. The government introduced insurance schemes, and trade unions were legal, "
   "if closely watched. Most strikes were about pay, not politics. Had war not come in 1914, the regime "
   "might well have survived.",
   [{"view": "the condition of workers before 1914 has been exaggerated",
     "pro": {"poor": "-", "gov": "-"},
     "ext": ["industry was growing and some wages rose", "insurance schemes were introduced"],
     "own_for": ["Industrial output grew rapidly between 1908 and 1914", "Trade unions were legalised in 1906", "Insurance laws were passed in 1912"],
     "own_against": ["Living conditions in factory barracks remained overcrowded", "Wages fell behind rising prices", "The Lena Goldfields strike showed the harsh conditions in some industries"]},
    {"view": "the Tsarist regime could have survived if war had not broken out in 1914",
     "pro": {"anger": "-"},
     "ext": ["most strikes were about pay, not politics", "the regime might well have survived without war"],
     "own_for": ["The army and police remained loyal before 1914", "Stolypin's reforms had reduced peasant unrest", "Revolutionary leaders were in exile and the parties were divided"],
     "own_against": ["Strikes were rising sharply in 1914", "The Tsar refused to share power with the Duma", "Opposition among workers and liberals was growing"]},
    {"view": "the government was making real efforts to improve the lives of workers before 1914",
     "pro": {"gov": "-"},
     "ext": ["the government introduced insurance schemes", "trade unions were legal"],
     "own_for": ["Insurance for sickness and accidents was introduced in 1912", "Factory inspectors reported on conditions", "Trade unions had been legalised in 1906"],
     "own_against": ["Unions were closely watched and often closed down", "Troops were used against strikers, as at Lena in 1912", "Hours remained long and housing poor"]}]),
 ]},
{"focus": "the effects of the 1905 Revolution",
 "aspects": {
   "change": {"+": "the Tsar made real concessions", "-": "the Tsar's concessions changed little"},
   "split": {"+": "the opposition was divided", "-": "the opposition remained united"},
   "force": {"+": "the regime used force against its opponents", "-": "the regime did not need to use force"},
   "power": {"+": "the Tsar kept his power", "-": "the Tsar gave up real power"},
   "duma": {"+": "a Duma was set up", "-": "no real parliament was granted"}},
 "sources": [
  ("From the memoirs of a liberal member of the First Duma, published in 1922.",
   "When the Manifesto was published in October 1905, we believed that Russia had become a constitutional "
   "state at last. Our joy did not last. Within months the Tsar had issued laws that left him master of "
   "the army, the ministers and the purse. When we criticised his government, he simply sent us home.",
   {"change": ("-", "the liberals' belief that Russia had become a constitutional state did not last"),
    "power": ("+", "the Tsar issued laws leaving him master of the army, ministers and purse, and sent the Duma home when it criticised him"),
    "duma": ("+", "the liberals sat in the new Duma and criticised the government")}),
  ("From a letter written by an army officer serving in Moscow, December 1905.",
   "We have cleared the Presnya district street by street. The workers fought well behind their barricades, "
   "but they could not stand against artillery. Hundreds are dead. The Manifesto satisfied the lawyers and "
   "professors, and so the workers fought alone. The Tsar owes his throne to the army.",
   {"force": ("+", "the army crushed the Moscow rising with artillery"),
    "change": ("+", "the Manifesto was enough to satisfy the lawyers and professors"),
    "split": ("+", "once the middle classes were satisfied, the workers fought alone"),
    "power": ("+", "it says the Tsar owes his throne to the army")}),
  ("From a speech by a socialist at a workers' meeting in St Petersburg, November 1905.",
   "The Manifesto is a trick! The Tsar promises freedom with one hand and sends his Cossacks with the other. "
   "The liberals have run off to celebrate, but we will not be fooled. The Soviet must continue the "
   "struggle until the autocracy is destroyed.",
   {"change": ("-", "it calls the Manifesto a trick"),
    "split": ("+", "the liberals have gone to celebrate while the socialists continue"),
    "force": ("+", "the Tsar sends his Cossacks"),
    "power": ("+", "the struggle must go on until the autocracy is destroyed")}),
  ("From a government statement published in newspapers, October 1906.",
   "His Majesty has granted his people the Duma and the freedoms of speech and assembly. Order has been "
   "restored throughout the empire. Those who used these freedoms to spread violence have been punished, "
   "and loyal subjects may now look forward to peace and progress.",
   {"change": ("+", "the freedoms of speech and assembly have been granted"),
    "duma": ("+", "His Majesty has granted his people the Duma"),
    "force": ("+", "those who spread violence have been punished")}),
 ],
 "extracts": [
  ("From a history of the Romanov dynasty, published in 2015.",
   "The Tsar survived 1905 because his enemies were divided and his army stayed loyal. The October Manifesto "
   "gave the liberals what they wanted, or seemed to, and so the middle classes deserted the revolution. "
   "The workers and peasants were then crushed one group at a time. The promises of 1905 were soon taken back.",
   [{"view": "the Tsar survived the 1905 Revolution mainly because his opponents were divided",
     "pro": {"split": "+"},
     "alt": {"force": "+"},
     "ext": ["his enemies were divided", "the middle classes deserted the revolution"],
     "own_for": ["The Octobrists and Kadets accepted the Manifesto", "Peasants, workers and liberals had different aims", "The St Petersburg Soviet was isolated and arrested in December 1905"],
     "own_against": ["A large French loan in 1906 let the government pay its army and officials", "The end of the war with Japan allowed troops to return", "Stolypin's repression crushed peasant revolts"]},
    {"view": "the Tsar's concessions in 1905 were not genuine",
     "pro": {"change": "-", "power": "+"},
     "ext": ["the Manifesto only seemed to give the liberals what they wanted", "the promises were soon taken back"],
     "own_for": ["The Fundamental Laws of 1906 confirmed the Tsar's autocratic power", "The first two Dumas were dissolved", "The electoral law was changed in 1907"],
     "own_against": ["The Duma continued to meet until 1917", "Trade unions and political parties became legal", "Censorship was relaxed"]},
    {"view": "the use of force was the main reason the regime survived 1905",
     "pro": {"force": "+"},
     "alt": {"split": "+", "change": "+"},
     "ext": ["the army stayed loyal", "workers and peasants were crushed one group at a time"],
     "own_for": ["Troops crushed the Moscow rising in December 1905", "Punitive expeditions were sent to the countryside", "Stolypin's courts executed many rebels"],
     "own_against": ["Witte persuaded the Tsar to make concessions rather than rely on force alone", "The Peasant Land Bank and cancellation of redemption payments reduced peasant anger", "Peace with Japan reduced discontent"]}]),
  ("From a study of Russian politics, published in 2003.",
   "The events of 1905 changed Russia more than is often admitted. For the first time, Russians could vote, "
   "form parties and trade unions, and read newspapers that criticised the government. The Duma, however weak, "
   "became a place where ministers were questioned in public. The autocracy would never be quite the same again.",
    [{"view": "the 1905 Revolution brought real change to Russia",
     "pro": {"change": "+", "power": "-"},
     "ext": ["Russians could vote and form parties and trade unions", "ministers were questioned in public"],
     "own_for": ["Four Dumas met between 1906 and 1917", "Trade unions were legalised in 1906", "Newspapers could criticise the government more openly"],
     "own_against": ["The Fundamental Laws gave the Tsar power to dissolve the Duma and rule by decree", "The voting system was changed to favour landowners", "The Okhrana continued to arrest opponents"]},
    {"view": "the creation of the Duma was a significant change in how Russia was ruled",
     "pro": {"change": "+", "duma": "+", "power": "-"},
     "ext": ["the Duma, however weak, was a place where ministers were questioned"],
     "own_for": ["The Third Duma passed laws on education and insurance", "The Duma criticised Rasputin and the conduct of the war", "Duma members formed the Provisional Government in 1917"],
     "own_against": ["The first and second Dumas lasted only a few months", "The Tsar kept control of ministers", "The Third and Fourth Dumas were dominated by loyal landowners"]},
    {"view": "after 1905 the Tsar could no longer rule as a complete autocrat",
     "pro": {"change": "+", "power": "-"},
     "ext": ["the autocracy would never be quite the same again"],
     "own_for": ["The Tsar had to work with an elected Duma", "Political parties operated openly", "Public criticism of the government increased"],
     "own_against": ["Nicholas II still called himself autocrat in the Fundamental Laws", "He appointed and dismissed ministers freely", "He ignored the Duma's advice during the war"]}]),
 ]},
],
"war-feb": [
{"focus": "conditions in Russia during the First World War",
 "aspects": {
   "food": {"+": "there were serious food shortages", "-": "food was still available, at least to the wealthy"},
   "army": {"+": "the army was badly led and equipped", "-": "the army was performing well"},
   "blame": {"+": "the royal family was blamed", "-": "people remained loyal to the Tsar"},
   "loss": {"+": "the war brought heavy losses or sacrifices for Russians", "-": "the war cost Russia little"}},
 "sources": [
  ("From a letter written by a soldier at the front to his family, 1915.",
   "We were sent forward with one rifle for every three men and told to pick up the weapons of the dead. "
   "The Germans have big guns that fire all day. Our officers drink and gamble while we starve on black bread. "
   "The men say that the Tsar's German wife is betraying us.",
   {"army": ("+", "one rifle for every three men and officers who drink and gamble"),
    "food": ("+", "the soldiers starve on black bread"),
    "blame": ("+", "the men say the Tsar's German wife is betraying them"),
    "loss": ("+", "soldiers are told to pick up the weapons of the dead")}),
  ("From a police report on the mood in Petrograd, October 1916.",
   "The price of bread has risen fourfold since the start of the war. Women stand in queues all night and "
   "often go home with nothing, while every week brings new lists of the dead from the front. Workers speak openly against the Tsar and the Tsarina. There is a real "
   "danger that hunger will lead to riots.",
   {"food": ("+", "bread has risen fourfold in price and women go home with nothing"),
    "loss": ("+", "every week brings new lists of the dead"),
    "blame": ("+", "workers speak openly against the Tsar and Tsarina")}),
  ("From the diary of a wealthy woman living in Petrograd, January 1917.",
   "We dined at the Bear restaurant last night and the food was as good as ever, though dearer. People talk "
   "of nothing but Rasputin's murder, and everyone has lost someone at the front. Everyone agrees that the Empress has ruined the government. Even the "
   "Grand Dukes say Nicholas must make changes.",
   {"food": ("-", "she dined well at a restaurant, though food was dearer"),
    "blame": ("+", "everyone agrees the Empress has ruined the government"),
    "loss": ("+", "everyone has lost someone at the front")}),
  ("From an official army newspaper, 1916.",
   "Our brave troops under General Brusilov have broken the Austrian lines and taken hundreds of thousands "
   "of prisoners. The war demands great sacrifices from every family, but new factories now supply shells in great numbers. The nation stands united behind its "
   "Emperor, who shares the hardships of his soldiers at the front.",
   {"army": ("-", "Brusilov's troops broke the Austrian lines and shells are now supplied"),
    "blame": ("-", "the nation stands united behind the Emperor"),
    "loss": ("+", "the war demands great sacrifices from every family")}),
 ],
 "extracts": [
  ("From a history of Russia in the First World War, published in 2014.",
   "The war did not cause the collapse of the Tsarist regime, but it exposed every weakness. Defeat at the "
   "front, shortages at home and scandal at court came together in the winter of 1916–17. By taking command "
   "of the army, Nicholas made himself personally responsible for every failure.",
   [{"view": "the war exposed the weaknesses of the Tsarist regime",
     "pro": {"army": "+", "food": "+", "blame": "+"},
     "ext": ["defeat, shortages and scandal came together", "the war exposed every weakness"],
     "own_for": ["Russia lost heavily at Tannenberg in 1914", "Railways could not supply both the army and the cities", "Inflation caused by printing money hit workers hard"],
     "own_against": ["Russia's armies did well in the Brusilov Offensive of 1916", "Shell production had improved by 1916", "Problems such as the Tsar's refusal to share power existed before the war"]},
    {"view": "the Tsar's decision to take command of the army was a serious mistake",
     "pro": {"blame": "+", "army": "+"},
     "ext": ["Nicholas made himself personally responsible for every failure"],
     "own_for": ["He took command in September 1915 and was blamed for later defeats", "He left the Tsarina and Rasputin in charge in Petrograd", "Ministers were changed frequently in his absence"],
     "own_against": ["The army's performance improved in 1916", "Shortages at home were caused by transport problems, not his command", "Opposition to the Tsar existed before 1915"]},
    {"view": "the combination of problems in 1916–17 made the fall of the Tsar likely",
     "pro": {"food": "+", "blame": "+", "army": "+"},
     "ext": ["defeat, shortages and scandal came together in the winter of 1916–17"],
     "own_for": ["Food shortages in Petrograd were severe in early 1917", "Rasputin's murder in December 1916 showed even nobles had turned against the court", "The Duma's Progressive Bloc demanded a new government"],
     "own_against": ["The army had stayed loyal until February 1917", "The revolution began unexpectedly with bread queues", "Revolutionary parties did not plan the February Revolution"]}]),
  ("From a study of the Russian army, published in 2009.",
   "The Russian army of 1916 was far from beaten. Its supply of shells had improved, and the Brusilov "
   "Offensive was one of the most successful attacks of the war. The real problem lay behind the lines, in "
   "the cities, where transport broke down and hunger turned workers against the government.",
   [{"view": "the Russian army was not the main cause of the regime's problems",
     "pro": {"army": "-", "food": "+"},
     "ext": ["the army of 1916 was far from beaten", "the real problem lay behind the lines"],
     "own_for": ["The Brusilov Offensive captured large numbers of prisoners", "Shell production rose sharply by 1916", "Hunger in Petrograd caused the protests of February 1917"],
     "own_against": ["Millions of soldiers had been killed or captured by 1917", "Desertion was rising", "The Petrograd garrison mutinied in February 1917"]},
    {"view": "shortages in the cities were the main cause of opposition to the government",
     "pro": {"food": "+"},
     "alt": {"army": "+"},
     "ext": ["transport broke down and hunger turned workers against the government"],
     "own_for": ["Bread queues in Petrograd sparked the February Revolution", "Fuel shortages closed factories", "Prices rose much faster than wages"],
     "own_against": ["The influence of Rasputin damaged the royal family", "Military defeats lowered morale", "The Duma politicians had lost faith in the Tsar"]},
    {"view": "transport problems were a key weakness in Russia's war effort",
     "pro": {"food": "+"},
     "ext": ["transport broke down"],
     "own_for": ["The railways were overloaded with military traffic", "Food rotted in the countryside while cities starved", "Coal could not reach factories"],
     "own_against": ["Poor leadership and corruption also weakened the war effort", "Heavy losses at the front caused discontent", "Inflation was caused by government finance"]}]),
 ]},
{"focus": "the February Revolution of 1917",
 "aspects": {
   "spont": {"+": "the revolution was spontaneous", "-": "revolutionaries led the protests"},
   "troops": {"+": "the army could no longer be relied on to defend the Tsar's government", "-": "the army remained loyal to the Tsar"},
   "tsar": {"+": "the Tsar had lost support", "-": "some still hoped the Tsar could save his dynasty"},
   "char": {"+": "Nicholas seemed strangely detached from the crisis", "-": "Nicholas fought hard to save his throne"}},
 "sources": [
  ("From the memoirs of a Petrograd factory worker, written in 1927.",
   "Nobody planned it. On Women's Day the women from the textile mills came out about the bread, and they "
   "called on us to join them. By the third day the whole city was on strike. When the soldiers of the "
   "Volynsky regiment came over to our side, we knew the Tsar was finished.",
   {"spont": ("+", "nobody planned it and it began with women protesting about bread"),
    "troops": ("+", "the soldiers of the Volynsky regiment came over to the workers' side"),
    "tsar": ("+", "the whole city was on strike and the workers knew the Tsar was finished")}),
  ("From a telegram sent to the Tsar by the President of the Duma, February 1917.",
   "The situation is serious. There is anarchy in the capital. The government is paralysed. Transport and "
   "food supplies are in complete disorder. Troops are firing on one another. A person trusted by the "
   "country must be given power to form a new government at once.",
   {"troops": ("+", "troops are firing on one another"),
    "tsar": ("+", "a person trusted by the country must form a new government")}),
  ("From a report by a Bolshevik organiser in Petrograd, March 1917.",
   "Our comrades in the factories led the strikes and carried the red flags. We called on the soldiers to "
   "join the people, and many listened. The Tsar had no friends left, not even among his generals.",
   {"spont": ("-", "the Bolshevik organiser says his comrades in the factories led the strikes"),
    "troops": ("+", "many soldiers listened and joined the people"),
    "tsar": ("+", "the Tsar had no friends left, even among the generals")}),
  ("From the diary of a Tsarist general at army headquarters, March 1917.",
   "His Majesty wished to send loyal troops to the capital, but the generals advised him that the army "
   "could not be relied upon. Some of us believed he could still save the dynasty. He signed the "
   "abdication calmly, as though he were handing over command of a squadron.",
   {"troops": ("+", "the army could not be relied upon"),
    "tsar": ("-", "some generals believed he could still save the dynasty"),
    "char": ("+", "he signed the abdication calmly, as though handing over command of a squadron")}),
 ],
 "extracts": [
  ("From a history of the Russian Revolution, published in 2017.",
   "The February Revolution was not planned by any party. It grew out of bread queues and strikes, and "
   "became a revolution only when the soldiers of the Petrograd garrison refused to fire on the crowds. "
   "Within a week the three-hundred-year-old Romanov dynasty had gone.",
   [{"view": "the February Revolution was not planned",
     "pro": {"spont": "+"},
     "ext": ["the revolution was not planned by any party", "it grew out of bread queues and strikes"],
     "own_for": ["Most Bolshevik leaders, including Lenin, were in exile", "The protests began on International Women's Day over bread", "Strikes spread rapidly from factory to factory"],
     "own_against": ["Activists in the factories helped to organise strikes", "The Putilov workers' strike began before Women's Day", "Duma leaders took control and formed a government"]},
    {"view": "the actions of the soldiers were the key reason for the fall of the Tsar",
     "pro": {"troops": "+"},
     "ext": ["it became a revolution only when the soldiers refused to fire"],
     "own_for": ["The Petrograd garrison mutinied on 27 February", "The generals told the Tsar they could not guarantee the army's loyalty", "Soldiers helped set up the Petrograd Soviet"],
     "own_against": ["Long-term discontent among workers and peasants was a cause", "The Tsar's absence at the front left weak ministers in charge in Petrograd", "The Tsar had lost the support of the Duma and nobility"]},
    {"view": "the collapse of the Romanov dynasty was very rapid",
     "pro": {"tsar": "+"},
     "ext": ["within a week the dynasty had gone"],
     "own_for": ["Protests began on 23 February and the Tsar abdicated on 2 March", "His brother Michael refused the throne", "No major group fought to save the monarchy"],
     "own_against": ["The regime had been weakening for years before 1917", "Discontent had built up since 1905", "The war had undermined the monarchy since 1914"]}]),
  ("From a study of Nicholas II, published in 2008.",
   "By the start of 1917 almost every group in Russia had lost faith in Nicholas. Workers and peasants "
   "were hungry, the Duma politicians were plotting and even members of the royal family begged him to "
   "change course. He refused. His stubbornness turned a crisis into a catastrophe.",
   [{"view": "by 1917 Nicholas II had lost the support of almost every group in Russia",
     "pro": {"tsar": "+"},
     "ext": ["almost every group had lost faith in Nicholas", "even members of the royal family begged him to change"],
     "own_for": ["The Duma's Progressive Bloc demanded a government of public confidence", "Nobles murdered Rasputin in December 1916", "The generals advised abdication in March 1917"],
     "own_against": ["Many peasant soldiers still respected the idea of the Tsar", "Some generals were willing to fight for him", "Opposition groups disagreed about what should replace him"]},
    {"view": "the Tsar's own character was the main reason for his downfall",
     "pro": {"char": "+"},
     "alt": {"troops": "+"},
     "ext": ["he refused to change course", "his stubbornness turned a crisis into a catastrophe"],
     "own_for": ["He refused to appoint ministers trusted by the Duma", "He ignored warnings from the Duma president", "He went to the front in 1915, leaving the Tsarina in charge"],
     "own_against": ["The war created problems no ruler could easily solve", "Food shortages were caused by the transport system", "The mutiny of the soldiers ended his rule"]},
    {"view": "the February Revolution was caused by a crisis that had been building up",
     "pro": {"tsar": "+"},
     "ext": ["workers and peasants were hungry", "the Duma politicians were plotting"],
     "own_for": ["Strikes had increased through 1916", "Police reports warned of revolution", "Inflation and shortages had grown since 1915"],
     "own_against": ["The revolution itself was sparked unexpectedly by bread queues", "Few people expected the Tsar to fall so quickly", "Revolutionary parties did not plan it"]}]),
 ]},
],
"provisional": [
{"focus": "the Provisional Government in 1917",
 "aspects": {
   "war": {"+": "the war was a serious problem for the government", "-": "the war still had support"},
   "weak": {"+": "the government was weak and lacked authority", "-": "the government had real authority"},
   "land": {"+": "the government delayed dealing with the land question", "-": "the government dealt with the land question"},
   "reform": {"+": "the government had introduced or promised political reforms", "-": "the government made no reforms"}},
 "sources": [
  ("From the diary of a member of the Provisional Government, June 1917.",
   "We have given Russia freedoms it never knew, and the Constituent Assembly will follow. Yet we cannot make peace without betraying our allies, and so the offensive must go ahead. Yet every day "
   "the Soviet issues orders of its own, and the soldiers obey them before they obey us. We govern, it "
   "seems, only with the Soviet's permission.",
   {"war": ("+", "the government cannot make peace without betraying its allies, so the offensive must go ahead"),
    "weak": ("+", "the soldiers obey the Soviet before the government"),
    "reform": ("+", "the government has given Russia new freedoms")}),
  ("From a letter written by a peasant in the Tambov region, August 1917.",
   "The government tells us to wait for the Constituent Assembly before we take the land. We have waited "
   "three hundred years. In our village we have already driven off the landlord's steward and divided his "
   "fields. My son writes from the front that the men there want only to come home.",
   {"land": ("+", "peasants are told to wait before taking the land"),
    "war": ("+", "the men at the front want to come home"),
    "weak": ("+", "the villagers have taken the land themselves"),
    "reform": ("+", "the government tells peasants to wait for the Constituent Assembly")}),
  ("From a speech by a supporter of the government in Moscow, May 1917.",
   "Free Russia has the freest government in the world. We have abolished the death penalty, freed the "
   "prisoners and given equal rights to all peoples. Soon the Constituent Assembly will decide our future. "
   "Our soldiers will defend this freedom against the German Kaiser.",
   {"war": ("-", "the soldiers will defend Russia's freedom against Germany"),
    "reform": ("+", "it has abolished the death penalty and freed prisoners")}),
  ("From the memoirs of a British diplomat in Petrograd, published in 1923.",
   "The new government's decrees on freedom of the press and religion were admirable on paper, and Kerensky spoke beautifully, but he could not act. The June offensive collapsed, the army melted away and "
   "deserters filled the trains. The government's orders meant nothing beyond the capital. By the autumn "
   "it was obvious that whoever was bold enough could seize power.",
   {"war": ("+", "the June offensive collapsed and the army melted away"),
    "weak": ("+", "the government's orders meant nothing beyond the capital"),
    "reform": ("+", "its decrees on freedom of the press and religion were admirable on paper")}),
 ],
 "extracts": [
  ("From a history of 1917, published in 2016.",
   "The decision to carry on fighting was the Provisional Government's greatest mistake. It cost the "
   "government the support of the soldiers, who deserted in their hundreds of thousands, and it made "
   "every other problem worse, from food supplies to land. The Bolsheviks, who promised peace, reaped the "
   "reward.",
   [{"view": "continuing the war was the Provisional Government's biggest mistake",
     "pro": {"war": "+"},
     "alt": {"weak": "+", "land": "+"},
     "ext": ["carrying on fighting was the greatest mistake", "soldiers deserted in their hundreds of thousands"],
     "own_for": ["The June Offensive of 1917 was a disaster", "Desertion increased, with soldiers going home to take land", "The Bolshevik slogan 'Peace, Bread and Land' became popular"],
     "own_against": ["Dual Power with the Petrograd Soviet limited the government's authority", "The delay over land reform angered the peasants", "The Kornilov Affair destroyed Kerensky's support among the army officers"]},
    {"view": "the Bolsheviks gained support because they promised peace",
     "pro": {"war": "+"},
     "alt": {"land": "+"},
     "ext": ["the Bolsheviks, who promised peace, reaped the reward"],
     "own_for": ["Lenin's April Theses demanded an end to the war", "Bolshevik membership grew to about 250,000 by October", "The Bolsheviks won majorities in the Petrograd and Moscow Soviets in September"],
     "own_against": ["The Kornilov Affair gave the Bolsheviks weapons and prestige", "Trotsky's organisation was important in October", "Promises of land and bread also attracted support"]},
    {"view": "the war made all the government's other problems worse",
     "pro": {"war": "+"},
     "ext": ["it made every other problem worse, from food supplies to land"],
     "own_for": ["Food shortages continued in the cities", "Soldiers left the front to seize land", "Inflation continued as the war was paid for by printing money"],
     "own_against": ["The land question was delayed by the government's own choice", "The government's weaknesses came from Dual Power", "Kerensky's mistakes in the Kornilov Affair were not caused by the war"]}]),
  ("From a study of Kerensky, published in 2011.",
   "The Provisional Government was weak from the start. It had not been elected, it had no reliable army "
   "and it shared power with the Petrograd Soviet. Kerensky's handling of the Kornilov Affair destroyed what "
   "little authority it had left, because he had to arm the Bolsheviks to save himself.",
   [{"view": "the Provisional Government was weak from the start",
     "pro": {"weak": "+"},
     "ext": ["it had not been elected", "it had no reliable army and shared power with the Soviet"],
     "own_for": ["Order Number One meant soldiers obeyed the Soviet", "It was formed from the old Duma, not elected", "It called itself 'provisional' and delayed decisions"],
     "own_against": ["It had wide support in March 1917", "It survived the July Days and the Bolsheviks were blamed", "It introduced important reforms such as civil rights"]},
    {"view": "the Kornilov Affair was the turning point for the Provisional Government",
     "pro": {},
     "alt": {"war": "+"},
     "ext": ["the Kornilov Affair destroyed what little authority it had left", "Kerensky had to arm the Bolsheviks"],
     "own_for": ["Red Guards were given weapons", "Bolshevik prisoners were released", "The officers turned against Kerensky"],
     "own_against": ["The failure of the June Offensive had already damaged the government", "Peasants were already taking land", "Lenin's leadership was important in October"]},
    {"view": "Dual Power was the main weakness of the Provisional Government",
     "pro": {"weak": "+"},
     "alt": {"war": "+", "land": "+"},
     "ext": ["it shared power with the Petrograd Soviet"],
     "own_for": ["The Soviet controlled the railways and the soldiers", "Order Number One undermined officers' authority", "The Soviet's Military Revolutionary Committee organised the October seizure of power"],
     "own_against": ["The decision to continue the war cost it support", "Delays over land reform and the Constituent Assembly made it unpopular", "Economic problems continued"]}]),
 ]},
{"focus": "the Bolshevik seizure of power in October 1917",
 "aspects": {
   "easy": {"+": "the seizure of power was easy and met little resistance", "-": "the seizure of power was violent and hard fought"},
   "lead": {"+": "the seizure of power was carefully planned", "-": "the seizure of power was not planned"},
   "lenin": {"+": "Lenin had great personal appeal", "-": "Lenin had little influence"},
   "trotsky": {"+": "Trotsky planned the seizure of power", "-": "Trotsky played little part"},
   "pop": {"+": "the Bolsheviks had popular support", "-": "the Bolsheviks had little popular support"}},
 "sources": [
  ("From the memoirs of a Red Guard who took part in the events, written in 1930.",
   "On the night of the 24th we moved quietly through the city and took the bridges and the telephone "
   "exchange. Hardly a shot was fired. Comrade Trotsky had planned everything at the Smolny. When we entered "
   "the Winter Palace, the ministers were sitting around a table waiting to be arrested.",
   {"easy": ("+", "hardly a shot was fired and the ministers were waiting to be arrested"),
    "lead": ("+", "everything had been planned in advance at the Smolny"),
    "trotsky": ("+", "it names Comrade Trotsky as the man who planned it")}),
  ("From a newspaper published by a rival socialist party, 26 October 1917.",
   "A small group of conspirators has seized power behind the backs of the people. The Bolsheviks have not "
   "waited for the Congress of Soviets or the Constituent Assembly. Their rule will not last and will bring "
   "civil war.",
   {"pop": ("-", "it says power was seized behind the backs of the people"),
    "lead": ("+", "it calls the Bolsheviks a small group of conspirators who did not wait for the Congress of Soviets")}),
  ("From the diary of an American journalist in Petrograd, October 1917.",
   "In the streets life went on as normal: trams ran and the theatres were open. Yet at the Congress of "
   "Soviets the hall roared its approval when Lenin appeared. A Bolshevik told me the rising had been planned "
   "for weeks by a handful of men at the Smolny. Workers and soldiers everywhere seemed to "
   "believe that the Bolsheviks would give them peace.",
   {"easy": ("+", "life went on as normal in the streets"),
    "pop": ("+", "workers and soldiers seemed to believe the Bolsheviks would give them peace"),
    "lenin": ("+", "the hall roared approval when Lenin appeared"),
    "lead": ("+", "a Bolshevik said the rising had been planned for weeks by a handful of men")}),
  ("From a letter written by an officer cadet defending the Winter Palace, October 1917.",
   "We were left with a handful of cadets and the women's battalion. The government had no other defenders. "
   "The cruiser Aurora fired a blank shot, and some of the Bolsheviks' shells hit the palace. When they "
   "came in there was confusion and looting. Few people in the square cheered them; most simply watched.",
   {"easy": ("+", "the government had only a handful of defenders"),
    "pop": ("-", "few people cheered the Bolsheviks; most simply watched")}),
 ],
 "extracts": [
  ("From a history of the Bolshevik party, published in 2005.",
   "The October Revolution was less a popular rising than a carefully planned coup. It was carried out by a "
   "few thousand Red Guards and sailors under the direction of Trotsky's Military Revolutionary Committee. "
   "Most of the people of Petrograd were hardly aware that anything had happened.",
   [{"view": "the October Revolution was a coup rather than a popular rising",
     "pro": {"pop": "-", "easy": "+", "lead": "+"},
     "ext": ["it was a carefully planned coup", "most people were hardly aware that anything had happened"],
     "own_for": ["Only a few thousand Red Guards, soldiers and sailors were involved", "The Bolsheviks acted before the Congress of Soviets met", "The Bolsheviks won only about a quarter of the votes in the Constituent Assembly elections"],
     "own_against": ["The Bolsheviks had won majorities in the Petrograd and Moscow Soviets", "The Congress of Soviets approved the new government", "Bolshevik membership had grown to around a quarter of a million"]},
    {"view": "Trotsky's role was vital to the success of the Bolshevik seizure of power",
     "pro": {"trotsky": "+"},
     "alt": {"lenin": "+"},
     "ext": ["the coup was carried out under the direction of Trotsky's Military Revolutionary Committee"],
     "own_for": ["Trotsky chaired the Petrograd Soviet and its Military Revolutionary Committee", "He planned the seizure of key points in the city", "He persuaded the garrison to support the Soviet"],
     "own_against": ["Lenin persuaded the Bolshevik Central Committee to act", "The weakness of the Provisional Government made the takeover easier", "The Kornilov Affair had already armed the Red Guards"]},
    {"view": "the Bolshevik seizure of power was achieved by a small number of people",
     "pro": {"easy": "+", "pop": "-", "lead": "+"},
     "ext": ["a few thousand Red Guards and sailors carried it out"],
     "own_for": ["The Winter Palace was defended only by cadets and a women's battalion", "Few people died in Petrograd", "Kerensky could not find troops to defend the government"],
     "own_against": ["The fighting in Moscow lasted about a week", "The Bolsheviks had wide support among Petrograd workers and soldiers", "Support from the Petrograd garrison was vital"]}]),
  ("From a study of Lenin, published in 2018.",
   "Without Lenin there would have been no October Revolution. It was he who insisted, against the doubts of "
   "his colleagues, that the moment had come to seize power. His slogans of peace, bread and land had won "
   "the Bolsheviks a mass following. When the Provisional Government collapsed, it was Lenin's party that was "
   "ready to take its place.",
   [{"view": "Lenin was the main reason for the Bolshevik seizure of power",
     "pro": {"lenin": "+"},
     "alt": {"trotsky": "+"},
     "ext": ["without Lenin there would have been no October Revolution", "he insisted the moment had come"],
     "own_for": ["Lenin's April Theses gave the party clear aims", "He returned from hiding to persuade the Central Committee to vote for a rising", "He wrote many articles urging the seizure of power"],
     "own_against": ["Trotsky organised the actual takeover", "Lenin was in hiding in Finland for much of the time after the July Days", "The Kornilov Affair increased Bolshevik support"]},
    {"view": "the Bolsheviks had won mass support by October 1917",
     "pro": {"pop": "+"},
     "ext": ["his slogans had won the Bolsheviks a mass following"],
     "own_for": ["Bolshevik membership rose from about 25,000 in February to around 250,000 by October", "The Bolsheviks won majorities in the Petrograd and Moscow Soviets", "The slogans 'Peace, Bread and Land' and 'All power to the Soviets' were popular"],
     "own_against": ["They won only about a quarter of the votes for the Constituent Assembly", "Many peasants supported the Socialist Revolutionaries", "Rival socialists condemned the seizure of power"]},
    {"view": "the Bolsheviks took power because the Provisional Government collapsed",
     "pro": {"easy": "+"},
     "alt": {"lead": "+", "trotsky": "+"},
     "ext": ["when the Provisional Government collapsed, Lenin's party was ready"],
     "own_for": ["The government had few troops to defend it", "Kerensky fled Petrograd", "The war and land problems had destroyed the government's support"],
     "own_against": ["The Bolsheviks actively planned and organised the takeover", "Bolshevik support in the Petrograd factories and garrison had been growing", "The Military Revolutionary Committee controlled the garrison"]}]),
 ]},
],
"civil-war": [
{"focus": "the Bolshevik consolidation of power in 1917–18",
 "aspects": {
   "force": {"+": "the Bolsheviks used force against opponents", "-": "the Bolsheviks ruled by consent"},
   "pop": {"+": "the Bolsheviks had won support", "-": "many Russians did not support the Bolsheviks"},
   "dem": {"+": "the Bolsheviks rejected democracy and free opposition", "-": "the Bolsheviks respected democracy"}},
 "sources": [
  ("From the memoirs of a Socialist Revolutionary deputy to the Constituent Assembly, published in 1921.",
   "We arrived at the Tauride Palace on 5 January to find it surrounded by sailors with rifles. The galleries "
   "were full of armed men who jeered at our speeches. When we tried to return the next day, the doors were "
   "locked. The people had voted for us, and Lenin simply sent us home.",
   {"dem": ("+", "the Assembly was surrounded by armed sailors and then locked out"),
    "pop": ("-", "the people had voted for the Socialist Revolutionaries, not the Bolsheviks"),
    "force": ("+", "sailors with rifles and armed men in the galleries")}),
  ("From a letter written by a peasant to a newspaper, December 1917.",
   "At last the land is ours! The new government has given us the landlord's estate without payment. We "
   "have divided it fairly by the number of mouths in each family. The Red Guards in town have shut the newspaper of the Socialist Revolutionaries, but what do we care for newspapers? Long live the Soviet power!",
   {"pop": ("+", "the peasant celebrates being given the land"),
    "dem": ("+", "the Red Guards have shut the SR newspaper")}),
  ("From a report by an official of the Cheka, 1918.",
   "In the past month we have arrested 400 counter-revolutionaries in this province, including priests, "
   "former officers and speculators. Forty have been shot. The bourgeoisie must learn that the "
   "dictatorship of the proletariat is not a joke.",
   {"force": ("+", "400 were arrested and forty shot"),
    "dem": ("+", "it talks of the dictatorship of the proletariat")}),
  ("From the diary of a Petrograd schoolteacher, March 1918.",
   "The newspapers that criticised the government have been shut. Bread is still scarce. Many who welcomed the "
   "Bolsheviks in October now curse them for signing the shameful peace with Germany, which has given away "
   "Ukraine. Yet the soldiers are glad to be home.",
   {"pop": ("-", "many now curse the Bolsheviks for the peace with Germany"),
    "dem": ("+", "critical newspapers have been shut")}),
 ],
 "extracts": [
  ("From a history of Soviet Russia, published in 2010.",
   "Lenin never intended to share power. He closed opposition newspapers within days of taking office, set "
   "up the Cheka in December 1917 and dispersed the Constituent Assembly after a single day. By the summer of "
   "1918 Russia was a one-party state ruled by terror.",
   [{"view": "Lenin never intended to share power after October 1917",
     "pro": {"dem": "+"},
     "ext": ["he closed opposition newspapers within days", "he dispersed the Constituent Assembly after one day"],
     "own_for": ["The Kadet party was banned in November 1917", "Sovnarkom was made up of Bolsheviks only at first", "Other socialist parties were later banned"],
     "own_against": ["Left Socialist Revolutionaries joined the government in December 1917", "Lenin allowed the Constituent Assembly elections to go ahead", "Power was formally held by the Congress of Soviets"]},
    {"view": "terror was the main way the Bolsheviks kept power in 1917–18",
     "pro": {"force": "+"},
     "alt": {"pop": "+"},
     "ext": ["he set up the Cheka in December 1917", "Russia was ruled by terror"],
     "own_for": ["The Red Terror followed the attempt on Lenin's life in August 1918", "The Tsar and his family were executed in July 1918", "The Cheka executed thousands of suspects"],
     "own_against": ["The Decree on Land won peasant support", "The Decree on Peace and Brest-Litovsk ended the war", "Workers' control of factories was popular in the cities"]},
    {"view": "the Bolsheviks had created a one-party state by 1918",
     "pro": {"dem": "+", "force": "+"},
     "ext": ["by the summer of 1918 Russia was a one-party state"],
     "own_for": ["The Left SRs left the government over Brest-Litovsk and were then suppressed", "Opposition newspapers were closed", "The Constituent Assembly was closed in January 1918"],
     "own_against": ["Mensheviks and SRs still sat in some soviets in 1918", "The civil war meant Bolshevik control was not complete", "Large areas of Russia were controlled by the Whites"]}]),
  ("From a study of the early Soviet state, published in 2014.",
   "Lenin's first decrees gave the people what they had been demanding all year. Peasants received land, "
   "soldiers received peace and workers received the eight-hour day. These measures were popular and help "
   "explain why so many Russians were willing, at first, to tolerate the new government.",
   [{"view": "the early Bolshevik decrees were popular",
     "pro": {"pop": "+"},
     "ext": ["the decrees gave the people what they had been demanding", "the measures were popular"],
     "own_for": ["The Decree on Land legalised the peasants' seizure of estates", "The Decree on Peace appealed to soldiers", "The eight-hour day and workers' control pleased factory workers"],
     "own_against": ["The Treaty of Brest-Litovsk was seen as humiliating", "The closure of the Constituent Assembly angered many", "Grain requisitioning soon turned peasants against the government"]},
    {"view": "the Bolsheviks kept power in 1917–18 mainly by winning support",
     "pro": {"pop": "+", "force": "-"},
     "alt": {"dem": "+"},
     "ext": ["many Russians were willing to tolerate the new government"],
     "own_for": ["The land decree won over many peasants", "Ending the war was welcomed by soldiers", "The Bolsheviks controlled the soviets in the main cities"],
     "own_against": ["The Cheka was used against opponents", "The Constituent Assembly was closed by force", "Opposition newspapers were banned"]},
    {"view": "the Bolsheviks' early decrees gave the people what they wanted",
     "pro": {"pop": "+"},
     "ext": ["peasants received land, soldiers peace and workers the eight-hour day"],
     "own_for": ["The Decree on Land of October 1917", "Russia left the war in March 1918", "The Decree on Workers' Control"],
     "own_against": ["Bread remained scarce in the cities", "The peace treaty lost huge areas of land", "Freedom of the press was ended"]}]),
 ]},
{"focus": "the Civil War of 1918–21",
 "aspects": {
   "white": {"+": "the Whites were divided", "-": "the Whites were strong and dangerous"},
   "red": {"+": "the Red Army was well organised", "-": "the Red Army was badly organised"},
   "geo": {"+": "geography and distance worked in the Reds' favour",
           "-": "geography did not hold the Whites back"},
   "peas": {"+": "ordinary people had reasons to oppose the Whites", "-": "ordinary people welcomed the Whites"},
   "foreign": {"+": "foreign powers were helping the Whites", "-": "the Whites had no foreign help"}},
 "sources": [
  ("From the memoirs of a White Army officer, published in Paris in 1928.",
   "We had brave men but no common aim. Some of our generals wanted the Tsar back; others wanted a republic. "
   "Kolchak in Siberia and Denikin in the south never managed to join their forces, even when British tanks and uniforms reached us. Our soldiers looted the "
   "villages, and the peasants came to hate us as much as the Reds.",
   {"white": ("+", "the Whites had no common aim: some generals wanted the Tsar back, others a republic"),
    "geo": ("+", "Kolchak in Siberia and Denikin in the south never managed to join their forces"),
    "peas": ("+", "White soldiers looted the villages and the peasants came to hate them"),
    "foreign": ("+", "British tanks and uniforms reached the Whites")}),
  ("From an order issued by Trotsky to the Red Army, 1918.",
   "Any unit that retreats without orders will have its commissar and commander shot. Deserters will be "
   "punished with the utmost severity. The Red Army will defend the revolution to the last drop of blood against the White Guards and their foreign paymasters.",
   {"red": ("+", "it shows strict discipline: commanders and commissars of units that retreat will be shot"),
    "foreign": ("+", "it calls the Whites' backers their foreign paymasters")}),
  ("From a letter written by a British officer serving with the Whites, 1919.",
   "Denikin's army is advancing fast and may reach Moscow before winter. The Reds are falling back in "
   "disorder, and the people in the towns we take greet us with relief. With more supplies from Britain we "
   "could finish the Bolsheviks this year.",
   {"white": ("-", "Denikin's army is advancing fast and may reach Moscow"),
    "red": ("-", "the Reds are falling back in disorder"),
    "peas": ("-", "the people in the towns the Whites take greet them with relief"),
    "foreign": ("+", "more supplies from Britain could finish the Bolsheviks")}),
  ("From the diary of a railway worker in central Russia, 1920.",
   "Trotsky's armoured train passed through again today, full of commissars and machine guns. The Reds hold "
   "all the railway lines from Moscow, and they move their men wherever they are needed. They take our grain "
   "and shoot anyone who hides it, but at least they are not the landlords, and not the English and French who are paying the Whites.",
   {"red": ("+", "the Reds move their men wherever they are needed, and Trotsky's armoured train keeps passing through"),
    "geo": ("+", "the Reds hold all the railway lines from Moscow"),
    "peas": ("+", "the railway worker prefers the Reds because at least they are not the landlords"),
    "foreign": ("+", "the English and French are paying the Whites")}),
 ],
 "extracts": [
  ("From a history of the Russian Civil War, published in 2007.",
   "The Whites lost the Civil War as much as the Reds won it. Their armies were scattered around the edges of "
   "Russia, thousands of kilometres apart, and their leaders distrusted one another. Many peasants feared that "
   "a White victory would mean the return of the landlords.",
   [{"view": "the Whites lost the Civil War mainly because of their own weaknesses",
     "pro": {"white": "+", "peas": "+"},
     "alt": {"red": "+"},
     "ext": ["their armies were scattered and their leaders distrusted each other", "peasants feared the return of the landlords"],
     "own_for": ["Kolchak, Denikin and Yudenich attacked at different times", "The Whites included monarchists and liberals with different aims", "Foreign support was limited and withdrawn by 1920"],
     "own_against": ["Trotsky's leadership of the Red Army was vital", "The Reds controlled the railways and industrial centres", "War Communism supplied the Red Army with food"]},
    {"view": "geography was a key reason for the White defeat",
     "pro": {"geo": "+"},
     "ext": ["White armies were scattered around the edges of Russia, thousands of kilometres apart"],
     "own_for": ["The Reds held Moscow and Petrograd with their factories and population", "The Reds could use the railways to move troops", "White forces could not coordinate attacks"],
     "own_against": ["War Communism kept the Red Army supplied with food and weapons", "Red propaganda and terror were important", "Trotsky imposed strict discipline on the Red Army"]},
    {"view": "peasant fears of the Whites helped the Reds to win",
     "pro": {"peas": "+"},
     "ext": ["many peasants feared that a White victory would bring back the landlords"],
     "own_for": ["The Reds had given land to the peasants in 1917", "White forces often looted villages", "Bolshevik propaganda warned of the return of the landlords"],
     "own_against": ["Many peasants resented Red requisitioning", "Peasant revolts such as the Green armies fought both sides", "Military factors such as the railways mattered more"]}]),
  ("From a biography of Trotsky, published in 2013.",
   "Trotsky built the Red Army from almost nothing. He brought back thousands of former Tsarist officers, "
   "watched by political commissars, and imposed ferocious discipline. From his armoured train he rushed to "
   "every danger point. More than any other individual, he won the Civil War for the Bolsheviks.",
   [{"view": "Trotsky was the main reason for the Bolshevik victory in the Civil War",
     "pro": {"red": "+"},
     "alt": {"white": "+", "geo": "+"},
     "ext": ["Trotsky built the Red Army from almost nothing", "more than anyone, he won the Civil War"],
     "own_for": ["He introduced conscription and the army grew to about 5 million", "He used around 50,000 former Tsarist officers", "His armoured train travelled to the fronts to raise morale"],
     "own_against": ["The divisions among the Whites were also important", "Control of central Russia and the railways helped the Reds", "Lenin's War Communism supplied the army"]},
    {"view": "the Red Army was well organised and disciplined",
     "pro": {"red": "+"},
     "ext": ["Trotsky imposed ferocious discipline", "former officers were watched by commissars"],
     "own_for": ["Deserters were shot", "Commissars ensured loyalty", "The army was centrally directed from Moscow"],
     "own_against": ["Desertion from the Red Army remained high", "It lost the war against Poland in 1920", "Many soldiers were poorly trained conscripts"]},
    {"view": "the use of former Tsarist officers strengthened the Red Army",
     "pro": {"red": "+"},
     "ext": ["he brought back thousands of former Tsarist officers"],
     "own_for": ["They provided military experience the Bolsheviks lacked", "Their families were sometimes held hostage to ensure loyalty", "They helped organise the army into effective units"],
     "own_against": ["Some officers deserted to the Whites", "Many Bolsheviks distrusted them", "Commissars were needed because their loyalty was doubtful"]}]),
 ]},
],
"nep": [
{"focus": "the effects of War Communism",
 "aspects": {
   "hunger": {"+": "War Communism caused hunger and hardship", "-": "War Communism fed the Red Army"},
   "anger": {"+": "War Communism caused anger and discontent", "-": "people accepted War Communism"},
   "need": {"+": "War Communism was needed to supply the war effort", "-": "War Communism was not necessary"},
   "taken": {"+": "grain was taken from the peasants", "-": "peasants gave grain willingly"},
   "kron": {"+": "the Kronstadt sailors were demanding political freedom",
            "-": "the Kronstadt sailors were loyal to Bolshevik policy"},
   "repress": {"+": "the Bolsheviks dealt harshly with their opponents", "-": "the Bolsheviks tolerated opposition"}},
 "sources": [
  ("From a letter written by a peasant in the Volga region to the government, 1920.",
   "The requisition squads have taken everything, even the seed for next year. They searched under the "
   "floorboards and in the stoves. We have nothing left to eat. If they come again, the men say they will "
   "meet them with pitchforks.",
   {"hunger": ("+", "the squads took everything, even next year's seed"),
    "anger": ("+", "the men will meet the squads with pitchforks"),
    "taken": ("+", "the squads searched under the floorboards and in the stoves")}),
  ("From a speech by a Bolshevik leader to party members, 1919.",
   "The Red Army must be fed, or the Whites will return and hang us all. Every pood of grain taken from the "
   "kulaks is a bullet against Kolchak and Denikin. These are hard measures, but the revolution is at war.",
   {"need": ("+", "the Red Army must be fed or the Whites will return"),
    "hunger": ("-", "the grain feeds the Red Army"),
    "taken": ("+", "grain is taken from the kulaks")}),
  ("From the demands of the sailors at Kronstadt, March 1921.",
   "We demand new elections to the soviets by secret ballot, freedom of speech for workers and peasants, "
   "the release of all socialist political prisoners, and an end to the armed squads that take the peasants' grain. The peasants must be free to work their "
   "land as they wish.",
   {"kron": ("+", "the Kronstadt sailors demand new elections to the soviets and free speech"),
    "anger": ("+", "the sailors demand that the peasants be free to work their land as they wish"),
    "repress": ("+", "the sailors demand the release of socialist political prisoners"),
    "taken": ("+", "armed squads take the peasants' grain")}),
  ("From the diary of a factory worker in Petrograd, 1920.",
   "Our ration is a quarter of a pound of bread a day, and half the time it does not arrive. Many of my "
   "comrades have gone back to their villages to find food, and those who remain grumble openly. The factory stands half empty. The commissar says it is all for the front, and we must endure until the Whites are beaten.",
   {"hunger": ("+", "the ration is tiny and often does not arrive"),
    "anger": ("+", "the workers who remain grumble openly"),
    "need": ("+", "the commissar says it is all for the front")}),
 ],
 "extracts": [
  ("From a history of the Soviet economy, published in 2009.",
   "War Communism helped the Bolsheviks to win the Civil War, but at a terrible cost. Requisitioning fed "
   "the Red Army, yet it destroyed the peasants' will to grow food. By 1921 the cities were empty, factories "
   "were idle and revolts had broken out across the countryside.",
   [{"view": "War Communism caused terrible damage to Russia",
     "pro": {"hunger": "+", "anger": "+", "kron": "+"},
     "ext": ["it destroyed the peasants' will to grow food", "by 1921 the cities were empty and factories idle"],
     "own_for": ["Grain production fell sharply by 1921", "Around 5 million died in the famine of 1921", "Industrial output fell to a fraction of its 1913 level"],
     "own_against": ["The Civil War itself caused much of the damage", "Drought contributed to the famine", "Foreign intervention and blockade cut Russia's trade"]},
    {"view": "War Communism was necessary to win the Civil War",
     "pro": {"need": "+"},
     "ext": ["War Communism helped the Bolsheviks to win the Civil War", "requisitioning fed the Red Army"],
     "own_for": ["The army needed food and weapons", "Nationalised factories produced for the war", "Strict discipline was applied to workers"],
     "own_against": ["Requisitioning caused peasant revolts such as Tambov", "Many Bolsheviks saw it as a way to bring in communism, not just to win the war", "It continued after the Whites were mostly defeated"]},
    {"view": "War Communism caused widespread revolt by 1921",
     "pro": {"anger": "+", "kron": "+"},
     "ext": ["revolts had broken out across the countryside"],
     "own_for": ["The Tambov rising involved tens of thousands of peasants", "The Kronstadt sailors rebelled in March 1921", "Workers went on strike in Petrograd in February 1921"],
     "own_against": ["The Bolsheviks crushed the revolts", "Many people were too hungry to rebel", "Some supported the Bolsheviks against the Whites"]}]),
  ("From a study of the Kronstadt Rising, published in 2015.",
   "The Kronstadt sailors had been called the pride of the revolution. When they rose against the Bolsheviks "
   "in 1921, demanding free soviets and an end to requisitioning, Lenin knew he had to change course. He "
   "crushed the rising with great brutality, but at the same party congress he announced the New Economic Policy.",
   [{"view": "the Kronstadt Rising forced Lenin to change his economic policy",
     "pro": {"kron": "+"},
     "alt": {"hunger": "+"},
     "ext": ["Lenin knew he had to change course", "at the same congress he announced the NEP"],
     "own_for": ["The NEP was announced at the Tenth Party Congress in March 1921", "Lenin called Kronstadt the flash that lit up reality", "Requisitioning was replaced with a tax in kind"],
     "own_against": ["The famine and economic collapse also forced a change", "Peasant revolts such as Tambov had begun earlier", "Lenin had already been considering reforms before Kronstadt"]},
    {"view": "the Bolsheviks used brutal methods to deal with opposition in 1921",
     "pro": {"repress": "+"},
     "ext": ["he crushed the rising with great brutality"],
     "own_for": ["Thousands of Kronstadt sailors were killed or executed", "The Tambov rising was crushed using poison gas", "Factions within the party were banned"],
     "own_against": ["Lenin also made concessions through the NEP", "Some rebels were pardoned", "The famine was met with foreign aid"]},
    {"view": "the Kronstadt sailors' demands showed how unpopular War Communism had become",
     "pro": {"kron": "+", "anger": "+"},
     "ext": ["the sailors demanded free soviets and an end to requisitioning"],
     "own_for": ["The sailors had supported the Bolsheviks in 1917", "Their demands echoed those of striking workers", "Peasant families of the sailors suffered from requisitioning"],
     "own_against": ["The sailors were a small group", "Many original sailors had been replaced by new recruits", "The Bolsheviks still had support in the army"]}]),
 ]},
{"focus": "the New Economic Policy",
 "aspects": {
   "recov": {"+": "the NEP led to economic recovery", "-": "the NEP did not improve the economy"},
   "retreat": {"+": "the NEP brought back private trade", "-": "the NEP did not bring back capitalism"},
   "temp": {"+": "the NEP was meant as a temporary retreat", "-": "the NEP was meant to be permanent"},
   "control": {"+": "the state kept control of the key parts of the economy", "-": "the state gave up control of the economy"},
   "unrest": {"+": "the NEP was criticised by communists", "-": "the NEP was accepted in the party"}},
 "sources": [
  ("From the diary of a Moscow schoolteacher, 1922.",
   "Shops have reopened on the Tverskaya, and for the first time in years you can buy butter and sugar, if "
   "you can afford them. The Nepmen strut about in fur coats. Our old Bolshevik neighbour says this is not "
   "what he fought for.",
   {"recov": ("+", "shops have reopened and food can be bought"),
    "retreat": ("+", "the private traders, the Nepmen, strut about in fur coats"),
    "unrest": ("+", "an old Bolshevik says it is not what he fought for")}),
  ("From a speech by Lenin to the party, 1921.",
   "We must make a step back in order to take two steps forward later. The peasant must be given a reason to "
   "grow more grain. The state will keep the large factories, the banks and foreign trade. This is not "
   "capitalism; it is a breathing space. Many comrades already call this a betrayal. They are wrong.",
   {"temp": ("+", "Lenin calls it a step back to take two steps forward later, a breathing space"),
    "control": ("+", "the state will keep the large factories, the banks and foreign trade"),
    "unrest": ("+", "Lenin says many comrades already call it a betrayal"),
    "retreat": ("-", "Lenin insists that 'this is not capitalism'")}),
  ("From a letter written by a young party member to a newspaper, 1923.",
   "We shed our blood in the Civil War to destroy the bourgeoisie, and now they are back, selling us bread at "
   "high prices. The kulaks grow rich while the workers' wages stay low. Is this what Lenin meant by communism?",
   {"retreat": ("+", "the bourgeoisie are back selling bread at high prices"),
    "unrest": ("+", "a young party member angrily questions the policy")}),
  ("From a report by a Soviet economic official, 1924.",
   "Grain production has almost returned to its pre-war level. Small industry and private trade, permitted again since 1921, are "
   "flourishing, although some comrades still complain that the Nepmen are a return to capitalism. "
   "However, heavy industry is recovering more slowly, and prices of manufactured goods are high compared "
   "with the prices peasants receive for grain.",
   {"recov": ("+", "grain production has almost returned to pre-war level"),
    "retreat": ("+", "small industry and private trade are permitted again and flourishing"),
    "unrest": ("+", "some comrades still complain about the Nepmen")}),
 ],
 "extracts": [
  ("From a history of the Soviet Union, published in 2011.",
   "The New Economic Policy saved the Soviet state. Within three years, grain output had recovered and the "
   "markets were full of goods. Yet many communists hated it. To them, the return of private trade and the "
   "rise of the Nepmen were a betrayal of everything they had fought for.",
   [{"view": "the NEP was a great economic success",
     "pro": {"recov": "+"},
     "ext": ["within three years grain output had recovered", "the markets were full of goods"],
     "own_for": ["Grain production rose from about 37 million tonnes in 1921 to over 50 million by 1924", "Small industries and shops recovered quickly", "The famine of 1921 was not repeated"],
     "own_against": ["Heavy industry recovered slowly", "The 'scissors crisis' of 1923 saw industrial prices rise far above farm prices", "Unemployment rose in the cities"]},
    {"view": "many communists saw the NEP as a betrayal",
     "pro": {"unrest": "+"},
     "ext": ["many communists hated it", "they saw private trade and the Nepmen as a betrayal"],
     "own_for": ["Left-wing Bolsheviks criticised the policy", "Lenin had to ban factions in 1921 to silence critics", "Some party members left the party in protest"],
     "own_against": ["Lenin persuaded the party that it was a temporary measure", "Bukharin strongly supported the NEP", "The state kept control of the commanding heights"]},
    {"view": "the NEP saved the Soviet state",
     "pro": {"recov": "+"},
     "ext": ["the New Economic Policy saved the Soviet state"],
     "own_for": ["It ended the peasant revolts", "It restored food supplies to the cities", "It gave the regime time to strengthen its control"],
     "own_against": ["The Bolsheviks also used terror and the Cheka to stay in power", "The victory in the Civil War had already secured the state", "Political repression continued alongside the NEP"]}]),
  ("From a study of Lenin's achievements, published in 2016.",
   "Lenin's NEP was not a return to capitalism. The state kept control of heavy industry, the banks and "
   "foreign trade, and the Communist Party kept total political control. Lenin was clear that the policy was "
   "a temporary retreat, designed to give the regime time to recover.",
   [{"view": "the NEP was not a return to capitalism",
     "pro": {"control": "+", "retreat": "-"},
     "ext": ["the state kept control of heavy industry, the banks and foreign trade"],
     "own_for": ["Lenin called these the commanding heights of the economy", "The party remained the only legal party", "Large industries stayed nationalised"],
     "own_against": ["Private trade and small businesses returned", "Peasants could sell their surplus for profit", "The Nepmen became wealthy"]},
    {"view": "Lenin saw the NEP only as a temporary retreat",
     "pro": {"temp": "+"},
     "ext": ["Lenin was clear that it was a temporary retreat"],
     "own_for": ["Lenin described it as a step back in order to take two steps forward", "It was introduced as an emergency response in 1921", "Stalin ended it in 1928"],
     "own_against": ["Lenin later suggested it might last for many years", "Bukharin saw it as the long-term road to socialism", "It became a central part of Soviet policy until Lenin's death"]},
    {"view": "the Communist Party kept total political control during the NEP",
     "pro": {"unrest": "-"},
     "ext": ["the Communist Party kept total political control"],
     "own_for": ["Factions were banned in 1921", "Mensheviks and SRs were put on trial in 1922", "The Cheka (later the GPU) continued to operate"],
     "own_against": ["There was open debate within the party", "Critics such as the Workers' Opposition continued to speak", "Local officials did not always follow Moscow's orders"]}]),
 ]},
],
}
