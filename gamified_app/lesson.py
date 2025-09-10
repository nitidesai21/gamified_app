from flask import session
lessons = [
    {
        "id": 1,
        "subject": "Maths",
        "title":{
            "english": "The Magical Rope",
            "hindi": "जादुई रस्सी",
            "gujarati": "જાદુઈ દોરી"
        },
        "content": {
            "english": """
There were two good friends in a small village—Golu and Molu. One day, they found a magical rope at the village fair. This rope was very special—whenever someone pulled it, more objects appeared out of nowhere!

Golu and Molu got curious. Golu already had 3 apples. When he pulled the magical rope, suddenly, 2 more apples appeared in front of him!

Molu asked, “Golu, how many apples did you have at first?”
Golu said, “I had three.”
Molu asked again, “And how many apples appeared now?”
Golu said, “Now I got two more!”

Molu asked, “So how many apples do you have in total now?”

Golu and Molu started counting all the apples together:
“One, two, three, four, five!”
They both shouted happily, “Wow! Now we have 5 apples!”

The magical rope spoke, “Whenever you put things together and count everything, that’s called addition!”

Golu and Molu loved this new trick. All day, as they explored the fair, they used the magical rope to add and count things—balloons, balls, and sometimes toys!

By the end of the day, they realized addition means joining two or more groups and counting to find out how many there are in all.

Moral:
Golu and Molu learned that addition is as simple as counting everything together, and math can be fun and magical!
""",
            "hindi": """
एक छोटे से गाँव में दो अच्छे दोस्त थे—गोलू और मोलू। एक दिन उन्होंने गाँव की मेले में एक जादुई रस्सी पाई। यह रस्सी बहुत खास थी—जब भी कोई इसे खींचता, चीजें अचानक सामने आ जातीं!

गोलू के पास पहले से 3 सेब थे। जब उसने जादुई रस्सी खींची, अचानक उसके सामने 2 और सेब आ गए!

मोलू ने पूछा, “गोलू, पहले तुम्हारे पास कितने सेब थे?” गोलू ने कहा, “मेरे पास तीन थे।” मोलू ने फिर पूछा, “और अब कितने सेब आए?” गोलू ने कहा, “अब मुझे दो और मिले!”

फिर मोलू ने पूछा, “तो अब तुम्हारे पास कुल कितने सेब हैं?”

गोलू और मोलू ने मिलकर सभी सेब गिनने शुरू किए: “एक, दो, तीन, चार, पाँच!” वे दोनों खुश होकर बोले, “वाह! अब हमारे पास 5 सेब हैं!”

जादुई रस्सी बोली, “जब भी आप चीजों को एक साथ जोड़ते हैं और सबकुछ गिनते हैं, उसे जोड़ना कहते हैं!”

गोलू और मोलू ने इस नए तरीके को पसंद किया। पूरे दिन, मेले में घूमते हुए वे जादुई रस्सी का उपयोग करके चीजें जोड़ते और गिनते रहे—गुब्बारे, गेंदें और कभी-कभी खिलौने!

दिन के अंत तक, उन्होंने समझा कि जोड़ना दो या अधिक समूहों को मिलाकर उनकी कुल संख्या गिनना होता है।

नैतिक: गोलू और मोलू ने सीखा कि जोड़ना बस सबकुछ मिलाकर गिनना है, और गणित मज़ेदार और जादुई हो सकता है!
""",
            "gujarati": """
એક નાના ગામમાં બે સારા મિત્રો હતા—ગોલૂ અને મોલૂ. એક દિવસ તેમને ગામના મેળામાં જાદુઈ દોરી મળી. આ દોરી ખાસ હતી—જ્યારે કોઈ તેને ખેંચતો, કોઈ અચાનક વસ્તુઓ ઊભી થઇ જતી!

ગોલૂ પાસે પહેલાથી જ 3 સફરજન હતા. જ્યારે તેણે જાદુઈ દોરી ખેંચી, અચાનક તેના સામે 2 વધુ સફરજન આવી ગયા!

મોલૂએ પૂછ્યું, "ગોલૂ, તારા પાસે પહેલાં કેટલા સફરજન હતા?" ગોલૂએ કહ્યું, "મારા પાસે ત્રણ હતા." મોલૂએ ફરી પૂછ્યું, "અને હવે કેટલા આવ્યા?" ગોલૂએ કહ્યું, "હવે મને બે વધુ મળ્યા!"

મોલૂએ પુછ્યુ, "તો હવે તારા પાસે કુલ કેટલા સફરજન છે?"

ગોલૂ અને મોલૂએ બધા સફરજન મળીને ગણવા શરૂ કર્યા: "એક, બે, ત્રણ, ચાર, પાંચ!" બંને ખુશીથી બોલ્યા, "વાહ! હવે અમારા પાસે 5 સફરજન છે!"

જાદુઈ દોરી બોલી, "જ્યારે પણ તમે વસ્તુઓને જોડો અને બધું ગણો, તેને ઉમેરો કહે છે!"

ગોલૂ અને મોલૂએ આ નવા નિયમને પસંદ કર્યું. આખો દિવસ, તેઓ મેળામાં ફરતા જાદુઈ દોરીથી વસ્તુઓને ઉમેરી અને ગણતા રહ્યા—ગબ્બરો, બોલ અને ક્યારેક રમકડાં!

દિવસના અંતે તેમને સમજાયું કે ઉમેરા નો અર્થ છે બે કે વધુ જૂથોને જોડીને તેમની કુલ સંખ્યા ગણવી.

તત્ત્વ: ગોલૂ અને મોલૂએ શીખ્યું કે ઉમેરો સરળ છે અને ગણિત મજેદાર અને જાદુઈ હોઈ શકે છે!
"""
        }
    },
    {
        "id": 2,
        "subject": "Science",
        "title": {
            "english": "Photosynthesis: Dewy's Journey",
            "hindi": "प्रकाश संश्लेषण: ड्यूवी की यात्रा",
            "gujarati": "ફોટોસિન્થેસિસ: ડ્યુવીની મુસાફરી"
        },
        "content": {
            "english": """
🌱 Detailed Summary of Photosynthesis

Photosynthesis is the process by which green plants, algae, and some bacteria prepare their own food. It mainly takes place in the leaves, which contain a green pigment called chlorophyll. Chlorophyll helps to capture sunlight, which provides the energy required for the process.

In photosynthesis, plants take in carbon dioxide from the air through small pores in the leaves called stomata, and they absorb water from the soil through their roots. Using sunlight as energy, these raw materials are converted into glucose, a simple sugar that plants use as food for growth, energy, and storage. During this process, plants also release oxygen into the atmosphere as a by-product, which is essential for animals and humans to survive.

The overall chemical reaction of photosynthesis is:

6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂

Photosynthesis is vital for life on Earth because it is the main source of oxygen in the atmosphere and forms the base of the food chain. Without it, living beings would not get the oxygen they need to breathe or the food energy required to live.
""",
            "hindi": """
🌱 प्रकाश संश्लेषण का विस्तृत सारांश

प्रकाश संश्लेषण वह प्रक्रिया है जिसके द्वारा हरे पौधे, शैवाल और कुछ बैक्टीरिया अपना भोजन तैयार करते हैं। यह मुख्य रूप से पत्तियों में होता है, जिनमें क्लोरोफिल नामक हरा रंग होता है। क्लोโรफिल सूर्य की रोशनी को पकड़ने में मदद करता है, जो प्रक्रिया के लिए आवश्यक ऊर्जा प्रदान करता है।

प्रकाश संश्लेषण में, पौधे हवा से कार्बन डाइऑक्साइड को पत्तियों की छोटी छिद्रों (स्टोमाटा) के माध्यम से लेते हैं, और मिट्टी से पानी अपनी जड़ों के जरिए अवशोषित करते हैं। सूर्य की रोशनी की ऊर्जा का उपयोग करके, ये कच्चे पदार्थ ग्लूकोज नामक सरल चीनी में परिवर्तित हो जाते हैं, जिसका उपयोग पौधे वृद्धि, ऊर्जा और संग्रह के लिए करते हैं। इस प्रक्रिया के दौरान, पौधे वायुमंडल में ऑक्सीजन भी छोड़ते हैं, जो जीवों के लिए आवश्यक है।

प्रकाश संश्लेषण की समग्र रासायनिक क्रिया है:
6CO₂ + 6H₂O + सूर्य की रोशनी → C₆H₁₂O₆ + 6O₂

प्रकाश संश्लेषण पृथ्वी पर जीवन के लिए महत्वपूर्ण है क्योंकि यह वायुमंडल में ऑक्सीजन का मुख्य स्रोत है और खाद्य श्रृंखला का आधार है। इसके बिना जीवों को सांस लेने के लिए ऑक्सीजन और जीवित रहने के लिए आवश्यक ऊर्जा नहीं मिलती।
""",
            "gujarati": """
🌱 ફોટોસિન્થેસિસનો વિગતવાર સારાંશ

ફોટોસિન્થેસિસ એ પ્રક્રિયા છે જેમાં લીલાં વૃક્ષો, શૈવાલ અને કેટલાક બેક્ટેરિયા પોતાનું આહાર બનાવે છે. આ મુખ્યત્વે પાનમાં થાય છે, જેમાં ક્લોરોફિલ નામનું લીલું રંગદાર પિગ્મેન્ટ હોય છે. ક્લોરોફિલ સૂર્યની રોશની પકડી છે, જે પ્રક્રિયા માટે જરૂરી ઊર્જા આપે છે.

ફોટોસિન્થેસિસમાં, છોડ હવાના નાના છિદ્રો (સ્ટોમેટા)માંથી કાર્બન ડાયોક્સાઇડ લે છે અને પાણી જમીનમાંથી તેની મૂળ દ્વારા શોષે છે. સૂર્યની રોશની energie તરીકે ઉપયોગ કરીને, આ કાચા સામગ્રી ગ્લુકોઝમાં પરિવર્તિત થાય છે, જે એક સરળ શુગર છે જે છોડ વૃદ્ધિ, ઊર્જા અને સંગ્રહ માટે ઉપયોગ કરે છે. આ પ્રક્રિયાના દ્રોણા, છોડ વાયુમંડળમાં ઓક્સિજન છોડે છે, જે પ્રાણી અને માનવજીવન માટે જરૂરી છે.

ફોટોસિન્થેસિસની સંપૂર્ણ રસાયણિક ક્રિયા છે:

6CO₂ + 6H₂O + સૂર્યપ્રકાશ → C₆H₁₂O₆ + 6O₂

ફોટોસિન્થેસિસ પૃથ્વી પર જીવન માટે મહત્વપૂર્ણ છે કારણ કે તે વાયુમંડળમાં ઓક્સિજનનો મુખ્ય સ્ત્રોત છે અને ખોરાક શ્રેણીનો આધાર છે. જેના વગર જીવનને શ્વાસ લેવા માટે ઓક્સિજન અને જીવવા માટે ઊર્જા મળતી નથી.
"""
        }
    },
    {
        "id": 3,
        "subject": "English",
        "title": {
            "english": "Three Pots",
            "hindi": "तीन बर्तन",
            "gujarati": "ત્રણ વાસણો"
        },
        "content": {
            "english": """
Murari, a boy, discovered three pots filled with gold, silver, and copper. A sage explained that the pots symbolized human life—some have great wealth, some less, some very little. But in the end, all pots are clay, just like all lives end the same way. The true treasure is not riches but virtue, knowledge, and good character.

👉 Moral: Real value lies in what we cultivate inside, not in outer wealth.
""",
            "hindi": """
translate:मुरारी, एक लड़का, तीन बर्तन ढूँढा जिनमें सोना, चाँदी और तांबा भरा था। एक साधु ने बताया कि ये बर्तन मानव जीवन का प्रतीक हैं—कुछ के पास बहुत धन है, कुछ के पास कम, कुछ के पास बहुत कम। लेकिन अंत में, सभी बर्तन मिट्टी के होते हैं, जैसे सभी जीवन का अंत एक ही तरह होता है। सच्चा खजाना धन नहीं बल्कि सदाचार, ज्ञान, और अच्छा चरित्र है।

👉 सीख: असली मूल्य वे चीजें हैं जिन्हें हम अपने अंदर विकसित करते हैं, न कि बाहरी संपत्ति में।
""",
            "gujarati": """
મુરારી, એક છોકરો, ત્રણ વાસણો શોધી શક્યો જેમાં સોનું, ચાંદી અને તાંબું ભરેલું હતું. એક સંતે સમજાવ્યો કે આ વાસણો માનવ જીવનનું પ્રતીક છે—કેટલાંક પાસે ધન વધારે છે, કેટલાક પાસે ઓછું અને કેટલાક પાસે ખૂબ ઓછું. અંતે, બધા વાસણો માટીની બનેલા હોય છે અને જીવનો અંત પણ એકસરખો જ હોય છે. સાચું ખજાનું ધન નહીં, પરંતુ નૈતિકતા, જ્ઞાન અને સારું ચલણ છે.
👉 વિચાર: સાચી કિંમત એ છે જે આપણું મન તેમજ સ્વભાવ વિકસાવે, બાહ્ય સંપત્તિ નથી.
"""
        }
    },
    {
        "id": 4,
        "subject": "Social Science",
        "title": {
            "english": "Sunrise, Sunset, and Earth’s Movement",
            "hindi": "सूर्योदय, सूर्यास्त, और पृथ्वी की गति",
            "gujarati": "સૂર્યોદય, સૂર્યાસ્ત અને પૃથ્વી નું ચલણ"
        },
        "content": {
            "english": """
The Sun seems to rise in the east, move across the sky, and set in the west. But in reality, the Sun does not move around the Earth. What actually happens is that the Earth rotates on its own axis. This rotation takes about 24 hours and is the reason we have day and night.

As the Earth spins from west to east, the part facing the Sun has daylight, and the part facing away from the Sun has night. Because of this spinning, it looks like the Sun is moving across the sky, but it is really the Earth that is changing its position.

👉 In short: The sunset is just an effect of the Earth’s rotation, not the Sun moving.
""",
            "hindi": """
सूरज पूर्व दिशा से उगता हुआ नजर आता है, आकाश के पार चलता है और पश्चिम दिशा में डूबता है। लेकिन वास्तव में सूरज पृथ्वी के आसपास नहीं घूमता। असल में पृथ्वी अपने अक्ष पर घूमती है। यह घूमना लगभग 24 घंटे का होता है और यही कारण है कि हमें दिन और रात होती है।

जैसे-जैसे पृथ्वी पश्चिम से पूर्व की ओर घूमती है, वह हिस्सा जो सूरज की ओर होता है, दिन होता है और जो सूरज से दूर होता है, रात होती है। इस घूमने की वजह से ऐसा लगता है मानो सूरज आकाश में कहीं से कहीं जा रहा हो, लेकिन असल में पृथ्वी मूवमेंट कर रही होती है।

👉 संक्षेप में: सूर्यास्त पृथ्वी के घूमने का प्रभाव है, सूरज की गति नहीं।
""",
            "gujarati": """
સૂર્ય પૂર્વ તરફ ઉગે છે, આકાશમાં ફરતું લાગે છે અને પશ્ચિમ તરફ ડૂબે છે. પરંતુ વાસ્તવમાં સૂર્ય પૃથ્વી આસપાસ ફરતું નથી. જે થાય છે તે છે કે પૃથ્વી પોતાની ધ્રુવીય ધ્રુવ પર ફરતી રહે છે. આ ફરત લાગતી લગભગ 24 કલાકની હોય છે અને એ જ કારણ છે કે આપણને દિવસ અને રાત્રિ મળે છે.

જ્યારે પૃથ્વી પશ્ચિમથી પૂર્વ તરફ ફરતી હોય છે ત્યારે તે ભાગ સૂર્ય તરફ હોય છે ત્યાં દીન હોય છે અને તે ભાગ જે સૂર્યથી દૂર હોય છે ત્યાં રાત્રિ હોય છે. આ ફરવાની ક્રિયા સૂર્યને આકાશમાં ફરતો દેખાડતી હોય છે, પરંતુ વાસ્તવમાં પૃથ્વી પોતાનું સ્થાન બદલતી રહે છે.

👉 સંક્ષિપ્તમાં: સૂર્યાસ્ત માત્ર પૃથ્વી ની ફરવાની ક્રિયાનો પ્રભાવ છે, સૂર્યની ચળવળ નહીં.
"""
        }
    }
]
def get_lesson_by_id(lesson_id):
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if lesson:
        lang = session.get('language', 'english')
        return {
            "id": lesson['id'],
            "subject": lesson['subject'],
            "title": lesson['title'].get(lang, lesson['title']['english']),
            "content": lesson['content'].get(lang, lesson['content']['english'])
        }
    return None
def get_lesson_by_subject(subject):
    return [lesson for lesson in lessons if lesson["subject"].lower()==subject.lower()]

