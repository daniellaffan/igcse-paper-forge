"""Original content for Paper 2 Section B breadth study: America: from new nation to divided union, 1783-1877.

DIFFERENCES[sub] = list of (subject phrase, time 1, time 2, [(difference, detail) x3])
CAUSES[sub]      = list of (event phrase, [(cause, detail) x3])
ISSUES[sub]      = list of {"stems": [...{f}...], "factors": [(name, [points x3]), ...]}
All written for this project.
"""

DIFFERENCES = {
"new-nation": [
("the government of the United States", "1783", "1789", [
 ("under the Articles of Confederation there was no president, but by 1789 there was an elected president", "George Washington became the first President in 1789"),
 ("in 1783 Congress could not raise taxes, but by 1789 the federal government could", "the Constitution gave Congress the power to levy taxes"),
 ("in 1783 each state had one vote in Congress, but by 1789 representation in the House depended on population", "the Connecticut Compromise created a two-chamber Congress")]),
("the power of the federal government", "1786", "1791", [
 ("in 1786 it could not deal with rebellion, but by 1791 it had the power to raise an army", "Shays' Rebellion had to be put down by a Massachusetts militia"),
 ("in 1786 it could not control trade between states, but by 1791 it could", "the Constitution gave Congress power over interstate commerce"),
 ("in 1786 there was no national court system, but by 1791 there was a Supreme Court", "the Judiciary Act of 1789 set up federal courts")]),
("the rights of American citizens", "1787", "1791", [
 ("in 1787 the Constitution had no list of rights, but by 1791 the Bill of Rights had been added", "the first ten amendments were ratified in December 1791"),
 ("in 1787 freedom of speech was not guaranteed nationally, but by 1791 it was", "the First Amendment protected speech, religion and the press"),
 ("in 1787 Anti-federalists feared federal tyranny, but by 1791 many of their concerns had been met", "the Tenth Amendment reserved powers to the states")]),
("political divisions in the USA", "1789", "1800", [
 ("in 1789 there were no organised political parties, but by 1800 there were two", "the Federalists and Democratic-Republicans competed in elections"),
 ("in 1789 Washington governed with broad support, but by 1800 there was bitter rivalry", "Hamilton and Jefferson clashed over the national bank"),
 ("in 1789 Federalists dominated government, but in 1800 power passed to their opponents", "Jefferson won the election of 1800")]),
("the size of the United States", "1783", "1803", [
 ("in 1783 the USA reached only to the Mississippi, but by 1803 it stretched far beyond it", "the Louisiana Purchase doubled the size of the country"),
 ("in 1783 New Orleans was not American, but by 1803 the USA controlled it", "control of the port allowed western farmers to export goods"),
 ("in 1783 there were thirteen states, but by 1803 there were seventeen", "Vermont, Kentucky, Tennessee and Ohio had joined the Union")]),
("the national debt and finances", "1783", "1795", [
 ("in 1783 the government could not pay its debts, but by 1795 it had a plan to do so", "Hamilton's financial plan took over state debts"),
 ("in 1783 there was no national bank, but by 1795 there was one", "the First Bank of the United States opened in 1791"),
 ("in 1783 the government relied on requests to the states for money, but by 1795 it collected taxes directly", "duties on imports and a tax on whiskey were introduced")]),
("the relationship between large and small states", "1786", "1788", [
 ("in 1786 every state had equal power, but by 1788 large states had more seats in the House", "seats in the House were based on population"),
 ("in 1786 there was no agreed way to count slaves, but by 1788 there was", "the three-fifths compromise counted enslaved people as three-fifths of a person"),
 ("in 1786 small states feared being dominated, but by 1788 their equal Senate vote protected them", "each state had two senators")]),
("the presidency", "1789", "1809", [
 ("in 1789 the President was a Federalist, but by 1809 the presidency was held by Democratic-Republicans", "Jefferson and Madison followed Washington and Adams"),
 ("in 1789 presidents governed in a formal style, but by 1809 Jefferson had made the office simpler", "Jefferson walked to his inauguration and reduced ceremony"),
 ("in 1789 the President had not used powers to buy land, but by 1809 Jefferson had done so", "Jefferson used loose interpretation to buy Louisiana")]),
("interpretation of the Constitution", "1789", "1803", [
 ("in 1789 strict and loose constructionism had not been tested, but by 1803 they had divided politics", "Jefferson opposed Hamilton's national bank as unconstitutional"),
 ("in 1789 the Supreme Court had little power, but by 1803 it could strike down laws", "the case of Marbury v. Madison established judicial review"),
 ("in 1789 Jefferson was a strict constructionist, but in 1803 he acted as a loose constructionist", "he bought Louisiana although the Constitution did not mention buying land")]),
("relations with Native Americans in the North-west", "1783", "1795", [
 ("in 1783 Native Americans controlled much of Ohio, but by 1795 they had ceded much of it", "the Treaty of Greenville gave most of Ohio to the USA"),
 ("in 1783 the USA had no army to fight in the west, but by 1795 it did", "General Wayne won the Battle of Fallen Timbers in 1794"),
 ("in 1783 settlers moved west with little protection, but by 1795 the area was opened for settlement", "the Northwest Ordinance of 1787 set rules for new territories")]),
("trade between the states", "1785", "1790", [
 ("in 1785 states charged taxes on each other's goods, but by 1790 this was not allowed", "the Constitution gave Congress control of interstate trade"),
 ("in 1785 states issued their own money, but by 1790 there was one national currency", "the Constitution gave Congress the power to coin money"),
 ("in 1785 foreign trade was disorganised, but by 1790 it was controlled nationally", "the federal government set tariffs on imports")]),
("support for slavery in the North", "1783", "1804", [
 ("in 1783 slavery was legal in most northern states, but by 1804 all northern states had acted to end it", "New Jersey passed a gradual emancipation law in 1804"),
 ("in 1783 slavery was legal in the North-west, but after 1787 it was banned there", "the Northwest Ordinance banned slavery north of the Ohio River"),
 ("in 1783 the slave trade was not limited, but by 1804 its end had been fixed in law", "the Constitution allowed Congress to ban the import of slaves from 1808")]),
],
"westward": [
("the size of the United States", "1800", "1850", [
 ("in 1800 the USA ended at the Mississippi, but by 1850 it reached the Pacific", "California joined the Union in 1850"),
 ("in 1800 Spain and France controlled the west, but by 1850 the USA did", "the Mexican Cession of 1848 gave the USA the south-west"),
 ("in 1800 there were sixteen states, but by 1850 there were thirty-one", "states such as Texas and California had joined")]),
("the treatment of Native Americans in the south-east", "1820", "1840", [
 ("in 1820 the Cherokee lived on their own lands in Georgia, but by 1840 they had been removed west", "the Trail of Tears in 1838–39"),
 ("in 1820 treaties recognised Native lands, but by 1840 the Indian Removal Act allowed their removal", "the Act was passed in 1830"),
 ("in 1820 the Supreme Court had not ruled on Cherokee rights, but by 1840 its ruling had been ignored", "Jackson ignored the ruling in Worcester v. Georgia (1832)")]),
("the balance between free and slave states", "1819", "1821", [
 ("in 1819 there were eleven free and eleven slave states, but by 1821 Missouri had joined as a slave state with Maine as a free state", "the Missouri Compromise of 1820"),
 ("in 1819 there was no line dividing slave and free territory, but by 1821 there was", "slavery was banned north of 36°30′ in the Louisiana Territory"),
 ("in 1819 the issue of slavery in new states was not settled, but by 1821 a compromise had been agreed", "Henry Clay helped negotiate the compromise")]),
("Texas", "1830", "1845", [
 ("in 1830 Texas was part of Mexico, but by 1845 it had joined the USA", "Texas was annexed in 1845"),
 ("in 1830 slavery was banned in Texas by Mexico, but by 1845 it was legal", "American settlers had brought enslaved people"),
 ("in 1830 Texas was ruled from Mexico City, but by 1845 it had been independent", "Texas won independence at San Jacinto in 1836")]),
("the population of California", "1847", "1852", [
 ("in 1847 California had a small population, but by 1852 it had over 200,000 people", "the Gold Rush brought migrants from across the world"),
 ("in 1847 California was part of Mexico, but by 1852 it was a US state", "it became a free state in 1850"),
 ("in 1847 San Francisco was a small village, but by 1852 it was a large city", "it grew rapidly as a port for gold seekers")]),
("the Oregon Country", "1818", "1846", [
 ("in 1818 Oregon was jointly occupied by Britain and the USA, but by 1846 it was divided", "the Oregon Treaty fixed the border at the 49th parallel"),
 ("in 1818 few Americans lived in Oregon, but by 1846 thousands had settled there", "migrants travelled the Oregon Trail in the 1840s"),
 ("in 1818 Oregon was seen as remote, but by 1846 it was a major political issue", "Polk campaigned with the slogan 'Fifty-four forty or fight'")]),
("attitudes to westward expansion", "1803", "1845", [
 ("in 1803 many Federalists opposed expansion, but by 1845 most Americans supported it", "O'Sullivan's idea of Manifest Destiny became popular"),
 ("in 1803 expansion was justified by trade, but by 1845 it was justified as God's plan", "Manifest Destiny claimed Americans had a duty to spread across the continent"),
 ("in 1803 expansion had little link to slavery, but by 1845 it was closely linked to it", "the annexation of Texas was opposed by many northerners")]),
("the border with Spanish territory", "1810", "1821", [
 ("in 1810 Florida belonged to Spain, but by 1821 it belonged to the USA", "the Transcontinental Treaty of 1819"),
 ("in 1810 the western border was unclear, but by 1821 it had been fixed", "the treaty set a border to the Pacific"),
 ("in 1810 Spain claimed land in the north-west, but by 1821 it had given up this claim", "Spain gave up claims to Oregon")]),
("the economy of the West", "1810", "1850", [
 ("in 1810 western farmers struggled to send goods east, but by 1850 transport was much better", "the Erie Canal opened in 1825"),
 ("in 1810 there were few railways, but by 1850 there were thousands of miles", "railways linked the Midwest to eastern cities"),
 ("in 1810 the west was mainly frontier land, but by 1850 it produced huge amounts of grain", "the Midwest became a major farming region")]),
("the land owned by the USA in the south-west", "1845", "1848", [
 ("in 1845 the south-west belonged to Mexico, but by 1848 it belonged to the USA", "the Treaty of Guadalupe Hidalgo"),
 ("in 1845 the Texas border was disputed, but by 1848 it was fixed at the Rio Grande", "Mexico accepted the Rio Grande border"),
 ("in 1845 the USA had not fought Mexico, but by 1848 it had won a war", "American troops captured Mexico City in 1847")]),
("the position of Native Americans on the Great Plains", "1830", "1851", [
 ("in 1830 the Plains were seen as Indian territory, but by 1851 settlers crossed them in large numbers", "migrants used the Oregon and California trails"),
 ("in 1830 there were few treaties on the Plains, but by 1851 the Fort Laramie Treaty had been signed", "it set out tribal territories"),
 ("in 1830 the Plains tribes had little contact with Americans, but by 1851 there was more conflict", "the buffalo herds were disturbed by migrants")]),
("the issue of slavery in new territories", "1821", "1848", [
 ("in 1821 the Missouri Compromise seemed to settle the issue, but by 1848 it was being challenged", "the Wilmot Proviso of 1846 tried to ban slavery in land taken from Mexico"),
 ("in 1821 there was little new territory to decide on, but by 1848 there was a vast area", "the Mexican Cession added California and New Mexico"),
 ("in 1821 the main parties avoided the issue, but by 1848 a Free Soil Party had been formed", "it campaigned against the spread of slavery")]),
],
"slavery": [
("the issue of slavery in the territories", "1850", "1854", [
 ("in 1850 the Missouri Compromise line still applied, but by 1854 it had been repealed", "the Kansas–Nebraska Act"),
 ("in 1850 Congress decided on slavery in some territories, but by 1854 settlers voted on it", "popular sovereignty was introduced in Kansas and Nebraska"),
 ("in 1850 there was a compromise that calmed tension, but by 1854 there was anger in the North", "northern opposition led to the Republican Party")]),
("political parties in the USA", "1850", "1860", [
 ("in 1850 the Whigs were a major party, but by 1860 they had collapsed", "the party split over the Kansas–Nebraska Act"),
 ("in 1850 there was no Republican Party, but by 1860 it won the presidency", "Lincoln was elected in 1860"),
 ("in 1850 the Democrats were united, but by 1860 they had split", "Northern and Southern Democrats chose different candidates")]),
("the situation in Kansas", "1854", "1858", [
 ("in 1854 Kansas was largely unsettled, but by 1858 it was the scene of violence", "the conflict known as Bleeding Kansas"),
 ("in 1854 there was one territorial government, but by 1858 there were rival governments", "pro-slavery and free-state governments"),
 ("in 1854 the Act was meant to settle the issue, but by 1858 the Lecompton Constitution had divided Congress", "Buchanan supported the pro-slavery constitution")]),
("the legal position of enslaved people in free states", "1849", "1857", [
 ("in 1849 northern states could protect escaped slaves, but by 1857 the Fugitive Slave Act forced their return", "the Act was part of the Compromise of 1850"),
 ("in 1849 enslaved people could claim freedom in free territory, but by 1857 the Supreme Court said they could not", "the Dred Scott decision"),
 ("in 1849 Congress could ban slavery in territories, but by 1857 the Court said it could not", "the Court ruled the Missouri Compromise unconstitutional")]),
("the economies of North and South", "1820", "1860", [
 ("in 1820 both regions were mainly agricultural, but by 1860 the North was much more industrial", "most of the nation's factories were in the North"),
 ("in 1820 cotton was important, but by 1860 it dominated the Southern economy", "cotton made up over half of US exports"),
 ("in 1820 the population was similar, but by 1860 the North's was much larger", "immigrants settled mainly in the North")]),
("Northern attitudes to slavery", "1830", "1860", [
 ("in 1830 abolitionists were a small minority, but by 1860 opposition to slavery's spread was widespread", "Uncle Tom's Cabin sold hundreds of thousands of copies"),
 ("in 1830 few northerners helped escaped slaves, but by 1860 many did", "the Underground Railroad"),
 ("in 1830 no major party opposed the expansion of slavery, but by 1860 the Republicans did", "the Republican platform of 1860")]),
("Southern attitudes to the Union", "1850", "1861", [
 ("in 1850 Southern states accepted the Compromise, but by 1861 many had seceded", "South Carolina seceded in December 1860"),
 ("in 1850 Southerners believed their interests were safe in the Union, but by 1861 they did not", "they feared Lincoln would end slavery"),
 ("in 1850 there was no Confederate government, but by 1861 there was", "Jefferson Davis became President of the Confederacy")]),
("Lincoln's political position", "1854", "1861", [
 ("in 1854 Lincoln was a little-known lawyer, but by 1861 he was President", "he won the election of 1860"),
 ("in 1854 he was a Whig, but by 1861 he was a Republican", "he joined the new party in 1856"),
 ("in 1854 he had no national fame, but by 1861 he was well known", "the Lincoln–Douglas debates of 1858")]),
("the position of California", "1848", "1850", [
 ("in 1848 California was a territory, but by 1850 it was a state", "it joined the Union in 1850"),
 ("in 1848 slavery in California had not been decided, but by 1850 it was a free state", "its entry upset the balance of free and slave states"),
 ("in 1848 California was a minor issue, but by 1850 it caused a national crisis", "it led to the Compromise of 1850")]),
("violence over slavery", "1850", "1859", [
 ("in 1850 the conflict was mainly political, but by 1859 there had been violence", "John Brown's raid on Harpers Ferry"),
 ("in 1850 Congress was a place of debate, but by 1856 a senator had been beaten there", "Charles Sumner was attacked by Preston Brooks"),
 ("in 1850 there was little fighting over slavery, but by 1856 there were killings in Kansas", "the Pottawatomie massacre")]),
("the relationship between the states and the federal government", "1850", "1861", [
 ("in 1850 the federal government was accepted across the country, but by 1861 Southern states rejected it", "seven states had seceded by February 1861"),
 ("in 1850 federal forts in the South were peaceful, but by 1861 one had been attacked", "Confederates fired on Fort Sumter in April 1861"),
 ("in 1850 there was one national government, but by 1861 there were two", "the Confederate States of America")]),
("the Supreme Court's role in the slavery issue", "1850", "1857", [
 ("in 1850 the Court had avoided ruling on slavery in territories, but by 1857 it had ruled", "the Dred Scott decision"),
 ("in 1850 Congress led on the issue, but by 1857 the Court had overruled Congress", "it declared the Missouri Compromise unconstitutional"),
 ("in 1850 the Court was respected in the North, but by 1857 it was attacked there", "Republicans condemned the decision")]),
],
"civil-war": [
("the aims of the Union", "1861", "1863", [
 ("in 1861 the war was to save the Union, but by 1863 it was also to end slavery", "the Emancipation Proclamation came into force in January 1863"),
 ("in 1861 Lincoln did not want to free slaves, but by 1863 he had freed them in Confederate areas", "he feared losing the border states in 1861"),
 ("in 1861 black men could not join the Union army, but by 1863 they could", "about 180,000 black soldiers served")]),
("the military situation", "1862", "1864", [
 ("in 1862 Lee won major victories, but by 1864 the Union was winning", "Lee won at Fredericksburg in 1862"),
 ("in 1862 the Mississippi was contested, but by 1864 the Union controlled it", "Vicksburg fell in July 1863"),
 ("in 1862 the Union lacked a successful commander, but by 1864 Grant was in charge", "Grant became general-in-chief in 1864")]),
("the Southern economy", "1861", "1865", [
 ("in 1861 the South could export cotton, but by 1865 the blockade had stopped most exports", "the Anaconda Plan"),
 ("in 1861 prices were stable, but by 1865 there was severe inflation", "prices rose by over 9,000 per cent"),
 ("in 1861 the South's farms were productive, but by 1865 many had been destroyed", "Sherman's March to the Sea")]),
("the Union's leadership", "1861", "1864", [
 ("in 1861 McClellan was a cautious commander, but by 1864 Grant fought aggressive campaigns", "Grant's Overland Campaign"),
 ("in 1861 Lincoln had little military experience, but by 1864 he had learned to direct the war", "he chose Grant and Sherman"),
 ("in 1861 Lincoln's re-election was uncertain, but by 1864 he won after Union victories", "Sherman captured Atlanta in September 1864")]),
("the position of enslaved people in the South", "1861", "1865", [
 ("in 1861 slavery was legal throughout the South, but by 1865 it had been abolished", "the Thirteenth Amendment"),
 ("in 1861 enslaved people had little chance to escape, but by 1865 many had fled to Union lines", "they were called contrabands"),
 ("in 1861 they were forced to work for the Confederacy, but by 1865 many fought for the Union", "black regiments such as the 54th Massachusetts")]),
("Confederate hopes of foreign support", "1861", "1863", [
 ("in 1861 the Confederacy hoped for British recognition, but by 1863 this was unlikely", "the Emancipation Proclamation made Britain less willing to support slavery"),
 ("in 1861 cotton was thought to be a strong weapon, but by 1863 it was not", "Britain found other sources of cotton"),
 ("in 1861 the Trent Affair nearly caused war with Britain, but by 1863 relations had calmed", "the Confederate envoys were released")]),
("the Union army", "1861", "1865", [
 ("in 1861 it was made up of volunteers, but by 1865 it included conscripts", "conscription was introduced in 1863"),
 ("in 1861 it was poorly trained, but by 1865 it was experienced", "it defeated Lee at Appomattox"),
 ("in 1861 it had no black soldiers, but by 1865 it had many", "about 10 per cent of Union soldiers were black")]),
("the strength of the Confederate army", "1862", "1865", [
 ("in 1862 it was winning battles, but by 1865 it was defeated", "Lee surrendered at Appomattox in April 1865"),
 ("in 1862 it had enough men, but by 1865 it was short of soldiers", "desertion was common"),
 ("in 1862 it could invade the North, but by 1865 it was defending its last cities", "Petersburg and Richmond fell in April 1865")]),
("Lincoln's view of slavery", "1858", "1863", [
 ("in 1858 he opposed its spread but not its existence, but by 1863 he was freeing slaves", "the Emancipation Proclamation"),
 ("in 1858 he did not think he could end slavery, but by 1863 he used war powers to do so", "he declared slaves in rebel states free"),
 ("in 1858 he talked about preserving the Union, but by 1863 he spoke of a new birth of freedom", "the Gettysburg Address")]),
("the city of Atlanta", "1863", "1865", [
 ("in 1863 it was a Confederate railway centre, but by 1865 it was in ruins", "Sherman captured it in 1864"),
 ("in 1863 it supplied the Confederate army, but by 1865 it could not", "its factories and rail yards were burned"),
 ("in 1863 its residents lived under the Confederacy, but by 1865 they were under Union control", "civilians were ordered to leave")]),
("the government of the Confederacy", "1861", "1865", [
 ("in 1861 Davis had wide support, but by 1865 he was criticised", "states such as Georgia opposed conscription"),
 ("in 1861 the Confederacy controlled eleven states, but by 1865 it controlled very little", "Union armies occupied most of the South"),
 ("in 1861 it had a capital at Richmond, but by 1865 Richmond had fallen", "Davis fled in April 1865")]),
("support for the war in the North", "1861", "1863", [
 ("in 1861 there was great enthusiasm, but by 1863 there was opposition", "the New York draft riots of 1863"),
 ("in 1861 few people opposed the war, but by 1863 the Copperheads wanted peace", "Peace Democrats criticised Lincoln"),
 ("in 1861 people expected a short war, but by 1863 they knew it would be long", "battles such as Antietam had huge casualties")]),
],
"reconstruction": [
("the legal position of African Americans", "1865", "1870", [
 ("in 1865 they were free but not citizens, but by 1870 they were citizens", "the Fourteenth Amendment of 1868"),
 ("in 1865 black men could not vote, but by 1870 they had the right to vote", "the Fifteenth Amendment"),
 ("in 1865 Black Codes limited their rights, but by 1870 these had been overturned", "the Civil Rights Act of 1866")]),
("government in the South", "1865", "1868", [
 ("in 1865 former Confederates controlled Southern governments, but by 1868 they did not", "the Reconstruction Acts of 1867"),
 ("in 1865 the South governed itself, but by 1868 it was under military rule", "the South was divided into five military districts"),
 ("in 1865 no black men held office, but by 1868 many did", "black politicians were elected to state legislatures")]),
("the power of President Johnson", "1865", "1868", [
 ("in 1865 Johnson controlled Reconstruction, but by 1868 Congress did", "Congress passed laws over his veto"),
 ("in 1865 he was popular, but by 1868 he had been impeached", "he survived by one vote in the Senate"),
 ("in 1865 he pardoned many Confederates, but by 1868 Congress had limited his powers", "the Tenure of Office Act")]),
("the lives of freed people", "1865", "1870", [
 ("in 1865 few freed people could read, but by 1870 many attended schools", "the Freedmen's Bureau set up about 1,000 schools"),
 ("in 1865 many had no work, but by 1870 many were sharecroppers", "sharecropping spread across the South"),
 ("in 1865 families had been separated by slavery, but by 1870 many were reunited", "freed people travelled to find relatives")]),
("the position of Native Americans on the Plains", "1865", "1877", [
 ("in 1865 many tribes lived freely on the Plains, but by 1877 most were on reservations", "the Peace Policy of 1869 moved tribes onto reservations"),
 ("in 1865 the buffalo herds were large, but by 1877 they were being destroyed", "hunters killed millions of buffalo"),
 ("in 1865 the Black Hills belonged to the Sioux, but by 1877 they had been taken", "gold was discovered there in 1874")]),
("violence against African Americans", "1865", "1877", [
 ("in 1865 there was no Ku Klux Klan, but by 1877 such groups had terrorised the South", "the Klan was founded in 1866"),
 ("in 1865 the federal government did little, but by 1871 it acted against the Klan", "the Enforcement Acts"),
 ("in 1865 violence was local, but by 1877 it was used to win elections", "white groups such as the Red Shirts intimidated black voters")]),
("the presence of federal troops in the South", "1867", "1877", [
 ("in 1867 troops enforced Reconstruction, but by 1877 they had been withdrawn", "the Compromise of 1877"),
 ("in 1867 the army protected black voters, but by 1877 it did not", "Democrats regained control of Southern states"),
 ("in 1867 Congress supported strong action, but by 1877 northerners had lost interest", "an economic depression began in 1873")]),
("the political power of African Americans", "1867", "1877", [
 ("in 1867 black men had just gained the vote, but by 1877 many were being stopped from using it", "intimidation and violence kept them from the polls"),
 ("in 1867 there were no black members of Congress, but by 1877 there had been several", "Hiram Revels became a senator in 1870"),
 ("in 1867 Republicans controlled Southern states, but by 1877 Democrats did", "the 'Redeemers' took back power")]),
("the Southern economy", "1865", "1877", [
 ("in 1865 the economy was based on slave labour, but by 1877 it relied on sharecropping", "freed people worked land for a share of the crop"),
 ("in 1865 much of the South was destroyed, but by 1877 railways had been rebuilt", "Reconstruction governments funded railways"),
 ("in 1865 cotton production had collapsed, but by 1877 it had recovered", "the South remained dependent on cotton")]),
("Congressional Reconstruction", "1866", "1876", [
 ("in 1866 Radical Republicans led Congress, but by 1876 their influence had declined", "leaders such as Thaddeus Stevens had died"),
 ("in 1866 Congress passed major civil rights laws, but by 1876 it passed few", "the Civil Rights Act of 1875 was weakly enforced"),
 ("in 1866 Republicans had large majorities, but by 1876 Democrats controlled the House", "the Democrats won the House in 1874")]),
("the US Army's relations with the Sioux", "1868", "1876", [
 ("in 1868 there was a peace treaty, but by 1876 there was war", "the Fort Laramie Treaty of 1868 and the Great Sioux War"),
 ("in 1868 the army withdrew from forts, but by 1876 it was attacking Sioux camps", "the army abandoned the Bozeman Trail forts in 1868"),
 ("in 1868 the Sioux kept the Black Hills, but by 1876 the army was protecting miners there", "Custer's expedition of 1874 found gold")]),
("the Freedmen's Bureau", "1865", "1872", [
 ("in 1865 it was newly created, but by 1872 it had been closed", "Congress ended it in 1872"),
 ("in 1865 it gave food to millions, but by 1872 its help had ended", "it provided rations to freed people and poor whites"),
 ("in 1865 it was opposed by Johnson, but by 1866 it had been renewed by Congress", "Congress passed it over his veto")]),
],
}

