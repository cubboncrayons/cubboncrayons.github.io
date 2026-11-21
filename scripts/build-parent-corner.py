from pathlib import Path
import html,json,argparse
ROOT=Path(__file__).parent
parser=argparse.ArgumentParser(description='Build the four Parent Corner pages; use --output . from the repository root.')
parser.add_argument('--output',type=Path,default=ROOT/'site')
args=parser.parse_args()
OUT=args.output
OUT.mkdir(exist_ok=True,parents=True)
URL='https://cubboncrayons.github.io'
SOURCES=[
 ('Anna Freud — Sharing','https://www.annafreud.org/resources/under-fives-wellbeing/common-difficulties/sharing/'),
 ('Raising Children Network — Teaching children to share','https://raisingchildren.net.au/toddlers/behaviour/friends-siblings/sharing'),
 ('PBS KIDS for Parents — Encouraging children to share and take turns','https://www.pbs.org/parents/thrive/encouraging-children-to-share-and-take-turns')
]
DATA={
 'en':{
  'hub':'parent-corner.html','article':'parent-corner/sharing-a-favourite-toy.html','otherhub':'parent-corner-kannada.html','otherarticle':'parent-corner/sharing-a-favourite-toy-kn.html',
  'corner':'Parent Corner','stories':'Stories','about':'Our story','skip':'Skip to the article','series':'REAL PARENTING MOMENTS',
  'heading':'A little reassurance.<br>A practical next step.',
  'intro':'For the moments that leave you wondering what to say. Thoughtfully researched reading for parents of children aged 2–5, in English and Kannada.',
  'cardtitle':'When a favourite toy is hard to share',
  'artcaption':'Original artwork from An Idli for Meera',
  'artalt':'Appi and Meera sharing an idli together beneath a tree',
  'jumpphrases':'Find words to try',
  'title':'My child won’t share a favourite toy. Am I getting this wrong?',
  'deck':'When a small disagreement starts to feel like a judgement on your parenting, it helps to pause and look at the moment differently.',
  'topic':'Sharing & visiting family','age':'Ages 2–5','read':'Read the answer','latest':'START WITH THIS QUESTION',
  'promise':'A calm place to think things through.',
  'promisebody':'Each article begins with a specific parenting moment, offers manageable options and shows its sources. No perfect-parent promises. No medical advice.',
  'pilottag':'First article · Editorial pilot','byline':'By Cubbon Crayons','date':'Sources checked 21 November 2026',
  'notice':'Illustrative situation, not a reader submission. Original editorial guidance informed by the sources below; not an individual assessment.',
  'opening':'You wanted a happy visit with the cousins. Instead, your child is holding tightly to one toy, someone is waiting, and you can feel the room watching. It can leave you wondering whether this says something about your parenting. You can help with the disagreement without turning it into a judgement about either of you.',
  'quickheading':'First, take the pressure down',
  'quick':'You can respect a treasured toy and still help your child practise taking turns. Before the next visit, choose together what to put away and what to make available. During a disagreement, stay nearby and help both children find a way forward. [1, 2]',
  'toc':'In this answer','understand':'One moment is not the whole story',
  'understandbody':'A two-year-old and a five-year-old may need different help. Younger toddlers often struggle to wait; preschoolers can understand more and still find a turn difficult. Adjust your expectations to the child and the situation, rather than treating one visit as a test of kindness. [1, 2]',
  'stepsheading':'Make the next visit a little easier',
  'steps':[
   ('Before guests arrive','Invite your child to choose a few toys for playing together. Keep a particularly precious toy somewhere safe for the visit. [2, 3]'),
   ('When both children want it','Name the difficulty briefly. Help arrange a next turn or offer another activity while they wait. Step in to stop grabbing or hurting. [1, 2]'),
   ('After everyone settles','Practise an exchange during ordinary play, with something neither child is worried about losing. Notice an offered turn without comparing the children. [1, 2]')],
  'wordsheading':'Words you could try','wordsintro':'You don’t need a perfect speech. Start gently, with one short sentence.',
  'phrases':['“Shall we choose something you both want to play with?”','“You’re using this. Let’s work out the next turn together.”'],
  'relativeheading':'And if a relative comments?',
  'relativebody':'You do not have to explain your whole approach while the children are upset. You could say: “I’ll help them with this. We can talk afterwards.” This is an example response, not a rule for every family.',
  'againheading':'If it is still difficult',
  'againbody':'Try a shorter visit or a different activity. If disagreements repeatedly become unsafe or feel unmanageable, ask a qualified professional for guidance suited to your family. There is no need to label your child from this article.',
  'sourceheading':'What informed this answer','sourcenote':'The sources support the age context and practical options. The opening, illustrative situation and sample phrases were written for Cubbon Crayons. This article has not received independent specialist review.',
  'relatedheading':'Explore sharing through a story','relatedbody':'An Idli for Meera offers a different everyday moment of sharing. Read, talk and trace together if it suits your family. Buying a book is optional and does not promise a change in behaviour.',
  'storytitle':'An Idli for Meera','storyalt':'Original An Idli for Meera book cover','preview':'See the story preview','price':'₹49 · Kannada + English · Printable PDF',
  'questionheading':'What would you like us to explore next?',
  'questionbody':'You can suggest an everyday, non-medical parenting topic through our contact page. Please leave out children’s names, photos and private details. Suggestions help choose future articles; individual replies are not promised.',
  'suggest':'Suggest a future topic','back':'Back to Parent Corner','footer':'Little stories. Everyday kindness.',
  'privacy':'Privacy','support':'Contact','sourceslink':'Sources','articlelink':'Read our first article'
 },
 'kn':{
  'hub':'parent-corner-kannada.html','article':'parent-corner/sharing-a-favourite-toy-kn.html','otherhub':'parent-corner.html','otherarticle':'parent-corner/sharing-a-favourite-toy.html',
  'corner':'ಪೋಷಕರಿಗಾಗಿ','stories':'ಕಥೆಗಳು','about':'ನಮ್ಮ ಬಗ್ಗೆ','skip':'ಲೇಖನಕ್ಕೆ ಹೋಗಿ','series':'ಪೋಷಕರ ದಿನನಿತ್ಯದ ಅನುಭವಗಳು',
  'heading':'ಸ್ವಲ್ಪ ಸಮಾಧಾನ.<br>ಮುಂದಿನ ಹೆಜ್ಜೆಗೆ ನೆರವು.',
  'intro':'ಮಕ್ಕಳ ಜೊತೆ ಏನು ಮಾತನಾಡಬೇಕು ಎಂದು ತೋಚದ ಕ್ಷಣಗಳಿಗಾಗಿ. 2–5 ವರ್ಷದ ಮಕ್ಕಳ ಪೋಷಕರಿಗೆ, ವಿಶ್ವಾಸಾರ್ಹ ಮೂಲಗಳ ಆಧಾರದ ಮೇಲೆ ಬರೆದ ಲೇಖನಗಳು. ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ.',
  'cardtitle':'ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಹಂಚಿಕೊಳ್ಳುವುದು ಕಷ್ಟವಾದಾಗ',
  'artcaption':'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ ಕಥೆಯ ಮೂಲ ಚಿತ್ರ',
  'artalt':'ಮರದ ಕೆಳಗೆ ಜೊತೆಯಾಗಿ ಇಡ್ಲಿ ಹಂಚಿಕೊಳ್ಳುತ್ತಿರುವ ಅಪ್ಪಿ ಮತ್ತು ಮೀರಾ',
  'jumpphrases':'ಹೇಳಬಹುದಾದ ಮಾತುಗಳನ್ನು ನೋಡಿ',
  'title':'ನನ್ನ ಮಗು ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಬೇರೆಯವರಿಗೆ ಕೊಡುತ್ತಿಲ್ಲ. ನಾನು ತಪ್ಪು ಮಾಡುತ್ತಿದ್ದೇನೆಯೇ?',
  'deck':'ಮಕ್ಕಳ ನಡುವಿನ ಸಣ್ಣ ಜಗಳವೂ ನಮ್ಮನ್ನು ಒಳ್ಳೆಯ ಪೋಷಕರೇ ಎಂದು ಪ್ರಶ್ನಿಸಿಕೊಳ್ಳುವಂತೆ ಮಾಡಬಹುದು. ಸ್ವಲ್ಪ ನಿಂತು, ಆ ಕ್ಷಣವನ್ನು ಬೇರೆ ರೀತಿಯಲ್ಲಿ ನೋಡೋಣ.',
  'topic':'ಆಟಿಕೆಗಳು ಮತ್ತು ಮನೆಯ ಅತಿಥಿಗಳು','age':'2–5 ವರ್ಷ','read':'ಉತ್ತರ ಓದಿ','latest':'ಈ ಪ್ರಶ್ನೆಯಿಂದ ಆರಂಭಿಸೋಣ',
  'promise':'ನೆಮ್ಮದಿಯಾಗಿ ಯೋಚಿಸಲು ಒಂದು ಜಾಗ.',
  'promisebody':'ಪ್ರತಿ ಲೇಖನದಲ್ಲೂ ದಿನನಿತ್ಯದ ಒಂದು ಸಂದರ್ಭ, ಪ್ರಯತ್ನಿಸಬಹುದಾದ ಸರಳ ಸಲಹೆಗಳು ಮತ್ತು ಬಳಸಿದ ಮೂಲಗಳು ಇರುತ್ತವೆ. ಪರಿಪೂರ್ಣ ಪೋಷಕರಾಗಬೇಕೆಂಬ ಒತ್ತಡವಿಲ್ಲ. ವೈದ್ಯಕೀಯ ಸಲಹೆಗಳಿಲ್ಲ.',
  'pilottag':'ಮೊದಲ ಲೇಖನ · ಪ್ರಾಯೋಗಿಕ ಪ್ರಕಟಣೆ','byline':'ಕಬ್ಬನ್ ಕ್ರೇಯಾನ್ಸ್ ಬರಹ','date':'ಮೂಲಗಳನ್ನು ಪರಿಶೀಲಿಸಿದ ದಿನ: 21 ನವೆಂಬರ್ 2026',
  'notice':'ಇದು ಉದಾಹರಣೆಗೆ ಬರೆದ ಸಂದರ್ಭ; ಓದುಗರು ಕಳುಹಿಸಿದ ನೈಜ ಘಟನೆಯಲ್ಲ. ಕೆಳಗಿನ ಮೂಲಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ವತಂತ್ರವಾಗಿ ಬರೆದ ಸಾಮಾನ್ಯ ಮಾರ್ಗದರ್ಶನ; ವೈಯಕ್ತಿಕ ಮೌಲ್ಯಮಾಪನವಲ್ಲ.',
  'opening':'ಮನೆಗೆ ಬಂದ ಮಕ್ಕಳ ಜೊತೆ ನಿಮ್ಮ ಮಗು ಖುಷಿಯಾಗಿ ಆಡಲಿ ಎಂದುಕೊಂಡಿದ್ದಿರಿ. ಆದರೆ ಈಗ ಅದು ಒಂದು ಆಟಿಕೆಯನ್ನು ಬಿಗಿಯಾಗಿ ಹಿಡಿದುಕೊಂಡಿದೆ. ಇನ್ನೊಂದು ಮಗು ಕಾಯುತ್ತಿದೆ. ಎಲ್ಲರೂ ನೋಡುತ್ತಿದ್ದಾರೆ ಎನ್ನಿಸಬಹುದು. “ನಾನು ಏನಾದರೂ ತಪ್ಪು ಮಾಡುತ್ತಿದ್ದೇನೆಯೇ?” ಎಂಬ ಪ್ರಶ್ನೆಯೂ ಬರಬಹುದು. ನಿಮ್ಮನ್ನಾಗಲಿ, ಮಗುವನ್ನಾಗಲಿ ದೂಷಿಸದೆ ಈ ಸಂದರ್ಭವನ್ನು ನಿಭಾಯಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು.',
  'quickheading':'ಮೊದಲು, ಸ್ವಲ್ಪ ಒತ್ತಡ ಕಡಿಮೆ ಮಾಡೋಣ',
  'quick':'ಮಗುವಿನ ಇಷ್ಟದ ಆಟಿಕೆಗೆ ಮಹತ್ವ ಕೊಡುವುದರ ಜೊತೆಗೆ, ಸರದಿಯಲ್ಲಿ ಆಡುವುದನ್ನೂ ಕಲಿಸಬಹುದು. ಮುಂದಿನ ಬಾರಿ ಅತಿಥಿಗಳು ಬರುವ ಮೊದಲು, ಯಾವ ಆಟಿಕೆಗಳನ್ನು ತೆಗೆದಿಡಬೇಕು, ಯಾವುದನ್ನು ಎಲ್ಲರೂ ಆಡಲು ಇಡಬೇಕು ಎಂದು ಜೊತೆಯಾಗಿ ಆಯ್ಕೆ ಮಾಡಿ. ಜಗಳವಾದಾಗ ಹತ್ತಿರವಿದ್ದು ಎರಡೂ ಮಕ್ಕಳಿಗೆ ಸಹಾಯ ಮಾಡಿ. [1, 2]',
  'toc':'ಈ ಲೇಖನದಲ್ಲಿ','understand':'ಒಂದು ಸಂದರ್ಭವೇ ಮಗುವಿನ ಸಂಪೂರ್ಣ ಪರಿಚಯವಲ್ಲ',
  'understandbody':'ಎರಡು ವರ್ಷದ ಮಗುವಿಗೂ ಐದು ವರ್ಷದ ಮಗುವಿಗೂ ಬೇಕಾಗುವ ಸಹಾಯ ಒಂದೇ ಆಗಿರುವುದಿಲ್ಲ. ಚಿಕ್ಕ ಮಕ್ಕಳಿಗೆ ಕಾಯುವುದು ಕಷ್ಟವಾಗಬಹುದು. ಸ್ವಲ್ಪ ದೊಡ್ಡ ಮಕ್ಕಳಿಗೆ ಸರದಿಯ ಅರ್ಥ ತಿಳಿದಿದ್ದರೂ, ಕಾಯುವುದು ಸುಲಭವಲ್ಲ. ಮಗುವಿನ ವಯಸ್ಸು ಮತ್ತು ಸಂದರ್ಭಕ್ಕೆ ತಕ್ಕಂತೆ ನಿರೀಕ್ಷೆ ಇಟ್ಟುಕೊಳ್ಳಿ. ಒಂದು ಭೇಟಿಯನ್ನೇ ಮಗುವಿನ ಒಳ್ಳೆಯತನದ ಪರೀಕ್ಷೆಯಾಗಿ ನೋಡಬೇಡಿ. [1, 2]',
  'stepsheading':'ಮುಂದಿನ ಭೇಟಿಯನ್ನು ಸ್ವಲ್ಪ ಸುಲಭ ಮಾಡೋಣ',
  'steps':[
   ('ಅತಿಥಿಗಳು ಬರುವ ಮೊದಲು','ಎಲ್ಲರೂ ಸೇರಿ ಆಡಲು ಕೆಲವು ಆಟಿಕೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಲು ಮಗುವನ್ನು ಕರೆಯಿರಿ. ತುಂಬಾ ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಆ ಭೇಟಿಯ ಸಮಯದಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ತೆಗೆದಿಡಬಹುದು. [2]'),
   ('ಎರಡೂ ಮಕ್ಕಳಿಗೆ ಒಂದೇ ಆಟಿಕೆ ಬೇಕಾದಾಗ','ಏನಾಗಿದೆ ಎಂದು ಚಿಕ್ಕದಾಗಿ ಹೇಳಿ. ಮುಂದಿನ ಸರದಿಯನ್ನು ಹೊಂದಿಸಲು ಸಹಾಯ ಮಾಡಿ ಅಥವಾ ಕಾಯುವಾಗ ಬೇರೊಂದು ಆಟ ಸೂಚಿಸಿ. ಕಸಿದುಕೊಳ್ಳುವುದನ್ನು ಅಥವಾ ನೋಯಿಸುವುದನ್ನು ತಡೆಯಿರಿ. [1, 2]'),
   ('ಎಲ್ಲರೂ ಶಾಂತವಾದ ಮೇಲೆ','ಕಳೆದುಕೊಳ್ಳುವ ಭಯವಿಲ್ಲದ ಸಾಮಾನ್ಯ ಆಟಿಕೆಯಿಂದ ಸರದಿಯಲ್ಲಿ ಆಡುವುದನ್ನು ಅಭ್ಯಾಸ ಮಾಡಿ. ಒಂದು ಮಗು ಇನ್ನೊಂದಕ್ಕೆ ಸರದಿ ಕೊಟ್ಟಾಗ ಗಮನಿಸಿ ಮೆಚ್ಚಿ; ಮಕ್ಕಳನ್ನು ಹೋಲಿಸಬೇಡಿ. [1, 2]')],
  'wordsheading':'ಹೀಗೆ ಹೇಳಿ ನೋಡಬಹುದು','wordsintro':'ಎಲ್ಲವನ್ನೂ ಒಮ್ಮೆಲೇ ವಿವರಿಸಬೇಕಿಲ್ಲ. ಮೃದುವಾಗಿ, ಒಂದು ಚಿಕ್ಕ ಮಾತಿನಿಂದ ಆರಂಭಿಸಿ.',
  'phrases':['“ನೀವಿಬ್ಬರೂ ಸೇರಿ ಆಡಲು ಏನಾದರೂ ಆಯ್ಕೆ ಮಾಡೋಣವಾ?”','“ಈಗ ನೀನು ಇದರಿಂದ ಆಡುತ್ತಿದ್ದೀಯ. ಮುಂದಿನ ಸರದಿಯನ್ನು ಜೊತೆಯಾಗಿ ನಿರ್ಧರಿಸೋಣ.”'],
  'relativeheading':'ಸಂಬಂಧಿಕರು ಏನಾದರೂ ಹೇಳಿದರೆ?',
  'relativebody':'ಮಕ್ಕಳು ಬೇಸರಗೊಂಡಿರುವಾಗಲೇ ನಿಮ್ಮ ಅಭಿಪ್ರಾಯವನ್ನೆಲ್ಲ ವಿವರಿಸಬೇಕಿಲ್ಲ. “ನಾನು ಮಕ್ಕಳಿಗೆ ಸಹಾಯ ಮಾಡುತ್ತೇನೆ. ಆಮೇಲೆ ಮಾತನಾಡೋಣ” ಎಂದು ಹೇಳಬಹುದು. ಇದು ಒಂದು ಉದಾಹರಣೆ ಮಾತ್ರ; ಪ್ರತಿಯೊಂದು ಕುಟುಂಬಕ್ಕೂ ಒಂದೇ ನಿಯಮವಲ್ಲ.',
  'againheading':'ಇನ್ನೂ ಕಷ್ಟವಾಗುತ್ತಿದ್ದರೆ',
  'againbody':'ಭೇಟಿಯ ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡಿ ನೋಡಿ ಅಥವಾ ಬೇರೆ ಆಟ ಆಯ್ಕೆ ಮಾಡಿ. ಜಗಳಗಳು ಪದೇಪದೇ ಅಪಾಯಕಾರಿಯಾಗುತ್ತಿದ್ದರೆ ಅಥವಾ ನಿಭಾಯಿಸಲು ತುಂಬಾ ಕಷ್ಟವಾಗುತ್ತಿದ್ದರೆ, ನಿಮ್ಮ ಕುಟುಂಬಕ್ಕೆ ತಕ್ಕ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಅರ್ಹ ತಜ್ಞರ ಸಹಾಯ ಕೇಳಿ. ಈ ಲೇಖನದ ಆಧಾರದ ಮೇಲೆ ಮಗುವಿಗೆ ಹಣೆಪಟ್ಟಿ ಹಚ್ಚಬೇಕಿಲ್ಲ.',
  'sourceheading':'ಈ ಉತ್ತರಕ್ಕೆ ಬಳಸಿದ ಮೂಲಗಳು','sourcenote':'ವಯಸ್ಸಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿವರಣೆ ಮತ್ತು ಪ್ರಯತ್ನಿಸಬಹುದಾದ ಸಲಹೆಗಳಿಗೆ ಈ ಮೂಲಗಳನ್ನು ಬಳಸಲಾಗಿದೆ. ಆರಂಭದ ಬರಹ, ಉದಾಹರಣೆಯ ಸಂದರ್ಭ ಮತ್ತು ಮಾತುಗಳನ್ನು ಕಬ್ಬನ್ ಕ್ರೇಯಾನ್ಸ್‌ಗಾಗಿ ಸ್ವತಂತ್ರವಾಗಿ ಬರೆಯಲಾಗಿದೆ. ಈ ಲೇಖನವನ್ನು ಸ್ವತಂತ್ರ ತಜ್ಞರು ಪರಿಶೀಲಿಸಿಲ್ಲ.',
  'relatedheading':'ಒಂದು ಕಥೆಯ ಮೂಲಕ ಹಂಚಿಕೊಳ್ಳುವ ಬಗ್ಗೆ ಮಾತನಾಡೋಣ','relatedbody':'“ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ” ಕಥೆಯಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳುವ ಇನ್ನೊಂದು ದಿನನಿತ್ಯದ ಸಂದರ್ಭವಿದೆ. ನಿಮ್ಮ ಕುಟುಂಬಕ್ಕೆ ಹೊಂದಿದರೆ, ಜೊತೆಯಾಗಿ ಓದಿ, ಮಾತನಾಡಿ, ಚಟುವಟಿಕೆ ಮಾಡಿ. ಪುಸ್ತಕ ಕೊಳ್ಳುವುದು ನಿಮ್ಮ ಆಯ್ಕೆ; ಅದರಿಂದ ಮಗುವಿನ ನಡವಳಿಕೆ ಬದಲಾಗುತ್ತದೆ ಎಂಬ ಭರವಸೆ ಇಲ್ಲ.',
  'storytitle':'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ','storyalt':'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ ಪುಸ್ತಕದ ಮೂಲ ಮುಖಪುಟ','preview':'ಕಥೆಯ ಮಾದರಿ ಪುಟಗಳನ್ನು ನೋಡಿ','price':'₹49 · ಕನ್ನಡ + ಇಂಗ್ಲಿಷ್ · ಮುದ್ರಿಸಬಹುದಾದ ಪಿಡಿಎಫ್',
  'questionheading':'ಮುಂದೆ ಯಾವ ವಿಷಯದ ಬಗ್ಗೆ ಓದಲು ಇಷ್ಟಪಡುತ್ತೀರಿ?',
  'questionbody':'ದಿನನಿತ್ಯದ, ಮಕ್ಕಳನ್ನು ಬೆಳೆಸುವಾಗ ಎದುರಾಗುವ, ವೈದ್ಯಕೀಯವಲ್ಲದ ವಿಷಯವನ್ನು ನಮ್ಮ ಸಂಪರ್ಕ ಪುಟದಲ್ಲಿ ಸೂಚಿಸಬಹುದು. ಮಕ್ಕಳ ಹೆಸರುಗಳು, ಫೋಟೋಗಳು ಮತ್ತು ಖಾಸಗಿ ವಿವರಗಳನ್ನು ಸೇರಿಸಬೇಡಿ. ಸಲಹೆಗಳು ಮುಂದಿನ ಲೇಖನಗಳ ಆಯ್ಕೆಗೆ ಸಹಾಯ ಮಾಡುತ್ತವೆ; ವೈಯಕ್ತಿಕ ಉತ್ತರದ ಭರವಸೆ ಇಲ್ಲ.',
  'suggest':'ಮುಂದಿನ ವಿಷಯ ಸೂಚಿಸಿ','back':'ಪೋಷಕರ ಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ','footer':'ಪುಟ್ಟ ಕಥೆಗಳು. ದಿನನಿತ್ಯದ ಕಾಳಜಿ.',
  'privacy':'ಗೌಪ್ಯತೆ','support':'ಸಂಪರ್ಕ','sourceslink':'ಮೂಲಗಳು','articlelink':'ನಮ್ಮ ಮೊದಲ ಲೇಖನ ಓದಿ'
 }
}
def esc(x):return html.escape(x,quote=True)
def langlinks(d,kind,lang):
 other=d['other'+kind]
 paths={'en':d[kind] if lang=='en' else other,'kn':d[kind] if lang=='kn' else other}
 return '<nav class="language-choice" aria-label="Reading language">'+''.join(f'<a href="/{paths[k]}" lang="{k}" hreflang="{k}" data-reading-language="{k}"'+(' aria-current="page"' if k==lang else '')+'>'+label+'</a>' for k,label in [('en','English'),('kn','ಕನ್ನಡ')])+'</nav>'
