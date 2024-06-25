# Kuznech! 

Kuznech is an implementation of Kuznyechik block cypher GOST R 34.12-2015.
It's using cbc encryption mode.



## Example 1: text encryption:

See results in `./examples/text-0` folder

```
python kuznech.py -e -K examples/text-0/key.txt -p examples/text-0/text-0.txt -o examples/text-0/text-0.enc.txt
python kuznech.py -d -k ./examples/text-0/key.txt -p ./examples/text-0/text-0.enc.txt -o examples/text-0/text-0.dec.txt
```

## Example 2: text encryption:

```sh
python kuznech.py -e -t "Дао, которое может быть выражено словами, не есть постоянное Дао. Имя, которое может быть названо, не есть постоянное имя. Безымянное есть начало неба и земли, обладающее именем – мать всех вещей. Поэтому тот, кто свободен от страстей, видит чудесную тайну [Дао], а кто имеет страсти, видит его только в конечной форме. Оба они (безымянное и обладающее именем) одного и того же происхождения"                                                                                                                                    
Total blocks:  98
Finished!
key:  21951881153354433090915124708858563344536366247101273623745415636278292077578
cypher:  33570094500485036931024994216278798205410004145601008667196604128363860853247627659403868631473881236522675706535665192739220680874788101376821904160442787505716233140386952609156182914634188159018466894417482846705789533498120612084768109826054580772819387521111191114528313845620907153237573708254835235887363508859122574469618495583811310783059982958442416199128865818276490488405986513291053279659626728747728078802241398109182586683255679382718957596777112568996100622341166293456052843879672444379313198340333565506426278943372956212092796834894871959600961978300619656719875527163189463337802602447384040912656268037693442572474569008594076945915932213985703570377792376186036383331188234114722585958363867336194676714681397514274097406762684117418225938712992229062146782716469488912572869397532623387351262604981930973882053051777561195166245328159938964921268864768412311374433915102619650442097533424414452012415232987766558508190721522949616744622744123181477289619362293531712479178371251521326696469959065225535196979834912454821750583055813384102539341396229403662781551392906009304540556797551339439928715582379663105879923777876769200725024353911417722630843262995679498928461352757842785655474549636981352336025564100021235559612480351912137640995780108235237767149664536984834119806882060810245910589928524330755292116675657013344663156187809662171866534156265617575899362334909957962917276658730938676610077478002540706948269909374764745912515846229837937131144116641366309785852374688517425088206075279517855807993868455364414493793389243087583305515160476188016693986190081816440555819912826342631151936736174867735975588064954429779542319175122679575133081138314501037979715259409965753645365098032571489430216970505056099028514902961314552438260991547589966439150715091720341945311870787511662571439711499729293661025249269478819417793751555151912755567824561671414575087339560795861247499975792595929512164347283396845090670943354648941902956718060207747586635486764440919285320001542577776468288314483288005436479252142507688758484688337759487499125532342805628676071173873773338088086507618776593767386415013612510945567642325653000850904345173918279777321691940209651789876398549181495150917618130831490298165013889901521215383958355243722518381381101338757824413416970766633897287678379418423415563889612486185962551673533359016468150065403488436817000455184979576379771784835945542553664767557833673466747584103144725697842087350497926378594221026975962986102223943692932021822806423997507505801603007652062112097477664894905394704598104736984330568284680598079236171575376681584745726432778920402332097318929321612461947337982655975095911866107843643906853991368544523947237991529292253008799170463953633785807721767739247354652655785963166654890601181446130836071192039629544317985835545500851107384504799312329690936092132809634266988102220849591993978647641532598001482503182142480400302063934572783646374280092587113051990954668299811966287962134478672144050040998313705245774604307642355966255747835318612947485343653377863784044927925879306046519024751598051175549679504912256683539165771010811799254416680669592097874147992320674843386709590349341829625025937987589871099552397427595030250919566706294380195864344964729350585705961212223290404001537067715489588057075471239579421178287731077659607950738162156305162099472125535016403725171365231857698812187362276197878029359387509949562901856278189491768524709961979059667907841830290642456949234565558879972768709093627129550436083833545266156893028608989209691212698938010379404032914298912472494428721421671771992502980932167733098174642953573464616100568840573486250082892871162633198741905795487955612517293864858168563042571748796872844659492057313071712391507445143115962084065556447729680121221691285661012587228360168
➜  Kuznechik git:(main) ✗ key=21951881153354433090915124708858563344536366247101273623745415636278292077578
➜  Kuznechik git:(main) ✗ cyp=33570094500485036931024994216278798205410004145601008667196604128363860853247627659403868631473881236522675706535665192739220680874788101376821904160442787505716233140386952609156182914634188159018466894417482846705789533498120612084768109826054580772819387521111191114528313845620907153237573708254835235887363508859122574469618495583811310783059982958442416199128865818276490488405986513291053279659626728747728078802241398109182586683255679382718957596777112568996100622341166293456052843879672444379313198340333565506426278943372956212092796834894871959600961978300619656719875527163189463337802602447384040912656268037693442572474569008594076945915932213985703570377792376186036383331188234114722585958363867336194676714681397514274097406762684117418225938712992229062146782716469488912572869397532623387351262604981930973882053051777561195166245328159938964921268864768412311374433915102619650442097533424414452012415232987766558508190721522949616744622744123181477289619362293531712479178371251521326696469959065225535196979834912454821750583055813384102539341396229403662781551392906009304540556797551339439928715582379663105879923777876769200725024353911417722630843262995679498928461352757842785655474549636981352336025564100021235559612480351912137640995780108235237767149664536984834119806882060810245910589928524330755292116675657013344663156187809662171866534156265617575899362334909957962917276658730938676610077478002540706948269909374764745912515846229837937131144116641366309785852374688517425088206075279517855807993868455364414493793389243087583305515160476188016693986190081816440555819912826342631151936736174867735975588064954429779542319175122679575133081138314501037979715259409965753645365098032571489430216970505056099028514902961314552438260991547589966439150715091720341945311870787511662571439711499729293661025249269478819417793751555151912755567824561671414575087339560795861247499975792595929512164347283396845090670943354648941902956718060207747586635486764440919285320001542577776468288314483288005436479252142507688758484688337759487499125532342805628676071173873773338088086507618776593767386415013612510945567642325653000850904345173918279777321691940209651789876398549181495150917618130831490298165013889901521215383958355243722518381381101338757824413416970766633897287678379418423415563889612486185962551673533359016468150065403488436817000455184979576379771784835945542553664767557833673466747584103144725697842087350497926378594221026975962986102223943692932021822806423997507505801603007652062112097477664894905394704598104736984330568284680598079236171575376681584745726432778920402332097318929321612461947337982655975095911866107843643906853991368544523947237991529292253008799170463953633785807721767739247354652655785963166654890601181446130836071192039629544317985835545500851107384504799312329690936092132809634266988102220849591993978647641532598001482503182142480400302063934572783646374280092587113051990954668299811966287962134478672144050040998313705245774604307642355966255747835318612947485343653377863784044927925879306046519024751598051175549679504912256683539165771010811799254416680669592097874147992320674843386709590349341829625025937987589871099552397427595030250919566706294380195864344964729350585705961212223290404001537067715489588057075471239579421178287731077659607950738162156305162099472125535016403725171365231857698812187362276197878029359387509949562901856278189491768524709961979059667907841830290642456949234565558879972768709093627129550436083833545266156893028608989209691212698938010379404032914298912472494428721421671771992502980932167733098174642953573464616100568840573486250082892871162633198741905795487955612517293864858168563042571748796872844659492057313071712391507445143115962084065556447729680121221691285661012587228360168
➜  Kuznechik git:(main) ✗ python kuznech.py -d -t $cyp -k $key
Finished!
Decrypted text:  Дао, которое может быть выражено словами, не есть постоянное Дао. Имя, которое может быть названо, не есть постоянное имя. Безымянное есть начало неба и земли, обладающее именем – мать всех вещей. Поэтому тот, кто свободен от страстей, видит чудесную тайну [Дао], а кто имеет страсти, видит его только в конечной форме. Оба они (безымянное и обладающее именем) одного и того же происхождения
```