CAUSES = {
"new-nation": [
("Shays' Rebellion (1786–87)", [
 ("farmers in Massachusetts were in debt", "many were veterans who had not been paid for their war service"),
 ("the state raised taxes", "farmers who could not pay had their farms seized"),
 ("the courts were taking farmers' land", "rebels closed courts to stop foreclosures")]),
("the calling of the Constitutional Convention (1787)", [
 ("the Articles of Confederation were weak", "Congress could not raise taxes or regulate trade"),
 ("Shays' Rebellion showed the danger of disorder", "the national government could not help put it down"),
 ("states argued over trade", "the Annapolis Convention of 1786 called for a wider meeting")]),
("the Connecticut Compromise (1787)", [
 ("large and small states disagreed about representation", "the Virginia Plan favoured large states, the New Jersey Plan small ones"),
 ("the Convention risked breaking up", "small states threatened to leave"),
 ("a two-chamber Congress satisfied both sides", "the House was based on population and the Senate gave each state two seats")]),
("the three-fifths compromise (1787)", [
 ("Southern states wanted enslaved people counted for representation", "this would give them more seats in the House"),
 ("Northern states objected", "they argued enslaved people had no rights so should not be counted"),
 ("delegates wanted to keep the South in the Union", "the compromise counted three-fifths of enslaved people")]),
("disagreements between Federalists and Anti-federalists (1787–88)", [
 ("they disagreed about the power of central government", "Anti-federalists feared it would become tyrannical"),
 ("the Constitution had no Bill of Rights", "Anti-federalists demanded protection of individual rights"),
 ("they represented different interests", "Federalists were often merchants, Anti-federalists often farmers")]),
("the adding of the Bill of Rights (1791)", [
 ("Anti-federalists demanded it", "several states ratified the Constitution only on condition it was added"),
 ("people feared government power", "they remembered British abuses before independence"),
 ("Madison wanted to unite the country", "he drafted the amendments to win over critics")]),
("the rise of political parties in the 1790s", [
 ("Hamilton and Jefferson disagreed over the economy", "Hamilton wanted a national bank"),
 ("they disagreed about the Constitution", "Hamilton was a loose constructionist and Jefferson a strict one"),
 ("they disagreed over foreign policy", "Jefferson supported France and Hamilton favoured Britain")]),
("the creation of the First Bank of the United States (1791)", [
 ("the government had large debts", "Hamilton wanted to establish the country's credit"),
 ("the economy needed a stable currency", "the bank could issue notes"),
 ("Hamilton believed the Constitution allowed it", "he argued for implied powers")]),
("Jefferson's victory in the election of 1800", [
 ("the Federalists were unpopular", "the Alien and Sedition Acts were seen as attacks on liberty"),
 ("the Federalists were divided", "Hamilton attacked Adams"),
 ("Jefferson had strong support among farmers", "his party was well organised in the South")]),
("the Louisiana Purchase (1803)", [
 ("Americans wanted control of New Orleans", "western farmers needed the port"),
 ("Napoleon needed money", "France was about to go to war with Britain"),
 ("Jefferson wanted land for farmers", "he believed America should be a nation of farmers")]),
("Southern fears of a strong federal government in the 1780s", [
 ("they feared it might end slavery", "some northern delegates opposed slavery"),
 ("they feared taxes on exports", "the Southern economy depended on exports"),
 ("they feared being outvoted", "the North had more states")]),
("the Whiskey Rebellion (1794)", [
 ("a new tax was placed on whiskey", "it was part of Hamilton's financial plan"),
 ("western farmers relied on whiskey", "it was easier to transport than grain"),
 ("they resented federal power", "they felt eastern merchants controlled the government")]),
],
"westward": [
("the Missouri Compromise (1820)", [
 ("Missouri wanted to join as a slave state", "this would upset the balance in the Senate"),
 ("Northerners objected to the spread of slavery", "the Tallmadge Amendment tried to ban slavery in Missouri"),
 ("Maine wanted to become a state", "it could be admitted as a free state to keep the balance")]),
("the Indian Removal Act (1830)", [
 ("settlers wanted Native American land", "gold was found on Cherokee land in Georgia"),
 ("Andrew Jackson supported removal", "he had fought Native Americans as a general"),
 ("southern states wanted cotton land", "the land was good for growing cotton")]),
("the Trail of Tears (1838–39)", [
 ("the Cherokee refused to leave", "they argued their treaties protected them"),
 ("the government ignored the Supreme Court", "Jackson refused to enforce Worcester v. Georgia"),
 ("a small group signed the Treaty of New Echota", "the government used it to justify removal")]),
("the Texas Revolution (1835–36)", [
 ("American settlers in Texas disliked Mexican rule", "they resented laws against slavery"),
 ("Santa Anna took more power", "he ended the federal system in Mexico"),
 ("Texans wanted independence", "they declared independence in March 1836")]),
("the annexation of Texas (1845)", [
 ("Texans wanted to join the USA", "they feared Mexico would invade again"),
 ("Southerners wanted another slave state", "Texas was a large slave-holding area"),
 ("Polk supported expansion", "he won the 1844 election on an expansionist platform")]),
("the Mexican–American War (1846–48)", [
 ("there was a border dispute", "the USA claimed the Rio Grande, Mexico the Nueces River"),
 ("Polk wanted California", "Mexico refused to sell it"),
 ("Americans believed in Manifest Destiny", "they thought they had a right to the continent")]),
("the California Gold Rush (1848–49)", [
 ("gold was discovered at Sutter's Mill", "news spread quickly in 1848"),
 ("people wanted to get rich quickly", "about 300,000 people arrived"),
 ("transport routes were available", "migrants came by ship and overland")]),
("migration on the Oregon Trail in the 1840s", [
 ("there was cheap, fertile land in Oregon", "farmers sought new opportunities"),
 ("there was an economic depression in the East", "the Panic of 1837 caused hardship"),
 ("missionaries promoted Oregon", "they sent back positive reports")]),
("the Transcontinental Treaty (1819)", [
 ("the USA wanted Florida", "Seminole raids came from Spanish Florida"),
 ("Spain was weak", "it faced revolts in its colonies"),
 ("Jackson's invasion of Florida", "showed Spain could not defend it")]),
("opposition to westward expansion", [
 ("some feared the spread of slavery", "abolitionists opposed the annexation of Texas"),
 ("some feared war", "the Mexican War was criticised by Whigs such as Lincoln"),
 ("some believed the country was too large", "Federalists feared losing influence")]),
("the popularity of the idea of Manifest Destiny in the 1840s", [
 ("Americans believed their system was superior", "they thought they should spread democracy"),
 ("many believed it was God's will", "O'Sullivan wrote of a divine mission"),
 ("there was a need for land", "the population was growing rapidly")]),
("the Oregon Treaty (1846)", [
 ("Britain and the USA both claimed Oregon", "they had shared it since 1818"),
 ("the USA did not want war with Britain", "it was also preparing for war with Mexico"),
 ("American settlers had moved into the area", "they outnumbered British settlers")]),
],
"slavery": [
("the Compromise of 1850", [
 ("California wanted to join as a free state", "this would upset the balance of free and slave states"),
 ("Southerners threatened secession", "they feared losing power in the Senate"),
 ("Congressional leaders worked for a deal", "Henry Clay and Stephen Douglas proposed compromise measures")]),
("the Kansas–Nebraska Act (1854)", [
 ("Douglas wanted a transcontinental railway", "it needed organised territories in the west"),
 ("Douglas wanted Southern support", "he hoped to become President"),
 ("he believed in popular sovereignty", "settlers would decide on slavery")]),
("Bleeding Kansas (1854–59)", [
 ("both sides rushed settlers to Kansas", "the New England Emigrant Aid Company sent anti-slavery settlers"),
 ("elections were fraudulent", "Border Ruffians from Missouri voted illegally"),
 ("extremists used violence", "John Brown killed five pro-slavery settlers at Pottawatomie")]),
("the rise of the Republican Party in the 1850s", [
 ("northerners were angered by the Kansas–Nebraska Act", "it opened land to slavery"),
 ("the Whig party collapsed", "its members needed a new party"),
 ("people opposed the expansion of slavery", "the party's slogan was free soil, free labour, free men")]),
("the Dred Scott decision (1857)", [
 ("Dred Scott sued for his freedom", "he had lived in free territory"),
 ("the Supreme Court was dominated by Southerners", "Chief Justice Taney was a Southerner"),
 ("the Court wanted to settle the issue", "it ruled that Congress could not ban slavery in territories")]),
("growing economic differences between North and South", [
 ("the North industrialised", "factories and railways grew in the North"),
 ("the South relied on cotton", "cotton depended on enslaved labour"),
 ("they disagreed over tariffs", "the North wanted protective tariffs, which hurt Southern exports")]),
("John Brown's raid on Harpers Ferry (1859)", [
 ("Brown believed slavery must be ended by force", "he believed he was doing God's work"),
 ("he wanted to start a slave rebellion", "he planned to seize weapons from the armoury"),
 ("he had support from some abolitionists", "the 'Secret Six' funded him")]),
("Lincoln's victory in the 1860 election", [
 ("the Democrats were divided", "they put up two candidates"),
 ("the Republicans were strong in the North", "the North had more electoral votes"),
 ("Lincoln was a moderate candidate", "he opposed the spread of slavery but not slavery itself")]),
("the secession of South Carolina (1860)", [
 ("Lincoln was elected without any Southern votes", "he was not even on the ballot in many Southern states"),
 ("Southerners feared for slavery", "they believed the Republicans would end it"),
 ("they believed in states' rights", "they argued states could leave the Union")]),
("the attack on Fort Sumter (1861)", [
 ("the Confederacy wanted federal forts in the South", "Fort Sumter was in Charleston harbour"),
 ("Lincoln decided to resupply the fort", "he sent food but not weapons"),
 ("Confederate leaders wanted to show strength", "they hoped to bring more states into the Confederacy")]),
("northern anger over the Fugitive Slave Act (1850)", [
 ("it forced northerners to help capture escaped slaves", "they could be fined for helping fugitives"),
 ("free black people were kidnapped", "suspects had no right to a jury trial"),
 ("it made abolitionism more popular", "Uncle Tom's Cabin was written in response")]),
("growing support for abolition in the North in the 1850s", [
 ("Uncle Tom's Cabin was published in 1852", "it showed the cruelty of slavery"),
 ("the Fugitive Slave Act angered northerners", "it brought slavery into the North"),
 ("escaped slaves spoke out", "Frederick Douglass described the reality of slavery")]),
],
"civil-war": [
("the Union victory in the Civil War", [
 ("the North had greater resources", "it had more people, factories and railways"),
 ("the blockade weakened the South", "the Anaconda Plan cut off trade"),
 ("Union generals such as Grant and Sherman were effective", "Grant wore down Lee's army in 1864–65")]),
("the Emancipation Proclamation (1863)", [
 ("Lincoln wanted to weaken the Confederacy", "freeing slaves damaged the Southern economy"),
 ("he wanted to stop Britain supporting the South", "Britain had abolished slavery"),
 ("he wanted black men to join the army", "this would add to Union manpower")]),
("the Union blockade of the South", [
 ("the North wanted to strangle the Southern economy", "the South depended on cotton exports"),
 ("it would stop the South getting weapons", "the South had few factories"),
 ("the North had a stronger navy", "it could patrol thousands of miles of coast")]),
("the Union victory at Gettysburg (1863)", [
 ("the Union held strong defensive positions", "they held Cemetery Ridge"),
 ("Lee made mistakes", "Pickett's Charge failed with heavy losses"),
 ("the Union had more men", "Meade had around 90,000 troops")]),
("the fall of Vicksburg (1863)", [
 ("Grant besieged the city", "he cut off supplies for six weeks"),
 ("the defenders were starving", "they ran out of food"),
 ("the Union controlled the Mississippi", "gunboats helped Grant's army")]),
("Sherman's March to the Sea (1864)", [
 ("he wanted to destroy the South's ability to fight", "railways, farms and factories were burned"),
 ("he wanted to break Southern morale", "it showed the Confederacy could not protect its people"),
 ("he wanted to split the Confederacy", "he marched from Atlanta to Savannah")]),
("problems in the Southern economy during the war", [
 ("the blockade stopped trade", "cotton exports collapsed"),
 ("the government printed money", "inflation reached over 9,000 per cent"),
 ("fighting destroyed farms and railways", "food shortages led to bread riots in Richmond in 1863")]),
("Lee's early successes in the war", [
 ("he was a skilled commander", "he won at the Second Battle of Bull Run"),
 ("the Union generals were cautious", "McClellan failed to attack decisively"),
 ("Confederate soldiers were defending their homes", "morale was high")]),
("the Gettysburg Address (1863)", [
 ("Lincoln wanted to honour the dead", "it was given at the dedication of a cemetery"),
 ("he wanted to explain the war's purpose", "he spoke of a new birth of freedom"),
 ("he wanted to strengthen support for the war", "northern morale needed a boost")]),
("the Confederate defeat", [
 ("the South lacked resources", "it had fewer factories and railways"),
 ("there were divisions in the Confederacy", "states opposed Davis's policies"),
 ("Southern armies lost key battles", "Gettysburg and Vicksburg in 1863")]),
("opposition to the war in the North", [
 ("conscription was unpopular", "the rich could pay to avoid service"),
 ("casualties were high", "Antietam was the bloodiest day of the war"),
 ("some opposed fighting to end slavery", "the Copperheads wanted peace")]),
("Lincoln's re-election in 1864", [
 ("the Union won important victories", "Sherman captured Atlanta"),
 ("the Democrats were divided", "their candidate McClellan disagreed with their peace platform"),
 ("soldiers supported Lincoln", "most soldiers voted for him")]),
],
"reconstruction": [
("the passing of the Reconstruction Acts (1867)", [
 ("Southern states passed Black Codes", "these limited the rights of freed people"),
 ("there was violence against freed people", "riots in Memphis and New Orleans in 1866"),
 ("Radical Republicans controlled Congress", "they won large majorities in 1866")]),
("the impeachment of Andrew Johnson (1868)", [
 ("Johnson opposed Congressional Reconstruction", "he vetoed many laws"),
 ("he dismissed Stanton", "this broke the Tenure of Office Act"),
 ("Radical Republicans wanted to remove him", "they disliked his lenient policy towards the South")]),
("the creation of the Freedmen's Bureau (1865)", [
 ("freed people needed help", "many had no land or work"),
 ("there was a need for education", "most freed people could not read"),
 ("the South was devastated", "poor whites also needed food")]),
("the introduction of Black Codes (1865–66)", [
 ("Southern whites wanted to control black labour", "they needed workers for plantations"),
 ("they feared freed people", "they wanted to keep white supremacy"),
 ("Johnson's lenient policy allowed it", "former Confederates returned to power")]),
("the Fourteenth Amendment (1868)", [
 ("Congress wanted to protect the Civil Rights Act", "it feared courts would strike it down"),
 ("Black Codes denied rights", "the amendment guaranteed equal protection"),
 ("Republicans wanted to punish former Confederates", "it banned them from office")]),
("the rise of the Ku Klux Klan", [
 ("white Southerners resented Reconstruction", "they disliked Republican governments"),
 ("they wanted to stop black people voting", "black men gained the vote in 1867"),
 ("they wanted to restore white supremacy", "they used violence and terror")]),
("the end of Reconstruction (1877)", [
 ("northerners lost interest", "the economic depression of 1873 diverted attention"),
 ("the disputed election of 1876", "the Compromise of 1877 removed federal troops"),
 ("violence in the South", "white groups intimidated Republican voters")]),
("the Peace Policy (1869)", [
 ("Grant wanted to end wars with Native Americans", "earlier wars were costly"),
 ("reformers wanted to 'civilise' Native Americans", "religious groups ran reservations"),
 ("the government wanted land for railways and settlers", "reservations freed land")]),
("the Battle of the Little Bighorn (1876)", [
 ("gold was found in the Black Hills", "miners entered Sioux land"),
 ("the government ordered the Sioux to reservations", "those who refused were treated as hostile"),
 ("Custer attacked a large camp", "he divided his forces and was outnumbered")]),
("the spread of sharecropping in the South", [
 ("freed people had no land", "they were not given the promised 40 acres"),
 ("planters had land but no money to pay wages", "the war had destroyed Southern wealth"),
 ("freed people wanted independence from gang labour", "sharecropping let families work their own plots")]),
("the Fifteenth Amendment (1870)", [
 ("Republicans wanted black votes", "they needed support in the South"),
 ("black soldiers had fought for the Union", "many believed they deserved the vote"),
 ("some states were still denying the vote", "Congress wanted national protection")]),
("conflict between Johnson and Congress (1865–68)", [
 ("they disagreed on how to treat the South", "Johnson was lenient and the Radicals wanted change"),
 ("Johnson vetoed civil rights laws", "he vetoed the Civil Rights Act of 1866"),
 ("Johnson opposed the Fourteenth Amendment", "he campaigned against Republicans in 1866")]),
],
}