def shell(lang,kind,body):
 d=DATA[lang];path=d[kind];other=d['other'+kind];title=d['corner'] if kind=='hub' else d['title']
 alternates=langlinks(d,kind,lang)
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self' data:; style-src 'self'; script-src 'self'; font-src 'self'; base-uri 'none'; form-action 'none'"><meta name="theme-color" content="#fcf9f1"><title>{esc(title)} · Cubbon Crayons</title><meta name="description" content="{esc(d['deck'] if kind=='article' else d['intro'])}"><link rel="canonical" href="{URL}/{path}"><link rel="alternate" hreflang="{lang}" href="{URL}/{path}"><link rel="alternate" hreflang="{'kn' if lang=='en' else 'en'}" href="{URL}/{other}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(d['deck'])}"><meta property="og:url" content="{URL}/{path}"><meta property="og:type" content="{'article' if kind=='article' else 'website'}"><link rel="stylesheet" href="/styles.css?v=20261121-larger-covers"><link rel="stylesheet" href="/parent-corner.css?v=20261121-refined"><script src="/parent-corner.js?v=20261121-refined" defer></script></head><body class="home editorial"><a class="skip-link" href="#reading">{d['skip']}</a><header class="site-header wrap"><a class="brand" href="/"><span class="mark" aria-hidden="true">c<span>.</span></span>Cubbon Crayons</a><nav aria-label="Main navigation"><a href="/#stories">{d['stories']}</a><a href="/{d['hub']}" aria-current="page">{d['corner']}</a><a href="/#our-story">{d['about']}</a></nav></header><main id="reading" class="editorial-main wrap"><div class="editorial-topline"><a class="breadcrumb" href="/{d['hub']}">{d['corner']}</a>{alternates}</div>{body}</main><footer class="site-footer wrap"><span>© 2026 Cubbon Crayons</span><nav aria-label="Footer"><a href="/privacy.html">{d['privacy']}</a><a href="https://payhip.com/CubbonCrayons/contact" rel="noreferrer">{d['support']}</a></nav></footer></body></html>'''
def hub(lang):
 d=DATA[lang]
 body=f'''<section class="editorial-hero"><p class="eyebrow">{d['series']}</p><h1>{d['heading']}</h1><p class="editorial-deck">{d['intro']}</p></section><section class="first-read" aria-labelledby="first-title"><figure class="feature-art"><img src="/assets/parent-corner-sharing.webp" width="744" height="990" alt="{d['artalt']}" fetchpriority="high"><figcaption>{d['artcaption']}</figcaption></figure><div class="first-read-copy"><p class="eyebrow">{d['latest']}</p><p class="article-meta">{d['topic']} · {d['age']}</p><h2 id="first-title"><a href="/{d['article']}">{d['cardtitle']}</a></h2><p>{d['deck']}</p><a class="button" href="/{d['article']}">{d['read']}</a><p class="pilot-note">{d['pilottag']}</p></div></section><section class="editorial-promise"><h2>{d['promise']}</h2><p>{d['promisebody']}</p></section>'''
 return shell(lang,'hub',body)
