"""Public-domain unseen poems for Section A.

Every poet here died well before 1955 and every poem was published before 1929,
so the texts are in the public domain in the UK and the US. Indicative content
is written for this project. `gloss` lists the footnotes printed under the poem
(the real paper glosses unusual words with an asterisk).
"""

PD_POEMS = [
dict(id="darkling-thrush", title="The Darkling Thrush", author="Thomas Hardy", date="1900",
     life="1840-1928",
     text="""I leant upon a coppice* gate
When Frost was spectre-grey,
And Winter's dregs made desolate
The weakening eye of day.
The tangled bine-stems* scored the sky
Like strings of broken lyres,
And all mankind that haunted nigh
Had sought their household fires.

The land's sharp features seemed to be
The Century's corpse outleant,
His crypt the cloudy canopy,
The wind his death-lament.
The ancient pulse of germ and birth
Was shrunken hard and dry,
And every spirit upon earth
Seemed fervourless as I.

At once a voice arose among
The bleak twigs overhead
In a full-hearted evensong
Of joy illimited;
An aged thrush, frail, gaunt, and small,
In blast-beruffled plume,
Had chosen thus to fling his soul
Upon the growing gloom.

So little cause for carolings
Of such ecstatic sound
Was written on terrestrial things
Afar or nigh around,
That I could think there trembled through
His happy good-night air
Some blessed Hope, whereof he knew
And I was unaware.""",
     gloss=["coppice: a small wood of trees that are regularly cut back", "bine-stems: the stems of climbing plants"],
     focuses=[
      ("nature", "a bleak winter landscape", "7-9", "the landscape is presented as dead or dying, and the thrush is the single sign of life within it"),
      ("feelings", "hope", "7-9", "the speaker cannot share the thrush's joy but is moved to wonder whether it knows of 'Some blessed Hope' hidden from him"),
      ("memory", "the end of an era", "7-9", "written at the very end of the nineteenth century, the poem presents the landscape as 'The Century's corpse', so the death of the year and the century are linked"),
     ],
     desc=["The opening establishes a cold, grey scene: 'spectre-grey' frost and the 'weakening eye of day'.",
           "The thrush is described in detail as 'aged', 'frail, gaunt, and small', which makes its powerful song all the more surprising.",
           "People are absent: 'all mankind' has retreated indoors, leaving the speaker alone in the landscape."],
     lang=["Imagery of death (corpse, crypt, death-lament) turns the winter landscape into a funeral scene.",
           "The simile 'Like strings of broken lyres' links the tangled stems to broken musical instruments, suggesting that music and joy have gone from the world.",
           "Religious and musical vocabulary ('evensong', 'carolings', 'blessed Hope') introduces the possibility of faith or meaning.",
           "The contrast between 'growing gloom' and 'joy illimited' sets the bird's song against the darkness."],
     form=["Four eight-line stanzas with a regular alternating rhyme scheme and rhythm give the poem a hymn-like, controlled feel.",
           "The structure turns at 'At once' in stanza three, when the thrush's song interrupts the gloom of the first two stanzas.",
           "The final lines end on uncertainty ('And I was unaware'), so hope is suggested but not confirmed."]),

dict(id="adlestrop", title="Adlestrop", author="Edward Thomas", date="1917", life="1878-1917",
     text="""Yes. I remember Adlestrop -
The name, because one afternoon
Of heat the express-train drew up there
Unwontedly*. It was late June.

The steam hissed. Someone cleared his throat.
No one left and no one came
On the bare platform. What I saw
Was Adlestrop - only the name

And willows, willow-herb, and grass,
And meadowsweet, and haycocks* dry,
No whit less still and lonely fair
Than the high cloudlets in the sky.

And for that minute a blackbird sang
Close by, and round him, mistier,
Farther and farther, all the birds
Of Oxfordshire and Gloucestershire.""",
     gloss=["Unwontedly: unusually", "haycocks: small heaps of hay"],
     focuses=[
      ("place", "a moment on a journey", "4-6", "the train's unexpected stop at a tiny station becomes a brief, still moment that the speaker remembers"),
      ("nature", "the countryside", "4-6", "the speaker notices the plants, hay and birdsong around the empty station, and the countryside seems to spread outwards"),
      ("memory", "a memory", "4-6", "the poem opens with 'Yes. I remember', as if answering a question, and shows how a trivial event can stay in the memory"),
     ],
     desc=["The station is described as almost empty: 'No one left and no one came / On the bare platform'.",
           "Sounds are carefully chosen: the steam hissing, someone clearing his throat, then the blackbird.",
           "The view widens from the platform to the plants, the sky and finally two whole counties."],
     lang=["The conversational opening 'Yes. I remember' gives a natural, personal voice.",
           "The list of plants joined by repeated 'And' creates a slow, peaceful pace.",
           "The phrase 'still and lonely fair' combines beauty with a sense of isolation.",
           "Words such as 'mistier' and 'Farther and farther' create a dreamy, expanding sound-picture."],
     form=["Four quatrains with a regular rhyme on alternate lines give a quiet, controlled shape.",
           "Enjambment across stanzas (the name 'only the name // And willows') carries the eye from the sign to the landscape.",
           "The poem builds from a single sound to 'all the birds', so the structure moves from the small and particular to the vast."]),

dict(id="innisfree", title="The Lake Isle of Innisfree", author="W. B. Yeats", date="1890", life="1865-1939",
     text="""I will arise and go now, and go to Innisfree,
And a small cabin build there, of clay and wattles* made;
Nine bean-rows will I have there, a hive for the honey-bee,
And live alone in the bee-loud glade.

And I shall have some peace there, for peace comes dropping slow,
Dropping from the veils of the morning to where the cricket sings;
There midnight's all a glimmer, and noon a purple glow,
And evening full of the linnet's* wings.

I will arise and go now, for always night and day
I hear lake water lapping with low sounds by the shore;
While I stand on the roadway, or on the pavements grey,
I hear it in the deep heart's core.""",
     gloss=["wattles: woven sticks used for building", "linnet: a small songbird"],
     focuses=[
      ("place", "a longed-for place", "4-6", "Innisfree is presented as an ideal island where the speaker could live simply and peacefully"),
      ("nature", "peace in nature", "4-6", "nature on the island is described as calm and gentle, bringing the speaker 'some peace'"),
      ("feelings", "longing", "7-9", "the final stanza reveals the speaker is standing on 'pavements grey', so the poem expresses a deep longing for escape from the city"),
     ],
     desc=["The speaker describes the life he imagines in detail: the cabin, 'Nine bean-rows', the beehive.",
           "Each time of day on the island has its own beauty: midnight 'a glimmer', noon 'a purple glow'.",
           "The grey city is only briefly glimpsed, but it makes the island seem even more beautiful."],
     lang=["The repeated 'I will arise and go now' sounds determined, almost like a vow or biblical declaration.",
           "Sound devices such as 'bee-loud glade' and 'lake water lapping with low sounds' use alliteration and assonance to create a soothing effect.",
           "Peace is described as something that 'comes dropping slow', making an abstract feeling seem physical and gentle.",
           "The phrase 'the deep heart's core' shows how deeply the longing is felt."],
     form=["Three quatrains with long lines and regular rhyme create a slow, musical rhythm.",
           "The shorter final line of each stanza gives a pause, like a moment of rest.",
           "The repetition of the opening line in the third stanza frames the poem and reinforces the longing to return."]),

dict(id="daffodils", title="I Wandered Lonely as a Cloud", author="William Wordsworth", date="1807 (revised 1815)", life="1770-1850",
     text="""I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the milky way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.

The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay*,
In such a jocund* company:
I gazed - and gazed - but little thought
What wealth the show to me had brought:

For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.""",
     gloss=["gay: (here) cheerful", "jocund: merry"],
     focuses=[
      ("nature", "the daffodils", "1-3", "the daffodils are presented as a huge, joyful crowd that seems to dance"),
      ("memory", "the power of memory", "4-6", "the final stanza shows that the memory of the daffodils can return later and cheer the speaker when he is alone"),
      ("feelings", "joy", "4-6", "the speaker moves from loneliness to delight, and the poem's final line shows his heart dancing with the flowers"),
     ],
     desc=["The daffodils are described as 'a crowd, / A host', suggesting vast numbers.",
           "Movement is central: the flowers are 'Fluttering and dancing', 'Tossing their heads'.",
           "The setting is described simply ('Beside the lake, beneath the trees'), keeping the focus on the flowers."],
     lang=["The opening simile 'lonely as a cloud' presents the speaker as detached and solitary.",
           "Personification of the daffodils as dancers and as 'jocund company' makes them seem like friends.",
           "The simile 'Continuous as the stars' and the hyperbole 'Ten thousand' emphasise abundance.",
           "The metaphor 'What wealth the show to me had brought' suggests the memory is valuable, like treasure."],
     form=["Four six-line stanzas, each with a quatrain and a rhyming couplet, create a regular, flowing rhythm.",
           "The first three stanzas describe the scene in the past; the final stanza shifts to the present and to memory.",
           "The poem ends where it began, with the daffodils, but the speaker's loneliness has become 'the bliss of solitude'."]),

dict(id="hope-feathers", title="'Hope' is the thing with feathers", author="Emily Dickinson", date="written c.1861; published 1891", life="1830-1886",
     text="""'Hope' is the thing with feathers -
That perches in the soul -
And sings the tune without the words -
And never stops - at all -

And sweetest - in the Gale - is heard -
And sore must be the storm -
That could abash* the little Bird
That kept so many warm -

I've heard it in the chillest land -
And on the strangest Sea -
Yet - never - in Extremity*,
It asked a crumb - of me.""",
     gloss=["abash: embarrass or silence", "Extremity: the worst of times"],
     focuses=[
      ("feelings", "hope", "4-6", "hope is presented as a small, constant bird living inside the soul, which keeps singing even in the hardest times"),
      ("feelings", "comfort in difficult times", "7-9", "the 'Gale', 'storm' and 'chillest land' stand for suffering, and hope is shown as a source of warmth that asks nothing in return"),
     ],
     desc=["The abstract idea of hope is described physically as a bird with feathers that perches and sings.",
           "Settings of hardship ('the chillest land', 'the strangest Sea') show where hope is most needed.",
           "The bird is described as 'little', which makes its endurance more impressive."],
     lang=["The extended metaphor of hope as a bird runs through the whole poem.",
           "'sings the tune without the words' suggests that hope is a feeling rather than a reasoned argument.",
           "Storm imagery ('Gale', 'storm') represents life's difficulties.",
           "The final line, 'It asked a crumb - of me', shows that hope gives without demanding anything."],
     form=["Three quatrains in a hymn-like rhythm give a simple, song-like quality.",
           "Dickinson's dashes create pauses and emphasis, making the voice hesitant yet thoughtful.",
           "Capitalisation of nouns such as 'Gale', 'Bird' and 'Sea' gives them weight; the final stanza moves to the personal 'I've heard it'."]),

dict(id="futility", title="Futility", author="Wilfred Owen", date="written 1918; published 1918", life="1893-1918",
     text="""Move him into the sun -
Gently its touch awoke him once,
At home, whispering of fields half-sown.
Always it woke him, even in France,
Until this morning and this snow.
If anything might rouse him now
The kind old sun will know.

Think how it wakes the seeds -
Woke once the clays of a cold star.
Are limbs, so dear-achieved, are sides
Full-nerved, still warm, too hard to stir?
Was it for this the clay grew tall?
- O what made fatuous* sunbeams toil
To break earth's sleep at all?""",
     gloss=["fatuous: pointless or foolish"],
     focuses=[
      ("feelings", "grief", "7-9", "the speaker's quiet instruction to move the dead soldier into the sun turns into anguished questioning"),
      ("society", "the waste of war", "7-9", "the death of one young soldier leads the speaker to question the point of life itself, showing war as a terrible waste"),
      ("nature", "the sun", "7-9", "the sun, once 'kind' and life-giving, is finally called 'fatuous' because it cannot bring the soldier back"),
     ],
     desc=["The scene is described with very few details: a dead soldier, the sun, snow in France.",
           "The soldier's past life is suggested through the memory of 'fields half-sown' at home.",
           "His body is described tenderly as 'still warm', which makes the loss more painful."],
     lang=["Personification of the sun as 'kind' and 'whispering' presents it as a gentle, caring force.",
           "Rhetorical questions in the second stanza express despair and confusion.",
           "The image of the clay that 'grew tall' alludes to the idea of humans created from earth, questioning the purpose of creation.",
           "The word 'fatuous' is a bitter final judgement that contrasts with 'kind old sun'."],
     form=["Two seven-line stanzas: the first is calm and hopeful, the second filled with questions.",
           "Owen uses half-rhyme (sun/once, sown/France) which creates a sense of something unresolved or broken.",
           "The poem ends on a question rather than an answer, leaving the reader with the speaker's grief."]),

dict(id="soft-rains", title="There Will Come Soft Rains", author="Sara Teasdale", date="1918", life="1884-1933",
     text="""There will come soft rains and the smell of the ground,
And swallows circling with their shimmering sound;

And frogs in the pools singing at night,
And wild plum trees in tremulous white;

Robins will wear their feathery fire,
Whistling their whims on a low fence-wire;

And not one will know of the war, not one
Will care at last when it is done.

Not one would mind, neither bird nor tree,
If mankind perished utterly;

And Spring herself, when she woke at dawn
Would scarcely know that we were gone.""",
     gloss=[],
     focuses=[
      ("nature", "nature's indifference to humans", "7-9", "the gentle, beautiful images of spring lead to the shocking idea that nature would not notice if humans disappeared"),
      ("society", "war and its consequences", "7-9", "written during the First World War, the poem imagines a world after humanity has destroyed itself"),
      ("nature", "the beauty of spring", "1-3", "the first half of the poem gives a delicate, joyful picture of spring through birds, frogs and blossom"),
     ],
     desc=["Spring is described through gentle sensory details: soft rain, the smell of the ground, frogs singing.",
           "Animals and plants are pictured going about their lives without humans.",
           "The final image of Spring waking 'at dawn' is calm, which makes the idea of human extinction more disturbing."],
     lang=["Soft sounds and sibilance ('swallows circling with their shimmering sound') create a peaceful tone.",
           "Personification of Spring as 'herself' who 'woke at dawn' presents nature as a living being.",
           "The repetition of 'not one' emphasises that nothing in nature would care.",
           "The phrase 'perished utterly' is blunt and final, contrasting with the delicate earlier language."],
     form=["Six rhyming couplets give a simple, song-like regularity.",
           "The fourth couplet marks a turn, introducing 'the war' and changing the poem's direction.",
           "The calm form contrasts with the disturbing message, which increases the irony."]),

dict(id="railway-carriage", title="From a Railway Carriage", author="Robert Louis Stevenson", date="1885", life="1850-1894",
     text="""Faster than fairies, faster than witches,
Bridges and houses, hedges and ditches;
And charging along like troops in a battle,
All through the meadows the horses and cattle:
All of the sights of the hill and the plain
Fly as thick as driving rain;
And ever again, in the wink of an eye,
Painted stations whistle by.

Here is a child who clambers and scrambles,
All by himself and gathering brambles;
Here is a tramp who stands and gazes;
And there is the green for stringing the daisies!
Here is a cart run away in the road
Lumping along with man and load;
And here is a mill and there is a river:
Each a glimpse and gone for ever!""",
     gloss=[],
     focuses=[
      ("place", "a train journey", "1-3", "the poem captures the speed of the train and the way the landscape rushes past the window"),
      ("family", "a child's view of the world", "4-6", "the excitement, imagination ('fairies', 'witches') and quick noticing of small details suggest a child's point of view"),
     ],
     desc=["A rapid series of sights is described: bridges, houses, hedges, horses, a tramp, a cart.",
           "People are glimpsed in brief moments (the child gathering brambles, the tramp who gazes).",
           "The stations are 'painted', a colourful detail seen in a flash."],
     lang=["The opening comparison 'Faster than fairies, faster than witches' is playful and imaginative.",
           "Similes such as 'like troops in a battle' and 'as thick as driving rain' express speed and energy.",
           "Alliteration and internal rhyme ('clambers and scrambles') add to the bouncing sound.",
           "The final line 'Each a glimpse and gone for ever!' suggests that life passes quickly."],
     form=["Rhyming couplets and a strong, galloping rhythm imitate the sound of the train on the track.",
           "The repetition of 'Here is ... here is' gives the sense of things appearing and vanishing.",
           "The second stanza slows slightly to focus on people, then ends with a thoughtful exclamation."]),

dict(id="self-unseeing", title="The Self-Unseeing", author="Thomas Hardy", date="1901", life="1840-1928",
     text="""Here is the ancient floor,
Footworn and hollowed and thin,
Here was the former door
Where the dead feet walked in.

She sat here in her chair,
Smiling into the fire;
He who played stood there,
Bowing it higher and higher.

Childlike, I danced in a dream;
Blessings emblazoned that day;
Everything glowed with a gleam;
Yet we were looking away!""",
     gloss=[],
     focuses=[
      ("memory", "a childhood memory", "7-9", "the speaker revisits a room from childhood and remembers a happy family scene"),
      ("family", "family members remembered", "4-6", "the mother smiling into the fire and the father playing the violin are remembered fondly, though they are now dead"),
      ("feelings", "regret", "7-9", "the final line suggests regret that the family did not realise how happy they were at the time"),
     ],
     desc=["The room is described in the present: an 'ancient floor', worn and 'hollowed'.",
           "The remembered scene places each family member precisely: 'She sat here', 'He ... stood there'.",
           "The child dancing 'in a dream' completes the picture of a warm, musical home."],
     lang=["'the dead feet walked in' is a haunting phrase that reminds the reader the people are gone.",
           "'Bowing it higher and higher' suggests the music growing lively and joyful.",
           "Light imagery ('glowed with a gleam', 'emblazoned') shows how precious the memory is.",
           "The exclamation 'Yet we were looking away!' expresses the regret of not noticing happiness."],
     form=["Three quatrains with alternate rhyme are short and controlled.",
           "The movement from 'Here is' to 'Here was' shifts from present to past.",
           "The final stanza moves from the speaker's dance to the reflective twist in the last line."]),

dict(id="up-hill", title="Up-Hill", author="Christina Rossetti", date="1861", life="1830-1894",
     text="""Does the road wind up-hill all the way?
   Yes, to the very end.
Will the day's journey take the whole long day?
   From morn to night, my friend.

But is there for the night a resting-place?
   A roof for when the slow dark hours begin.
May not the darkness hide it from my face?
   You cannot miss that inn.

Shall I meet other wayfarers at night?
   Those who have gone before.
Then must I knock, or call when just in sight?
   They will not keep you standing at that door.

Shall I find comfort, travel-sore and weak?
   Of labour you shall find the sum.
Will there be beds for me and all who seek?
   Yea, beds for all who come.""",
     gloss=[],
     focuses=[
      ("place", "a journey", "4-6", "the poem presents a long uphill journey and the promise of a resting-place at the end"),
      ("feelings", "uncertainty and reassurance", "7-9", "the anxious traveller asks questions and a calm voice reassures them, so the poem moves from worry to comfort"),
     ],
     desc=["The road is described as winding 'up-hill all the way', suggesting effort and difficulty.",
           "The journey lasts 'From morn to night', which may stand for a whole lifetime.",
           "The inn and its beds are described as welcoming and available to all."],
     lang=["The journey can be read as an extended metaphor for life, and the inn for death or heaven.",
           "Questions such as 'May not the darkness hide it from my face?' show fear and doubt.",
           "The calm answers ('You cannot miss that inn') are reassuring and gentle.",
           "'Those who have gone before' suggests people who have already died."],
     form=["The poem is a dialogue of questions and answers, with the answers indented.",
           "Four quatrains with alternating rhyme give a steady pace like walking.",
           "The poem ends with the inclusive promise 'beds for all who come', a firm and comforting close."]),

dict(id="break-break", title="Break, Break, Break", author="Alfred, Lord Tennyson", date="1842", life="1809-1892",
     text="""Break, break, break,
On thy cold gray stones, O Sea!
And I would that my tongue could utter
The thoughts that arise in me.

O, well for the fisherman's boy,
That he shouts with his sister at play!
O, well for the sailor lad,
That he sings in his boat on the bay!

And the stately ships go on
To their haven under the hill;
But O for the touch of a vanish'd hand,
And the sound of a voice that is still!

Break, break, break
At the foot of thy crags, O Sea!
But the tender grace of a day that is dead
Will never come back to me.""",
     gloss=[],
     focuses=[
      ("feelings", "grief", "7-9", "the speaker is unable to put his sorrow into words and longs for 'the touch of a vanish'd hand'"),
      ("nature", "the sea", "4-6", "the sea's endless breaking on the stones mirrors the speaker's grief and continues regardless of his loss"),
     ],
     desc=["The sea is described breaking on 'cold gray stones', a bleak, colourless image.",
           "Other people (the fisherman's boy, the sailor lad) are shown happy and active, in contrast with the speaker.",
           "The 'stately ships' going to their 'haven' suggest a world that carries on calmly."],
     lang=["The repeated 'Break, break, break' imitates the waves and suggests a breaking heart.",
           "Apostrophe ('O Sea!') shows the speaker addressing nature in his distress.",
           "Synecdoche in 'a vanish'd hand' and 'a voice that is still' focuses on small, lost details of a loved person.",
           "'a day that is dead' personifies time and shows that the past cannot return."],
     form=["Four quatrains with alternate rhyme; the first and last stanzas mirror each other.",
           "The heavy stresses of the opening line slow the rhythm.",
           "The structure moves from the sea, to others' happiness, to personal loss, and back to the sea, showing grief as circular."]),

dict(id="sympathy", title="Sympathy", author="Paul Laurence Dunbar", date="1899", life="1872-1906",
     text="""I know what the caged bird feels, alas!
When the sun is bright on the upland slopes;
When the wind stirs soft through the springing grass,
And the river flows like a stream of glass;
When the first bird sings and the first bud opes*,
And the faint perfume from its chalice steals -
I know what the caged bird feels!

I know why the caged bird beats his wing
Till its blood is red on the cruel bars;
For he must fly back to his perch and cling
When he fain* would be on the bough a-swing;
And a pain still throbs in the old, old scars
And they pulse again with a keener sting -
I know why he beats his wing!

I know why the caged bird sings, ah me,
When his wing is bruised and his bosom sore, -
When he beats his bars and he would be free;
It is not a carol of joy or glee,
But a prayer that he sends from his heart's deep core,
But a plea, that upward to Heaven he flings -
I know why the caged bird sings!""",
     gloss=["opes: opens", "fain: gladly"],
     focuses=[
      ("society", "freedom and captivity", "7-9", "the caged bird can be read as a symbol of people denied freedom, and the speaker's repeated 'I know' suggests personal experience"),
      ("feelings", "suffering", "7-9", "the bird's bleeding wing and 'old, old scars' express long-lasting pain, and its song is a 'prayer' rather than joy"),
     ],
     desc=["The first stanza describes a beautiful spring day outside the cage: bright sun, soft wind, flowing river.",
           "The bird's struggle is described in physical, painful detail: blood on 'the cruel bars', 'old, old scars'.",
           "The song is described not as joyful but as a desperate plea."],
     lang=["The refrain 'I know' expresses empathy and suggests the speaker shares the bird's experience.",
           "Natural imagery of freedom ('upland slopes', 'springing grass') contrasts sharply with 'cruel bars'.",
           "The phrase 'It is not a carol of joy or glee' overturns the reader's expectation about birdsong.",
           "Religious language ('prayer', 'Heaven') presents the bird's song as a cry for help."],
     form=["Three seven-line stanzas, each beginning and ending with a version of the refrain, give the poem a strong, insistent structure.",
           "The refrains build from 'what the caged bird feels' to 'why he beats his wing' to 'why the caged bird sings', deepening understanding.",
           "Regular rhyme and rhythm create a musical quality that echoes the bird's song."]),

dict(id="spring-and-fall", title="Spring and Fall", author="Gerard Manley Hopkins", date="written 1880; published 1918", life="1844-1889",
     text="""to a young child

Margaret, are you grieving
Over Goldengrove unleaving*?
Leaves, like the things of man, you
With your fresh thoughts care for, can you?
Ah! as the heart grows older
It will come to such sights colder
By and by, nor spare a sigh
Though worlds of wanwood leafmeal* lie;
And yet you will weep and know why.
Now no matter, child, the name:
Sorrow's springs are the same.
Nor mouth had, no nor mind, expressed
What heart heard of, ghost guessed:
It is the blight man was born for,
It is Margaret you mourn for.""",
     gloss=["unleaving: losing its leaves", "wanwood leafmeal: pale woods with leaves fallen and broken into pieces"],
     focuses=[
      ("family", "a child's grief", "7-9", "the speaker gently addresses a child who is crying over falling leaves, and explains that she is really mourning something deeper"),
      ("nature", "autumn", "7-9", "the falling leaves of 'Goldengrove' represent loss, change and death"),
      ("memory", "growing older", "7-9", "the speaker predicts that as Margaret grows older she will feel less for the leaves but understand more about sorrow"),
     ],
     desc=["The wood is given a beautiful, invented name, 'Goldengrove', which suggests autumn colours.",
           "The child's sadness is described with tenderness: 'are you grieving'.",
           "The future landscape of 'worlds of wanwood leafmeal' is pale and bleak."],
     lang=["The poem is addressed directly to Margaret, giving it a gentle, intimate tone.",
           "Compound words such as 'unleaving' and 'leafmeal' are invented to describe the process of loss.",
           "'the blight man was born for' suggests that suffering and death are part of being human.",
           "The final line reveals that Margaret mourns for herself, her own mortality."],
     form=["The poem is written in rhyming couplets (with one triplet), which gives it a song-like but serious quality.",
           "The structure moves from a question to an explanation to a final revelation.",
           "The last two lines both begin 'It is', building to the poem's strongest statement."]),

dict(id="westminster", title="Composed upon Westminster Bridge, September 3, 1802", author="William Wordsworth", date="1807", life="1770-1850",
     text="""Earth has not anything to show more fair:
Dull would he be of soul who could pass by
A sight so touching in its majesty:
This City now doth, like a garment, wear
The beauty of the morning; silent, bare,
Ships, towers, domes, theatres, and temples lie
Open unto the fields, and to the sky;
All bright and glittering in the smokeless air.
Never did sun more beautifully steep
In his first splendour, valley, rock, or hill;
Ne'er saw I, never felt, a calm so deep!
The river glideth at his own sweet will:
Dear God! the very houses seem asleep;
And all that mighty heart is lying still!""",
     gloss=[],
     focuses=[
      ("place", "the city", "4-6", "London at dawn is presented as calm, beautiful and almost natural, unlike the busy city it will become later in the day"),
      ("feelings", "awe and wonder", "7-9", "the speaker's exclamations show how deeply moved he is by the sight of the sleeping city"),
     ],
     desc=["The city is described in a list: 'Ships, towers, domes, theatres, and temples'.",
           "The scene is calm and quiet: 'silent, bare', 'the smokeless air'.",
           "The river and houses are described as peaceful and asleep."],
     lang=["The simile 'like a garment, wear / The beauty of the morning' presents the city dressed in light.",
           "Hyperbole in the opening line shows the speaker's admiration.",
           "Personification of the river and the houses suggests the city is a living being at rest.",
           "The metaphor 'that mighty heart' presents London as a great body, its heartbeat stilled for a moment."],
     form=["A Petrarchan sonnet: the octave describes the city; the sestet expresses the speaker's feelings.",
           "Exclamations ('Dear God!') in the sestet show the intensity of emotion.",
           "The final line pauses on 'lying still', capturing a moment before the city wakes."]),

dict(id="blake-london", title="London", author="William Blake", date="1794", life="1757-1827",
     text="""I wander thro' each charter'd* street,
Near where the charter'd Thames does flow,
And mark in every face I meet
Marks of weakness, marks of woe.

In every cry of every Man,
In every Infant's cry of fear,
In every voice, in every ban*,
The mind-forg'd manacles I hear.

How the Chimney-sweeper's cry
Every black'ning Church appalls;
And the hapless Soldier's sigh
Runs in blood down Palace walls.

But most thro' midnight streets I hear
How the youthful Harlot's curse
Blasts the new-born Infant's tear,
And blights with plagues the Marriage hearse.""",
     gloss=["charter'd: owned, controlled or mapped out by those with power", "ban: a law, curse or official ban"],
     focuses=[
      ("society", "life in the city", "7-9", "the speaker sees suffering everywhere in London and blames the people and institutions with power"),
      ("place", "the streets of a city", "4-6", "the city is presented through the speaker's walk, as a place of misery rather than beauty"),
     ],
     desc=["The speaker wanders the streets and sees 'Marks of weakness, marks of woe' in every face.",
           "Specific figures are picked out: the chimney-sweeper, the soldier, the young prostitute.",
           "The images of blood running down palace walls and blackened churches are vivid and shocking."],
     lang=["The repeated 'charter'd' suggests that even the river is owned and controlled.",
           "Repetition of 'every' shows that suffering is universal in the city.",
           "The metaphor 'mind-forg'd manacles' suggests people are trapped by ideas and attitudes as well as by laws.",
           "The oxymoron 'Marriage hearse' links love and death, suggesting that disease and poverty corrupt even marriage."],
     form=["Four quatrains with a regular rhyme scheme and strong rhythm create a relentless, marching effect.",
           "The poem moves through sight to sound ('I hear'), building in intensity.",
           "The final stanza, introduced by 'But most', presents the worst horror as the climax."]),

dict(id="ozymandias", title="Ozymandias", author="Percy Bysshe Shelley", date="1818", life="1792-1822",
     text="""I met a traveller from an antique land,
Who said - "Two vast and trunkless legs of stone
Stand in the desert .... Near them, on the sand,
Half sunk a shattered visage* lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them, and the heart that fed;
And on the pedestal, these words appear:
My name is Ozymandias, King of Kings;
Look on my Works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal Wreck, boundless and bare
The lone and level sands stretch far away." """,
     gloss=["visage: face"],
     focuses=[
      ("society", "power", "7-9", "the ruined statue of a proud king shows that human power is temporary"),
      ("memory", "time and its effects", "7-9", "time has destroyed the king's 'Works', leaving only a broken statue in empty sand"),
     ],
     desc=["The statue is described in fragments: 'vast and trunkless legs', a 'shattered visage'.",
           "The king's expression is described in detail: 'frown', 'wrinkled lip', 'sneer of cold command'.",
           "The surrounding desert is vast and empty, emphasising how little remains."],
     lang=["The words on the pedestal are deeply ironic: the 'Works' have vanished, so the 'Mighty' should despair for a different reason.",
           "Alliteration in 'boundless and bare' and 'lone and level sands' stresses emptiness.",
           "The short sentence 'Nothing beside remains.' is blunt and final.",
           "The phrase 'colossal Wreck' combines greatness with ruin."],
     form=["A sonnet, but with an unusual rhyme scheme, perhaps reflecting the broken statue.",
           "The story is told at second hand through 'a traveller', distancing the king further.",
           "The poem ends with the endless desert rather than the king, showing nature and time outlasting power."]),

dict(id="tropics-new-york", title="The Tropics in New York", author="Claude McKay", date="1920", life="1889-1948",
     text="""Bananas ripe and green, and ginger-root,
Cocoa in pods and alligator pears*,
And tangerines and mangoes and grape fruit,
Fit for the highest prize at parish fairs,

Set in the window, bringing memories
Of fruit-trees laden by low-singing rills*,
And dewy dawns, and mystical blue skies
In benediction over nun-like hills.

My eyes grew dim, and I could no more gaze;
A wave of longing through my body swept,
And, hungry for the old, familiar ways,
I turned aside and bowed my head and wept.""",
     gloss=["alligator pears: avocados", "rills: small streams"],
     focuses=[
      ("place", "homesickness", "4-6", "fruit in a New York shop window reminds the speaker of his Caribbean homeland and fills him with longing"),
      ("memory", "memories triggered by something ordinary", "4-6", "a display of fruit brings back memories of trees, streams and hills, showing how memory can be sudden and powerful"),
     ],
     desc=["The opening stanza is a rich list of tropical fruits, full of colour and abundance.",
           "The remembered homeland is described as peaceful and beautiful: 'dewy dawns', 'mystical blue skies'.",
           "The speaker's reaction is described physically: dim eyes, a wave through the body, bowed head."],
     lang=["Listing of fruit creates a sense of abundance and appeals to the senses.",
           "Religious imagery ('benediction', 'nun-like hills') makes the homeland seem sacred.",
           "The metaphor 'A wave of longing' shows the emotion as overwhelming and physical.",
           "'hungry for the old, familiar ways' links the fruit (food) with emotional hunger."],
     form=["Three quatrains with alternate rhyme.",
           "The structure moves from present (the window), to memory, to emotional response.",
           "The final line, with its sequence of actions joined by 'and', slows down and ends on 'wept'."]),

dict(id="the-oxen", title="The Oxen", author="Thomas Hardy", date="1915", life="1840-1928",
     text="""Christmas Eve, and twelve of the clock.
"Now they are all on their knees,"
An elder said as we sat in a flock
By the embers in hearthside ease.

We pictured the meek mild creatures where
They dwelt in their strawy pen,
Nor did it occur to one of us there
To doubt they were kneeling then.

So fair a fancy few would weave
In these years! Yet, I feel,
If someone said on Christmas Eve,
"Come; see the oxen kneel,

"In the lonely barton* by yonder coomb*
Our childhood used to know,"
I should go with him in the gloom,
Hoping it might be so.""",
     gloss=["barton: farmyard", "coomb: a small valley"],
     focuses=[
      ("memory", "childhood belief", "7-9", "the speaker remembers believing a Christmas legend as a child, and the poem contrasts that innocence with adult doubt"),
      ("feelings", "longing to believe", "7-9", "although he no longer believes, the speaker admits he would go to see the oxen 'Hoping it might be so'"),
     ],
     desc=["The childhood scene is cosy: children 'in a flock / By the embers in hearthside ease'.",
           "The oxen are imagined as 'meek mild creatures' in a 'strawy pen'.",
           "The final setting, 'the lonely barton' in 'the gloom', is darker and more uncertain."],
     lang=["The metaphor of children sitting 'in a flock' presents them as innocent like lambs.",
           "'So fair a fancy few would weave / In these years!' shows regret that such beliefs have faded.",
           "The word 'gloom' suggests the darkness of doubt as well as night.",
           "The final line, 'Hoping it might be so', is honest and wistful."],
     form=["Four quatrains with regular rhyme and rhythm, like a carol or ballad.",
           "The first two stanzas describe the past; the second half moves to the present.",
           "The turn at 'Yet, I feel' reveals the speaker's continuing wish to believe."]),

dict(id="when-you-are-old", title="When You Are Old", author="W. B. Yeats", date="1893", life="1865-1939",
     text="""When you are old and grey and full of sleep,
And nodding by the fire, take down this book,
And slowly read, and dream of the soft look
Your eyes had once, and of their shadows deep;

How many loved your moments of glad grace,
And loved your beauty with love false or true,
But one man loved the pilgrim soul in you,
And loved the sorrows of your changing face;

And bending down beside the glowing bars,
Murmur, a little sadly, how Love fled
And paced upon the mountains overhead
And hid his face amid a crowd of stars.""",
     gloss=[],
     focuses=[
      ("feelings", "love", "7-9", "the speaker claims that his love, unlike others', was for the woman's 'pilgrim soul', not just her beauty"),
      ("memory", "old age and looking back", "7-9", "the poem imagines the woman in old age, reading and remembering, so it looks forward to a future that will look back"),
     ],
     desc=["The woman is imagined in old age: 'old and grey and full of sleep', 'nodding by the fire'.",
           "Her younger self is recalled through her 'soft look' and 'shadows deep'.",
           "The final image of Love hiding 'amid a crowd of stars' is grand and mysterious."],
     lang=["The poem is addressed to 'you', giving it the feel of a private message or letter.",
           "Repetition of 'loved' contrasts the many admirers with the one true lover.",
           "'pilgrim soul' suggests a searching, restless spirit that the speaker valued.",
           "Love is personified as someone who 'fled' and 'hid his face', suggesting lost opportunity."],
     form=["Three quatrains with enclosed rhyme (abba) give a gentle, circular feel.",
           "The poem is one long sentence beginning with 'When', which creates a dreamy, flowing tone.",
           "The structure moves from her future, to the past, to a final, sad reflection."]),

dict(id="a-birthday", title="A Birthday", author="Christina Rossetti", date="1861", life="1830-1894",
     text="""My heart is like a singing bird
Whose nest is in a water'd shoot;
My heart is like an apple-tree
Whose boughs are bent with thickset fruit;
My heart is like a rainbow shell
That paddles in a halcyon* sea;
My heart is gladder than all these
Because my love is come to me.

Raise me a dais* of silk and down;
Hang it with vair* and purple dyes;
Carve it in doves and pomegranates,
And peacocks with a hundred eyes;
Work it in gold and silver grapes,
In leaves and silver fleurs-de-lys;
Because the birthday of my life
Is come, my love is come to me.""",
     gloss=["halcyon: calm and peaceful", "dais: a raised platform", "vair: fur used to decorate robes"],
     focuses=[
      ("feelings", "the joy of love", "4-6", "the speaker's happiness is so great that she compares her heart to several joyful natural things and calls for a celebration"),
      ("nature", "images from the natural world", "7-9", "natural images (a singing bird, a laden apple-tree, a shell in a calm sea) express fulfilment and contentment"),
     ],
     desc=["The first stanza describes nature at its most abundant and peaceful.",
           "The second stanza describes a luxurious, richly decorated platform for a celebration.",
           "Colours and materials (purple, gold, silver, silk) make the second stanza lavish and royal."],
     lang=["Anaphora of 'My heart is like' builds a sequence of similes, each more joyful.",
           "'My heart is gladder than all these' shows that no comparison is enough to express her feelings.",
           "Imperatives in the second stanza ('Raise', 'Hang', 'Carve', 'Work') show excitement and urgency.",
           "The metaphor 'the birthday of my life' suggests that love has given her a new life."],
     form=["Two eight-line stanzas: the first natural, the second artificial and decorative.",
           "Each stanza ends with the same idea, 'my love is come to me', which acts as a refrain.",
           "Regular rhythm and rhyme give the poem the quality of a song of celebration."]),
]