ISSUES = {
"new-nation": [
{"stems": ["How far was {f} the main reason for disagreement over how the USA should be governed in the years 1783–1803?",
           "How significant was {f} in shaping the government of the new nation in the years 1783–1803?"],
 "factors": [
  ("the weakness of the Articles of Confederation", [
   "Congress could not raise taxes or regulate trade", "Shays' Rebellion exposed the weakness", "It led to the Constitutional Convention in 1787"]),
  ("the division between large and small states", [
   "The Virginia and New Jersey Plans disagreed on representation", "The Connecticut Compromise created a two-chamber Congress", "Small states gained equal votes in the Senate"]),
  ("disagreement over slavery", [
   "The three-fifths compromise was needed to satisfy the South", "The slave trade was protected until 1808", "Slavery was banned in the North-west by the 1787 Ordinance"]),
  ("the conflict between Federalists and Anti-federalists", [
   "Anti-federalists feared a strong central government", "The Federalist Papers argued for ratification", "The Bill of Rights was added in 1791"]),
  ("the debate between strict and loose constructionists", [
   "Hamilton used loose construction to justify the national bank", "Jefferson opposed the bank as unconstitutional", "Jefferson later used loose construction to buy Louisiana"]),
  ("the presidency of Jefferson", [
   "He reduced the size of government and the army", "He bought Louisiana in 1803", "His election in 1800 showed power could pass peacefully"]),
 ]},
{"stems": ["How significant was {f} in the development of the new nation in the years 1783–1820?"],
 "factors": [
  ("the Constitution of 1787", [
   "It created a stronger federal government", "It set up a President, Congress and Supreme Court", "It allowed new states to join on equal terms"]),
  ("Hamilton's financial policies", [
   "The federal government took over state debts", "The national bank stabilised the currency", "They caused the rise of political parties"]),
  ("the Bill of Rights", [
   "It protected freedom of speech and religion", "It reassured Anti-federalists", "It limited federal power"]),
  ("the Louisiana Purchase", [
   "It doubled the size of the USA", "It gave control of New Orleans and the Mississippi", "It opened the west to settlement"]),
  ("the Missouri Compromise", [
   "It kept the balance between free and slave states", "It drew a line at 36°30′", "It delayed conflict over slavery"]),
  ("Shays' Rebellion", [
   "It showed the weakness of the Articles", "It frightened leaders into calling the Convention", "It showed the danger of debt and taxation"]),
 ]},
],
"westward": [
{"stems": ["How significant was {f} in the expansion of the United States in the years 1800–50?",
           "How far was {f} the main reason for westward expansion in the years 1803–53?"],
 "factors": [
  ("the Louisiana Purchase", [
   "It doubled the size of the country in 1803", "It gave the USA control of the Mississippi", "It began the move beyond the Mississippi"]),
  ("Manifest Destiny", [
   "Americans believed they had a God-given right to the continent", "It justified the annexation of Texas", "It encouraged the war with Mexico"]),
  ("the Mexican–American War", [
   "It added California and the south-west", "The Treaty of Guadalupe Hidalgo transferred land", "It created new disputes over slavery"]),
  ("the California Gold Rush", [
   "It brought around 300,000 migrants", "California became a state in 1850", "It encouraged the development of transport routes"]),
  ("government policy towards Native Americans", [
   "The Indian Removal Act of 1830", "The Trail of Tears cleared land in the south-east", "Treaties opened Plains land for travel"]),
  ("economic factors", [
   "Farmers needed fresh land", "The Panic of 1837 encouraged migration", "Canals and railways connected the west to markets"]),
  ("the annexation of Texas", [
   "Texas joined in 1845", "It added a large slave state", "It led to war with Mexico"]),
 ]},
{"stems": ["How far was {f} the main consequence of westward expansion in the years 1803–54?"],
 "factors": [
  ("conflict over slavery", [
   "The Missouri Compromise of 1820", "The Wilmot Proviso of 1846", "The Compromise of 1850 and the Kansas–Nebraska Act"]),
  ("the removal of Native Americans", [
   "The Trail of Tears", "The Indian Removal Act", "The Fort Laramie Treaty of 1851"]),
  ("economic growth", [
   "New farmland in the Midwest", "Gold from California", "Growth of railways and trade"]),
  ("conflict with other countries", [
   "War with Mexico in 1846–48", "Tension with Britain over Oregon", "Disputes with Spain over Florida"]),
  ("growing national pride", [
   "Manifest Destiny", "The USA became a continental nation", "Pride in military victories over Mexico"]),
  ("the admission of new states", [
   "Missouri and Maine in 1820", "Texas in 1845", "California in 1850"]),
 ]},
],
"slavery": [
{"stems": ["How far was {f} the main reason for growing tension between North and South in the years 1820–61?",
           "How significant was {f} in the outbreak of civil war in 1861?"],
 "factors": [
  ("the issue of slavery in the territories", [
   "The Missouri Compromise of 1820", "The Kansas–Nebraska Act of 1854", "The Dred Scott decision of 1857"]),
  ("economic differences", [
   "The North industrialised while the South relied on cotton", "Disputes over tariffs", "The South feared Northern economic power"]),
  ("the growth of abolitionism", [
   "Uncle Tom's Cabin was published in 1852", "The Underground Railroad", "John Brown's raid in 1859"]),
  ("the election of Lincoln", [
   "Lincoln won in 1860 without Southern votes", "Southerners believed he would end slavery", "South Carolina seceded in December 1860"]),
  ("the idea of states' rights", [
   "Southerners argued states could reject federal laws", "The Nullification Crisis of 1832", "Seceding states claimed the right to leave"]),
  ("the failure of compromise", [
   "The Compromise of 1850 broke down", "Popular sovereignty led to violence in Kansas", "The Crittenden Compromise failed in 1861"]),
 ]},
{"stems": ["How significant was {f} in increasing divisions over slavery in the years 1850–61?"],
 "factors": [
  ("the Fugitive Slave Act", [
   "It forced northerners to help capture escaped slaves", "It led to protests and rescues", "It turned many northerners against slavery"]),
  ("Bleeding Kansas", [
   "Violence between pro- and anti-slavery settlers", "Rival governments in Kansas", "It led to the attack on Sumner in the Senate"]),
  ("the Dred Scott decision", [
   "It ruled that enslaved people were property", "It said Congress could not ban slavery in territories", "It angered the North"]),
  ("John Brown's raid", [
   "Brown attacked Harpers Ferry in 1859", "Southerners believed northerners supported slave revolts", "Brown became a martyr in the North"]),
  ("the collapse of the Whig Party", [
   "The party split over slavery", "It removed a national party linking North and South", "It led to the rise of the Republicans"]),
  ("the rise of the Republican Party", [
   "It was formed in 1854", "It was a purely northern party", "It won the presidency in 1860"]),
 ]},
],
"civil-war": [
{"stems": ["How far was {f} the main reason for the Union victory in the Civil War?",
           "How significant was {f} in the defeat of the Confederacy in the years 1861–65?"],
 "factors": [
  ("the North's economic strength", [
   "The North had most of the factories", "It had more railways", "It had a larger population"]),
  ("the Union blockade", [
   "It cut off Southern trade", "It caused shortages in the South", "It was part of the Anaconda Plan"]),
  ("the leadership of Lincoln", [
   "He kept the border states in the Union", "He chose Grant and Sherman", "The Emancipation Proclamation"]),
  ("the military leadership of Grant and Sherman", [
   "Grant captured Vicksburg", "Grant wore down Lee in 1864–65", "Sherman's March to the Sea"]),
  ("the weaknesses of the Confederacy", [
   "States resisted Davis's government", "Inflation and shortages", "Lack of foreign recognition"]),
  ("the Emancipation Proclamation", [
   "It weakened the Southern economy", "It stopped British recognition of the Confederacy", "It allowed black soldiers to join the Union army"]),
 ]},
{"stems": ["How significant was {f} as a turning point in the Civil War in the years 1861–65?"],
 "factors": [
  ("the Battle of Gettysburg", [
   "It ended Lee's invasion of the North", "Lee lost about a third of his army", "Lincoln's Gettysburg Address"]),
  ("the fall of Vicksburg", [
   "It gave the Union control of the Mississippi", "It split the Confederacy", "It made Grant famous"]),
  ("the Emancipation Proclamation", [
   "It changed the aims of the war", "It encouraged slaves to escape", "It prevented British intervention"]),
  ("Sherman's March to the Sea", [
   "It destroyed Southern resources", "It damaged Southern morale", "It helped Lincoln win in 1864"]),
  ("the appointment of Grant as general-in-chief", [
   "He coordinated Union armies", "He pressed Lee continuously", "Lee surrendered to him at Appomattox"]),
  ("the Battle of Antietam", [
   "It stopped Lee's first invasion", "It allowed Lincoln to announce emancipation", "It was the bloodiest single day"]),
 ]},
],
"reconstruction": [
{"stems": ["How far was {f} the main reason why Reconstruction did not bring equality for African Americans in the years 1865–77?",
           "How significant was {f} in the failure of Reconstruction in the years 1865–77?"],
 "factors": [
  ("the policies of Andrew Johnson", [
   "He pardoned many former Confederates", "He vetoed the Civil Rights Act and Freedmen's Bureau Bill", "He allowed Black Codes"]),
  ("violence by white Southerners", [
   "The Ku Klux Klan terrorised black people", "Riots in Memphis and New Orleans", "Intimidation of voters"]),
  ("the lack of land for freed people", [
   "They were not given 40 acres", "Sharecropping kept them poor", "Planters kept their land"]),
  ("Northern loss of interest", [
   "The depression of 1873", "Radical leaders died", "The Compromise of 1877"]),
  ("the Black Codes", [
   "They restricted where freed people could work and live", "They punished vagrancy", "They were later overturned"]),
  ("the withdrawal of federal troops", [
   "Troops left after 1877", "Southern Democrats regained power", "Black voters lost protection"]),
 ]},
{"stems": ["How significant was {f} in changing the lives of African Americans in the years 1863–77?"],
 "factors": [
  ("the Thirteenth Amendment", [
   "It abolished slavery in 1865", "It freed about 4 million people", "It was the basis for further rights"]),
  ("the Freedmen's Bureau", [
   "It set up schools", "It provided food and medical care", "It helped with labour contracts"]),
  ("the Fourteenth and Fifteenth Amendments", [
   "They made African Americans citizens", "They gave black men the vote", "They promised equal protection"]),
  ("the Reconstruction Acts", [
   "They placed the South under military rule", "They required new state constitutions", "They allowed black men to vote and hold office"]),
  ("the Emancipation Proclamation", [
   "It freed enslaved people in Confederate areas", "It allowed black men to join the army", "It made emancipation a war aim"]),
  ("sharecropping", [
   "It gave families some independence", "It kept many in debt", "It tied them to the land"]),
 ]},
],
}