def article(lang):
 d=DATA[lang];ids=[('understand',d['understand']),('try',d['stepsheading']),('words',d['wordsheading']),('sources',d['sourceheading'])]
 toc=''.join(f'<li><a href="#{key}">{title}</a></li>' for key,title in ids)
 steps=''.join(f'<li><h3>{title}</h3><p>{copy}</p></li>' for title,copy in d['steps'])
 phrases=''.join(f'<p class="say-line">{p}</p>' for p in d['phrases'])
 sources=''.join(f'<li><a href="{url}" rel="noreferrer">{name}</a></li>' for name,url in SOURCES)
 body=f'''<article><header class="article-header"><p class="eyebrow">{d['series']}</p><p class="article-meta">{d['topic']} · {d['age']}</p><h1>{d['title']}</h1><p class="editorial-deck">{d['deck']}</p><p class="article-meta">{d['byline']} · <time datetime="2026-11-21">{d['date']}</time></p><p class="pilot-note">{d['pilottag']}</p></header><div class="article-layout"><aside class="reading-toc"><details><summary>{d['toc']}</summary><ul>{toc}</ul></details></aside><div class="article-prose"><p class="opening">{d['opening']}</p><section class="quick-answer"><h2>{d['quickheading']}</h2><p>{d['quick']}</p><a class="phrase-jump" href="#words">{d['jumpphrases']}</a></section><section id="understand"><h2>{d['understand']}</h2><p>{d['understandbody']}</p></section><section id="try"><h2>{d['stepsheading']}</h2><ul class="practical-options">{steps}</ul></section><section id="words" class="words-panel" aria-labelledby="words-title"><p class="eyebrow">{'A LITTLE HELP WITH THE WORDS' if lang=='en' else 'ಮಾತುಗಳಿಗೆ ಒಂದು ಪುಟ್ಟ ನೆರವು'}</p><h2 id="words-title">{d['wordsheading']}</h2><p>{d['wordsintro']}</p>{phrases}</section><section><h2>{d['relativeheading']}</h2><p>{d['relativebody']}</p></section><section><h2>{d['againheading']}</h2><p>{d['againbody']}</p></section><section id="sources" class="article-sources"><h2>{d['sourceheading']}</h2><ol>{sources}</ol><p>{d['sourcenote']}</p><p class="scenario-note">{d['notice']}</p></section><aside class="related-story" aria-labelledby="related-title"><img src="/assets/previews/idli-cover-small.webp" alt="{d['storyalt']}" width="780" height="1103" loading="lazy"><div><p class="eyebrow">{'OPTIONAL STORY COMPANION' if lang=='en' else 'ಓದಲು ಒಂದು ಸಂಬಂಧಿತ ಕಥೆ'}</p><h2 id="related-title">{d['relatedheading']}</h2><p>{d['relatedbody']}</p><p><strong>{d['storytitle']}</strong><br>{d['price']}</p><a class="text-link" href="/?preview=idli#previews" data-parent-story="idli">{d['preview']}</a></div></aside><section class="suggest-topic"><h2>{d['questionheading']}</h2><p>{d['questionbody']}</p><a class="text-link" href="https://payhip.com/CubbonCrayons/contact" rel="noreferrer">{d['suggest']}</a></section><a class="back-link" href="/{d['hub']}">{d['back']}</a></div></div></article>'''
 return shell(lang,'article',body)
for lang in DATA:
 for kind,fn in [('hub',hub),('article',article)]:
  path=OUT/DATA[lang][kind];path.parent.mkdir(exist_ok=True,parents=True);path.write_text(fn(lang),encoding='utf8')
(ROOT/'article-content.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf8')
print('Built four bilingual pages, one original article.')
