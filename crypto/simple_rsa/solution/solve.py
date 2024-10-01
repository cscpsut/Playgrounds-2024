# write your code with explanation.

from Crypto.Util.number import * 
import string

ct = [14221884800500406190394393622086069870708198691028103676640757986864297733001859467164421569187130211795242561317369573158515502088251769800465437716662899642537787466709284106255546482246855779963235705128309223877017726469728622723079792371090408062693538753798372030645178744537326664595548809944459708147354361131226371318263399701934242300148717099353181634015099523082579542206957531067981500341038562014895746663889091151947316372571290996412291553706299192990659672907331093746798399823953185524771369049724335285348875412606393717337311962143350036033362467235663296184577164027580662683182374006084563612106, 13754419137628220378688966861080320742326630583315884681875567661153766228210657729929520144753658701088999051576330460717850449850724853833612232385780458619339027440240089943587562355632844767865535366865469054368917753625769775958720958477771280048193848537201420745471557773788915928120426259854252349595949759884069997011164504079283222101594766804704984199885385778269927192651960259296448618970920095544048325077871783750428606753119167760758915373892979707637854134901292226011892450749838501285331073710895628655849351351606242959374478274581150771519077601418004819259542700356299436248318304712231787276401, 2687651545658748306128145434464386907811010937434267829174422456195192547977084043480324506620543712637785825540419286607087763149303841490233670188127262246199025306085065341447370676961129760463585610011816800644105958102350905691543206252474917538550723872704712506292290037685645593022836407244211368325192827402198942286071395466478220726209317504965643738036901007599392015519702359723100895302641542089083667798632278119187268069602505621678902653562448478539207035660900930495817105140133867203272045447243892413191123679491201773277181010040259817219169539358038938566110941010926779694624090299457018393678, 8306598294010440383302678356076898070264909372201195383944279035922097801660578079571690697052206094221839479875457851650081195728248102092530892966418269392370032124573511470977252324154441212249688724439518142702602682136309800030457220217292827485265362338220030391569127665883008311607198447467589625894553773256776223399325773788658904245749932927382851076796570885779978132827008883190629030635600126698367347909947485536586863780480840641379926973372611062627103787563447426700884467659394634171472112609335074387988588880481559233305417938268057227136975612453225961210556639986047013412048916429711294008591, 15012963137120587890099311013184662911040251931210085541280947361385058715053965844141143569725077347806261466341362217676902533918495866899783351318601856624041644252043494228753477953480845424485518662144720751580593496783522381219377556501787394974455402916813245934020943069202715957813975564147360658279048365622831780007640117066088276874638174894252138802043738389936877009085569563167607243040032162180960256995214559592611922538718553255607161039494719689230247635086904897298323030421195430613545070047265489688237167246585250605171930495675999477110727161690032178148727243472099753213027907375600001675852, 7150149127177465355846349012418528006388765424594106218440456981031183434593764669458815465182709803103994407506646219838011311081207561786351403453825905639120840421600176704268641788378252462465029409758346710365485391273441338732530398778700529494418546993536920568166872571681251400352365655726116438536856389748322919224849187691822666612186251320580582069463705844775996051697562090732221361777052000063244322842963443435591719933344845152843117336850952679082584700600120176015513225580557011549337289447653815069173131530624861758756133288397273549177865933306031156337609349864889265427825521900992176536184, 13372261087108204239627340342457207331259504232107591592831716418097516055820307482084479185810431541866296594526951744803179265430651276659921539285206401725866009571630797413710173268294085550605950141814455244968819105293268744781528226144848170070180933895912572607854089220001931602566738562258780436560106572731753589817164573058470756036912548954491176949531824985211488954229078074983763967675442440342140082513723890287912176783157350357242890790990215847320802031623629950684070970409612334775425921280171342232096568788441657963679527889058247217286953634902591134804331419231775830896598521262309089261435, 11711747888925221956406812148620316230759687624395871626554654327798612974371042208280713056228057328939396235783218039544104583975323829433631143105762823596478252710586336456421032533495843170698533136732799449465402717566138013795426006084536587257364683399545822992650644924323531150224007289799252633686287043210385686889447740259673693249404761981743697160255565947888683315217064994783046018976104658904807792808592741486564187050655278756472266430345418947239627863515826769694863484318354278175511443128518046576236860706100545188082219583745723712142012087012658445291135131953451422757237632821657864445325, 15376252421217915784625004182854210611209856825271005299628162531598773239007649473317605979290351577938852288034323835698551765290669609249771060789377009439562119235949188025353386444151388342433597720186998027181776851771803786013120851303955580417543286868756634723240013500020558028038583853666687013591247730424930524590496311361010566414579661965949110212553755655883371254291328748242379044475335173403947558334774387568713062087196798648518246024420740294912392706972429533592675482014052150361418608428730738403962756330107158964721041123562150779649183806786994286039906749023963664563430290656885319899909, 6374509310917339641511872187797936580045648376341057073133072170830080703265391671869560443197033848571315113605040102874415800475971230519149980498419208659696358043713057252134527636770535957651955603494259540778629746902340724297212169480299363950075294874882164294157927294675719430944427040886383711033047231101978285802511152108102971384122705124154981730574073560454318346105303210226125779389369129319036852568478359147756127439404757790405765492218841968617320937956806698905996900432311808839117967674612248876254590865754773567562714247538797873682755927363012107365659162246317321256252586483266991258448, 3224717521118289241639908510948690682183035500752317431898818864059900946955785412833091907478146848163481586531142246819849561971447072267645769364909185484586702703073489039279535087123088656805707341060536743672354313409067579657734834904831051488114818386415011548221915152825902054802667273315518224552135739632756868256376330003544153290546872610438980979793397517628524256054630666471101018831421157129973316823183588727953089107020255149431252188027855329815272235548468705535464364017820652299982212029843070268704708163229789850188896784368633228830067368012623336085607891973655593122948299700168562385215, 6977823885403740397188172233575053410856272343865625342528126175601989891252488038075506554643571976873429111988583630237374379891411486229160502144436541946048682749534412443624186589956818244250288321923375193552219124718585740176198740138622554217787991975949583231058289818605511381512157826315365110805928915047950348237065172999859620472382016709688143924750758640538541974811929117710714341229546370268941691809226328469266087592499937981853544806903209366898340035109016901698744895740127230605955577444210373596748229009833762661746677186779425767606313359424828271010533467129995485776038046552974578523522, 8403829083963859713271822608914254066629401253319025604247354597406151028263902679844374967576422753160792648551605466075374491108447041978982464836909919161620569489799505521838699560010823120697638075162638827436410320845758624228638296056956340024407755985864577387872399635426213998888632037675438716600939674675489158895151367169042730359056609967670359493314042416060830131314589374922765833106798580051971623496180552275035067374371760938302968888487131651112078717080802552324342796005014816812808271245530636282003714988495800267411698051974943608239748832329510236907996597591001659049809904357387876347723, 12933685422218099037389038715031942339371319597341769655342993460342213978722676932887836583678899462639119038309311228690708699155701943913343555412825064895139721611643773427113371833348689395175070757930339295558727825286710146117052025693532890499436946253937161495632137929687111654649360743666591816303417451070165711044739854009986728975078628963976247937272595216502026197443571972567292048520728341496584884928958793581281492630706227145791560656057746759655328563800147421341684542671981802398352386220371541652893001121947578089467232774904764426269634574977013755481217195379788807514674989579481499013859, 15544585606452476220586396253581082956934007818600064541918341947482183079731715414483274697311277397040551430944997847532168558168968594694648533482964657831233061449097228166806259736183348031516777868965887171101455720307936456877997571063705261567991461692949073421651333572344984194744292930694888176000760921060655779142186639953996664933378098295611964850097799725809118441248408702109584838755758388997217560239150342290388671642594636735846615211962684222520374063911512152581816021934558717529752390647189004973943923804748720409900434102078477929260087930272532521392028660294475306767152683704600715414111, 6186277271943381946738125416026583206563624102237612790869722447994141847452436081161380053179592668313834425918994542587703099010628754686951064743529456722973381277352056212354224647169781117045413915279272699231482698479777891843980089800873594698198456252863966714950194618531001867607412866518845402222754590744056624113658775507900947234208804811606551169878014139409106499172767028727901913797745756920671645596580356734111202973493974706375650161791590420985251032630399209707169706686562225617153088305578484684517497703398567973079285124514521415178431345356512078279481569826367869259275708446571640293729, 10910614168797254250025519899041401662587744435721763546640569583482131310560437921491719700405560736427797719975872667375354676398913017979165696336215607464435628837934228002557166098349274222453747661026616064775079509890136754455454039364883909956591144941216070995260688123759240080516635415355533089451147520741026118736504474214893857861790200358403989606216246117347181912763186076175210188908120870527248450292303626457900172779495352411308712276067561774605608326908437181313027597539318341773641172741370836248991684658492820984533891550656244013808984939100941965629701998132206782087057376945789870948356, 10910614168797254250025519899041401662587744435721763546640569583482131310560437921491719700405560736427797719975872667375354676398913017979165696336215607464435628837934228002557166098349274222453747661026616064775079509890136754455454039364883909956591144941216070995260688123759240080516635415355533089451147520741026118736504474214893857861790200358403989606216246117347181912763186076175210188908120870527248450292303626457900172779495352411308712276067561774605608326908437181313027597539318341773641172741370836248991684658492820984533891550656244013808984939100941965629701998132206782087057376945789870948356, 7624995961658007873687893559180432484438982543133407522741924146795736532504538591729699404565558630176275252213036424594145804733260498190386668156558020855774670761867973735456458996763786592593999431011471574135498814382520282113935347189186603906194384852182373069769696231484237679783436924803224958590490126379089221075633768302880755541435514284122970756750139500556173817387928050811329093438873764311068298357189166508764393878646353517442789208269498242610550154224374725214602813269012577593527018987835265218295649218914989030526979242763317678569566789832049158751262324517985109385196350566005299679228, 3224717521118289241639908510948690682183035500752317431898818864059900946955785412833091907478146848163481586531142246819849561971447072267645769364909185484586702703073489039279535087123088656805707341060536743672354313409067579657734834904831051488114818386415011548221915152825902054802667273315518224552135739632756868256376330003544153290546872610438980979793397517628524256054630666471101018831421157129973316823183588727953089107020255149431252188027855329815272235548468705535464364017820652299982212029843070268704708163229789850188896784368633228830067368012623336085607891973655593122948299700168562385215, 14702448392318579566693452374309865843029574436394580624289893306424129234228845984507765438766536977337578369343726169244515456057269013755869232181626546826024712616017907256335382710918446919099313780392589951339710568037441247378698553106664284838210719890152886355994888901332964428062951257897430928079290839011330427285649041463413194468257387438672648020792018901450272803386260529948072371387586725699594890104768155040162162291489382412852328583879877425915693569864873197614339762227438289396981152293295026419585479458370435074008442072297139198638686405583213423763391566398778689608076508925663115468628, 9762279542038659865187234888507875451120019885259674392498891026666374318780625437943853978498272192600221601383069578343578242124516335045033846694009462231789388305941749243195365105608992789663981123375141011905947787056959476964876690200902677790907384076647393681128392998074068318631172761641826249745916816896646624180459278932328990873905036232858870033100162820517732399558151340000171804878354737029375992162441287825999740982975511357994212292147273716444460989914389963886812102072206212769770593951670318996436068367746043322751199558984307972185468746543529692359554128267653394549568216447490457250206, 9762279542038659865187234888507875451120019885259674392498891026666374318780625437943853978498272192600221601383069578343578242124516335045033846694009462231789388305941749243195365105608992789663981123375141011905947787056959476964876690200902677790907384076647393681128392998074068318631172761641826249745916816896646624180459278932328990873905036232858870033100162820517732399558151340000171804878354737029375992162441287825999740982975511357994212292147273716444460989914389963886812102072206212769770593951670318996436068367746043322751199558984307972185468746543529692359554128267653394549568216447490457250206, 8076994744345700730735898759741850758723033178574199342842761083655096719415405261598257341679258643375810313610744078794428662909962139229943967606453075755289587744012418514041498291986038273640904494468804467043713947536660404786103188779847903310351965359465127948123105565323628602015392265861857390842639413557018934318887550476288339846237930621007150549110541216424874336767344281003427589856377302232718087697801131803508992161729448254941497787498179421170208780428802343287586307271025255755610395455387084629146999534199836583729063611613097378502528343788028737420884642708968518485556838687003494493392, 8076994744345700730735898759741850758723033178574199342842761083655096719415405261598257341679258643375810313610744078794428662909962139229943967606453075755289587744012418514041498291986038273640904494468804467043713947536660404786103188779847903310351965359465127948123105565323628602015392265861857390842639413557018934318887550476288339846237930621007150549110541216424874336767344281003427589856377302232718087697801131803508992161729448254941497787498179421170208780428802343287586307271025255755610395455387084629146999534199836583729063611613097378502528343788028737420884642708968518485556838687003494493392, 8076994744345700730735898759741850758723033178574199342842761083655096719415405261598257341679258643375810313610744078794428662909962139229943967606453075755289587744012418514041498291986038273640904494468804467043713947536660404786103188779847903310351965359465127948123105565323628602015392265861857390842639413557018934318887550476288339846237930621007150549110541216424874336767344281003427589856377302232718087697801131803508992161729448254941497787498179421170208780428802343287586307271025255755610395455387084629146999534199836583729063611613097378502528343788028737420884642708968518485556838687003494493392, 6109146589701245122745497883778095691108476354311862788597178950397808687632502596794272657713897791833759513149615060101480629899731194619223534865219571006378546297702839375652188051203652445888826471812985153844762188003255218925228172937352901126719731793425632097038567561151302695254962668106064855679228060720854272336919385560737442342180467279592179778352899425702735842214183124736803354470229440599783762431483670488218905711224008408659680262214609376646081811014431443614930442547753335042673817747329495002301157220313495609030715916727073989635932038353840445971852414800223655621058709812915153097312, 8306598294010440383302678356076898070264909372201195383944279035922097801660578079571690697052206094221839479875457851650081195728248102092530892966418269392370032124573511470977252324154441212249688724439518142702602682136309800030457220217292827485265362338220030391569127665883008311607198447467589625894553773256776223399325773788658904245749932927382851076796570885779978132827008883190629030635600126698367347909947485536586863780480840641379926973372611062627103787563447426700884467659394634171472112609335074387988588880481559233305417938268057227136975612453225961210556639986047013412048916429711294008591, 13372261087108204239627340342457207331259504232107591592831716418097516055820307482084479185810431541866296594526951744803179265430651276659921539285206401725866009571630797413710173268294085550605950141814455244968819105293268744781528226144848170070180933895912572607854089220001931602566738562258780436560106572731753589817164573058470756036912548954491176949531824985211488954229078074983763967675442440342140082513723890287912176783157350357242890790990215847320802031623629950684070970409612334775425921280171342232096568788441657963679527889058247217286953634902591134804331419231775830896598521262309089261435, 11711747888925221956406812148620316230759687624395871626554654327798612974371042208280713056228057328939396235783218039544104583975323829433631143105762823596478252710586336456421032533495843170698533136732799449465402717566138013795426006084536587257364683399545822992650644924323531150224007289799252633686287043210385686889447740259673693249404761981743697160255565947888683315217064994783046018976104658904807792808592741486564187050655278756472266430345418947239627863515826769694863484318354278175511443128518046576236860706100545188082219583745723712142012087012658445291135131953451422757237632821657864445325, 10910614168797254250025519899041401662587744435721763546640569583482131310560437921491719700405560736427797719975872667375354676398913017979165696336215607464435628837934228002557166098349274222453747661026616064775079509890136754455454039364883909956591144941216070995260688123759240080516635415355533089451147520741026118736504474214893857861790200358403989606216246117347181912763186076175210188908120870527248450292303626457900172779495352411308712276067561774605608326908437181313027597539318341773641172741370836248991684658492820984533891550656244013808984939100941965629701998132206782087057376945789870948356, 11711747888925221956406812148620316230759687624395871626554654327798612974371042208280713056228057328939396235783218039544104583975323829433631143105762823596478252710586336456421032533495843170698533136732799449465402717566138013795426006084536587257364683399545822992650644924323531150224007289799252633686287043210385686889447740259673693249404761981743697160255565947888683315217064994783046018976104658904807792808592741486564187050655278756472266430345418947239627863515826769694863484318354278175511443128518046576236860706100545188082219583745723712142012087012658445291135131953451422757237632821657864445325, 1014949716628710422188147595142313957417670530450140918078336808320985105728791704843299129167843392021003923965987765938450515751394935840361214008300804365487442005416959090269692248275979032264996529077474005470249173492310910356437696857470800706943600413556998535045521054158083740288258470914013100326810737000419349644998209434892601706388835839380378847606320299432329278647174492271298035084246219915595966558632329416966224798801768595940973437343273397065362587584657105242757065844719233857176138741688652015834289191787666256965342958283594790947881585233455463082518567962319539965864238525403382471365, 14692076811253630692941546862561442639278043945339969777033602386805649284610669914584385153405640901585719879416520946813491452366455247682746050018125267055785587981058331241498443154705163024034341461999979173117666966134949872108450797817969522215314839204995713543339106393493686018161859443712128228649799947477917978815354984203010202804673200349861006212865779869289879592407880527023632507255111861527801606465289205858025730235996798161703669279982099029043175387266538747636829019351630514637996417133140973737975793496038271795203533444655253550497864163840642411610803095884588663157798747672073391965502, 6109146589701245122745497883778095691108476354311862788597178950397808687632502596794272657713897791833759513149615060101480629899731194619223534865219571006378546297702839375652188051203652445888826471812985153844762188003255218925228172937352901126719731793425632097038567561151302695254962668106064855679228060720854272336919385560737442342180467279592179778352899425702735842214183124736803354470229440599783762431483670488218905711224008408659680262214609376646081811014431443614930442547753335042673817747329495002301157220313495609030715916727073989635932038353840445971852414800223655621058709812915153097312, 14220257284591899832809455915536989801731526918870351509135632687884308136534243499158661338447417940104811209426944576983834103214291482176080652092204880225430681013046979992886929158801317058422284680142250865152450153364506868843775796756379983661024559181460340912495913334958858589613601053347665049359980472210467669364761161284795630096059381456534801971815518910694360561649007767478705434153385325315235634567957929484648375647805448485916963962411616025273336571947534389616264818857277677339871352256605421028586043376957016588023143751473662551444604449388376960028403176105611978575906483215893826332454, 13372261087108204239627340342457207331259504232107591592831716418097516055820307482084479185810431541866296594526951744803179265430651276659921539285206401725866009571630797413710173268294085550605950141814455244968819105293268744781528226144848170070180933895912572607854089220001931602566738562258780436560106572731753589817164573058470756036912548954491176949531824985211488954229078074983763967675442440342140082513723890287912176783157350357242890790990215847320802031623629950684070970409612334775425921280171342232096568788441657963679527889058247217286953634902591134804331419231775830896598521262309089261435, 14900117520708980686401758570167453448033222114503639992256965287877828633799789316653624574342891469691434795966193820649358360563845661837581661497731757009750506178588396601174930182777258261354411672877228444766546753699045618954044754128592980180626920594201908266896779118565216850057839341745401904987331468407970949940038594498329355020096534307561036503321557689113503902853334941975736556914720282930694527175394425686780591800845036101068327653131545299755729293723324086364277267239363552787416996980254110654192761673152577683000036411132365057201838543129366928578075620366346439721145666302546508716556, 9762279542038659865187234888507875451120019885259674392498891026666374318780625437943853978498272192600221601383069578343578242124516335045033846694009462231789388305941749243195365105608992789663981123375141011905947787056959476964876690200902677790907384076647393681128392998074068318631172761641826249745916816896646624180459278932328990873905036232858870033100162820517732399558151340000171804878354737029375992162441287825999740982975511357994212292147273716444460989914389963886812102072206212769770593951670318996436068367746043322751199558984307972185468746543529692359554128267653394549568216447490457250206, 8076994744345700730735898759741850758723033178574199342842761083655096719415405261598257341679258643375810313610744078794428662909962139229943967606453075755289587744012418514041498291986038273640904494468804467043713947536660404786103188779847903310351965359465127948123105565323628602015392265861857390842639413557018934318887550476288339846237930621007150549110541216424874336767344281003427589856377302232718087697801131803508992161729448254941497787498179421170208780428802343287586307271025255755610395455387084629146999534199836583729063611613097378502528343788028737420884642708968518485556838687003494493392, 2687651545658748306128145434464386907811010937434267829174422456195192547977084043480324506620543712637785825540419286607087763149303841490233670188127262246199025306085065341447370676961129760463585610011816800644105958102350905691543206252474917538550723872704712506292290037685645593022836407244211368325192827402198942286071395466478220726209317504965643738036901007599392015519702359723100895302641542089083667798632278119187268069602505621678902653562448478539207035660900930495817105140133867203272045447243892413191123679491201773277181010040259817219169539358038938566110941010926779694624090299457018393678, 10910614168797254250025519899041401662587744435721763546640569583482131310560437921491719700405560736427797719975872667375354676398913017979165696336215607464435628837934228002557166098349274222453747661026616064775079509890136754455454039364883909956591144941216070995260688123759240080516635415355533089451147520741026118736504474214893857861790200358403989606216246117347181912763186076175210188908120870527248450292303626457900172779495352411308712276067561774605608326908437181313027597539318341773641172741370836248991684658492820984533891550656244013808984939100941965629701998132206782087057376945789870948356, 14220257284591899832809455915536989801731526918870351509135632687884308136534243499158661338447417940104811209426944576983834103214291482176080652092204880225430681013046979992886929158801317058422284680142250865152450153364506868843775796756379983661024559181460340912495913334958858589613601053347665049359980472210467669364761161284795630096059381456534801971815518910694360561649007767478705434153385325315235634567957929484648375647805448485916963962411616025273336571947534389616264818857277677339871352256605421028586043376957016588023143751473662551444604449388376960028403176105611978575906483215893826332454, 6186277271943381946738125416026583206563624102237612790869722447994141847452436081161380053179592668313834425918994542587703099010628754686951064743529456722973381277352056212354224647169781117045413915279272699231482698479777891843980089800873594698198456252863966714950194618531001867607412866518845402222754590744056624113658775507900947234208804811606551169878014139409106499172767028727901913797745756920671645596580356734111202973493974706375650161791590420985251032630399209707169706686562225617153088305578484684517497703398567973079285124514521415178431345356512078279481569826367869259275708446571640293729, 6777316802187703884138540787633716602221060989536904949334551960158567562991103437083977657529222430003026195561555298874878001615382277172375784385814684677252382929374198805797428726636240490009499139797593286969889673365211330006962290703474036960974580769216909815313444031693291626645012780618946651661012089482891318688426336033859606179867933342026382270587883900628876514057582344754456821559424008055536616170338694720448453865458986276569035628803448286464912875526153233555174018852552187038908031517972053633358110291838244091525104873102174871950781823738077052911050525722025830472662562392631279797639, 6383415205455093629560746934481827082910485519608956872112017107846335896623265514815701381348844002514612306988165814121969001202872922379278074624944721914005057940866923476163956650254246114165100087121056172277817409881489213302245890962492352869908387197274604014654525183761136164077733893617529335992331092720871698437931343678803273531409235257257385274307379906150679784406696894419965072036615263219801158570941685943782408809135951104735939571176712606267450782732040368703441088316165918672039783049695656482025808445229487373064862199326331455509167537870899367754084476207497245932893702710164739169883, 6375958161842344068792224252367356920738540638935345165215852134917635035102771537362551157352234837851303290094706210753465618711966612527195429876162480851946453675823174145721066522244776007456993287194574672798342128663865211331956295496562360522767755989748975362220843071983812377239827142413752059470993475833892705822761338174676456854196623248046027133634542340552847123767114566361407587335071667058124042919758125161245279616997069412805681512020732745720798602105354204728759871943124211072234828043517651594752955987079044861711385684603759567453893316103109388875239874523666312202806233962649674072386, 8167419786197395095964426102694827292131330652533607940107543674735087473617569403199087817389946525945543704307477312281806087621606382516592443107995258431697047567614898094580407219482159582386492907491624662852588688103597239526159268316314639107958684309889808202916809142046355105479173842751432231547304847642976015595975014999373266388186127112269220615181926592015683877059937728363579054426765118894316749945070615722298426577110238135847500007913633548524259571200614339134424929636488795434117317860407068399640555279579791041990135447878167257479858905431157804069084900814536425979518058221543145158805, 13001861490491854607543333152002153734229136676346650676181387148436761637627358329315836171161954377180128522864962140250354914262695133101922028658017149373743812480021104592524533464615698157760514995014449820881369314737583833898630190772286957208886403585780919647439839061786652964171317566345280213096158975599348471549870984370590457998209056187258308214091171437201822915273246142872180484013318658047257143663920728712100321058277324516095232627095119764672112078726584239669662858308281439793473356428840589693796703458103929063744331589231416051749950893816800916380375333798390756590931978331522376321285, 4248846666441167725374668381028312274954621998673736315524850201081464827064398034952820630815469584259898989434726823213919986437496778243356277374105844489636607459665466279026358150359218773489552923617782425954499378426393164986316988563824736883131366361333769643633925191231275577584035032058829882500189524141821626067784270807810482816222880793286077831380705926105929550398381291888492302439138628664654655589666621066659492678233604363486658079390416083261250121143193892333925255685645573768713370616141921939920808609045022520544381429286270050974989976898753029911461029709288582670213063515914223112257, 11405611304099817911934986419514230717110674376481782940728321106899719789745125939849941121247045362860876148056047977759823163829929358446082746369017606658116497066355765959942809758064750958098829587176226550423435229452600866357703025197002066115465568567179390724402705587344781836584227359071378097217896866609769422286392225343768133825529380618279500801583741749367332901819976650780441873856041841852936605119102698770141736193591802052427692549990851626267257320576885788299145891292579980238838658716743181609793441357149738881245289154039173923233761774096947826876951488242432013494987299794413238964902, 1505525658864456426374972420478434188691586389958629180014821668041932267212776458595305969803096147094743339494997544560258587520323451451329629193960221967974033919188413609568259223627465748544043555941940452518058214178902414614231851657692171972640450448393773403675787267717375003968150835554209309596813977098382145249918951205023035549362635942486779621273283736086117198612848691596767416458688308216046842913651620549505095282048394356002902719603302344904190547928804350622982901260834189056253638912385955667642737236586299063847576176093095990125228034645216132487936657528765265598474435050404168547611, 13973028018420493711416554141730174031027199840189063404795311449288220484805709535203552031894026162724291204051680717441367641962395363270979171414303522320489551957756426034441933482162567709635906205661974108433796425938328520554182860023317265773903962571289544015635898134699472552059215255722599906145850966820621024575864762339324068043740754678171087660487541919877617951153205870553685537699828197974427434766144925159134966482797994615818733251846716677385737391558071533308731947747384866302535148549322304018862169738717129369690429273606143883833249874965128778713638987358937075044029699970609210577257, 15012963137120587890099311013184662911040251931210085541280947361385058715053965844141143569725077347806261466341362217676902533918495866899783351318601856624041644252043494228753477953480845424485518662144720751580593496783522381219377556501787394974455402916813245934020943069202715957813975564147360658279048365622831780007640117066088276874638174894252138802043738389936877009085569563167607243040032162180960256995214559592611922538718553255607161039494719689230247635086904897298323030421195430613545070047265489688237167246585250605171930495675999477110727161690032178148727243472099753213027907375600001675852, 10812612281070762425790639727985117919353911357249095608221493282670254684411833000800024109382993315940185278994811208430093195461352902924141531735710901479587718353177454927400803123367747263352037833627021146533883344010747431356431529881485108678207808600738203863664052525090262286026040311935143372704243111060276206768075270336368555004890005264438180698335385598685834512294831948024589848086396337482165853417994971125755371141587659911404087338762092206622656940911212782437746204409641501930394763530533503700679609628026007075873630843551788116318491588148928922398831078943621186882432310011813904620668, 6836116492787913413559489481461133684688781269878109718920409323785980998865498356818715522144038619145732984166343561895703522091885703971169847704279226890844168385076888421452799024894429980380251409035623280279509087050503352356294329904256460503003540892467901495166906794905101323183700473099255778196863978154616331700138704563564464270435724297366469839719738811420123552155870047879203193860478951983810962197399152187229670385539688485521873420964785645638570532664169077959885909778162249063322495790084587908829525107618773500460951767860024839889717099955619132762466739280062307510335411544362911998955, 15376252421217915784625004182854210611209856825271005299628162531598773239007649473317605979290351577938852288034323835698551765290669609249771060789377009439562119235949188025353386444151388342433597720186998027181776851771803786013120851303955580417543286868756634723240013500020558028038583853666687013591247730424930524590496311361010566414579661965949110212553755655883371254291328748242379044475335173403947558334774387568713062087196798648518246024420740294912392706972429533592675482014052150361418608428730738403962756330107158964721041123562150779649183806786994286039906749023963664563430290656885319899909, 7845698584599939185235088590997086361367886340015698036384374217862166615337808068338871553313254113869685232545332008433316251190001272089712305391245383282430733768987326257811838209736655230910822259143031540601854673967749681568012361635725920831230509357390724654658679448025169501817632227511373710669545200747582193375996098761259025933192072914388850655445631372927187742020878083714348339474864326033832844859109414061643487118108571087043486611990610827491427499490816281947843608478144429410876981812354079645828996569588448289422081011289929395566512697944873921778005754427075443012380087059085959012370, 81015126793492000191925196611846914693345513896726684703757803732172177163191864842819578690152776761591359762298309831466740877104602253162410193409690086242910100778499051296942823406466593644889782885289399646922216311717606333725829272334048828992718054255644966462579392208286359029399133197205797251057074428284674902447638501251453619498883383850978842961411808825712867580196086255879063607774294432349633218557267818714904679185139561998225628285161138014476512731763086482177467986224886529006232787976273725577139197146688522371820754463306104862065882966404597385487566528971223973887444352009747549805]
n = 15855345621000569331600311696395025138250647615006814401643102161970822924576959096372743332238137548424574897522736250244115737274425243542337158805251950632851274380669903026601039611867282903748051047490284438412650094188509649014124577387130725346648002380656538139076108222016560735586005858080920588870430629334193518944170226436126917202835614612162333719569014768268348738892576210437934599203156174985578050879129262189753755679150795806905605650997167538167790504544896947540289815712469461505280065210107692232614495337816763477444607874380684669148325953584718447361451281402603717940514540226891393164617

printables = string.printable
enc_printables = [pow(ord(c), 0x10001, n) for c in printables]


for c in ct:
    if c in enc_printables:
        print(printables[enc_printables.index(c)], end='')
    else:
        print(c, end='')
print()