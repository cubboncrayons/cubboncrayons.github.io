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
DATA={'en': {'hub': 'parent-corner.html',
        'article': 'parent-corner/sharing-a-favourite-toy.html',
        'otherhub': 'parent-corner-kannada.html',
        'otherarticle': 'parent-corner/sharing-a-favourite-toy-kn.html',
        'corner': 'Parent Corner',
        'stories': 'Stories',
        'about': 'Our story',
        'skip': 'Skip to the article',
        'series': 'REAL PARENTING MOMENTS',
        'heading': 'A little reassurance.<br>A practical next step.',
        'intro': 'For the moments when you’re not sure what to say. Reassurance and small, practical steps for parents '
                 'of children aged 2–5, in English and Kannada.',
        'cardtitle': 'My child won’t share a favourite toy. Am I getting this wrong?',
        'artcaption': 'Original artwork from An Idli for Meera',
        'artalt': 'Appi and Meera sharing an idli together beneath a tree',
        'jumpphrases': 'Find words to try',
        'title': 'My child won’t share a favourite toy. Am I getting this wrong?',
        'deck': 'One toy, two children—and that uncomfortable feeling that everyone is watching. Let’s make the next '
                'moment a little easier.',
        'topic': 'Sharing & visiting family',
        'age': 'Ages 2–5',
        'read': 'Read the answer',
        'latest': 'START WITH THIS QUESTION',
        'promise': 'A calm place to think things through.',
        'promisebody': 'An everyday parenting moment, a little room to breathe and something you can try. Each answer '
                       'includes the sources behind its guidance.',
        'pilottag': 'First article · Editorial pilot',
        'byline': 'By Cubbon Crayons',
        'date': 'Sources checked 21 November 2026',
        'notice': 'The opening is an illustrative situation, not a reader submission. The guidance is general rather '
                  'than an assessment of a particular child.',
        'opening': 'You hoped the cousins would have a lovely time together. Now your child is holding tightly to one '
                   'toy, another child is waiting, and you’re wondering what everyone thinks. It can be an awkward '
                   'moment. It doesn’t have to become a judgement on you or your child.',
        'quickheading': 'You don’t have to solve it all today',
        'quick': 'Your child can practise taking turns without having to hand over every treasured toy. Put a special '
                 'toy away before a visit and choose some others to play with together. If an argument starts, stay '
                 'nearby and help. You don’t have to teach it all in one afternoon. [1, 2]',
        'toc': 'In this answer',
        'understand': 'Waiting can still be hard',
        'understandbody': 'A two-year-old and a five-year-old may need different help. Younger toddlers often find '
                          'waiting hard. Preschoolers may understand taking turns and still struggle when it is their '
                          'favourite toy. Start with the help your child needs in this moment; one difficult visit is '
                          'not a test of kindness. [1, 2]',
        'stepsheading': 'Try this at the next visit',
        'steps': [('Before everyone arrives',
                   'Ask your child to help choose a few toys for playing together. Put a particularly precious toy '
                   'somewhere safe for the visit. This gives you something to agree on before anyone is waiting. [2, '
                   '3]'),
                  ('When they both want the same toy',
                   'Keep it short: both children want the same thing. Help arrange the next turn, or offer something '
                   'else to do while waiting. Step in to stop grabbing or hurting. [1, 2]'),
                  ('Later, when things are calm',
                   'Try taking turns during ordinary play, with something your child is less worried about handing '
                   'over. When they offer a turn, notice it warmly, without comparing them with another child. [1, '
                   '2]')],
        'wordsheading': 'Words you could try',
        'wordsintro': 'You don’t need a perfect speech. One gentle sentence is a place to start.',
        'phrases': ['“Shall we find something you can both play with?”',
                    '“You’re still playing with this. Let’s work out who has the next turn.”'],
        'relativeheading': 'And if a relative says something?',
        'relativebody': 'That can make an already awkward moment feel harder. You can keep your reply short: “I’ll '
                        'help them. Let’s give them a little time.” You can talk more later, when the children are '
                        'settled.',
        'againheading': 'And if the next visit is difficult too?',
        'againbody': 'You can try a shorter visit or a different activity. If disagreements repeatedly become unsafe '
                     'or feel too hard to manage, ask a qualified professional for guidance suited to your family.',
        'sourceheading': 'What informed this answer',
        'sourcenote': 'These sources inform the age context and practical suggestions. The wording, illustrative '
                      'situation and example phrases are original Cubbon Crayons writing. This article has not had '
                      'independent specialist review.',
        'relatedheading': 'Keep the conversation going with a story',
        'relatedbody': 'If a story is an easier way to begin, An Idli for Meera explores sharing through another '
                       'familiar moment. Read, talk and trace together at your own pace.',
        'storytitle': 'An Idli for Meera',
        'storyalt': 'Original An Idli for Meera book cover',
        'preview': 'See the story preview',
        'price': '₹49 · Kannada + English · Printable PDF',
        'questionheading': 'Is there a moment you’d like us to write about?',
        'questionbody': 'Suggest an everyday parenting topic through our contact page. Leave out children’s names, '
                        'photos and private details. We use suggestions to plan future articles, rather than provide '
                        'individual advice.',
        'suggest': 'Suggest a future topic',
        'back': 'Back to Parent Corner',
        'footer': 'Little stories. Everyday kindness.',
        'privacy': 'Privacy',
        'support': 'Contact',
        'sourceslink': 'Sources',
        'articlelink': 'Read our first article',
        'closing': 'For now, choose one small thing to try. The rest can wait.'},
 'kn': {'hub': 'parent-corner-kannada.html',
        'article': 'parent-corner/sharing-a-favourite-toy-kn.html',
        'otherhub': 'parent-corner.html',
        'otherarticle': 'parent-corner/sharing-a-favourite-toy.html',
        'corner': 'ಪೋಷಕರಿಗಾಗಿ',
        'stories': 'ಕಥೆಗಳು',
        'about': 'ನಮ್ಮ ಬಗ್ಗೆ',
        'skip': 'ಲೇಖನಕ್ಕೆ ಹೋಗಿ',
        'series': 'ಪೋಷಕರ ದಿನನಿತ್ಯದ ಅನುಭವಗಳು',
        'heading': 'ಸ್ವಲ್ಪ ಸಮಾಧಾನ.<br>ಮುಂದಿನ ಹೆಜ್ಜೆಗೆ ನೆರವು.',
        'intro': 'ಮಕ್ಕಳಿಗೆ ಏನು ಹೇಳಬೇಕು ಎಂದು ತೋಚದ ಕ್ಷಣಗಳಿಗೆ ಸ್ವಲ್ಪ ಸಮಾಧಾನ, ಪ್ರಯತ್ನಿಸಲು ಸರಳ ಸಲಹೆಗಳು. 2–5 ವರ್ಷದ ಮಕ್ಕಳ '
                 'ಪೋಷಕರಿಗಾಗಿ, ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್\u200cನಲ್ಲಿ.',
        'cardtitle': 'ನನ್ನ ಮಗು ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಕೊಡುತ್ತಿಲ್ಲ. ನಾನು ತಪ್ಪು ಮಾಡುತ್ತಿದ್ದೇನಾ?',
        'artcaption': 'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ ಕಥೆಯ ಮೂಲ ಚಿತ್ರ',
        'artalt': 'ಮರದ ಕೆಳಗೆ ಜೊತೆಯಾಗಿ ಇಡ್ಲಿ ಹಂಚಿಕೊಳ್ಳುತ್ತಿರುವ ಅಪ್ಪಿ ಮತ್ತು ಮೀರಾ',
        'jumpphrases': 'ಹೇಳಬಹುದಾದ ಮಾತುಗಳನ್ನು ನೋಡಿ',
        'title': 'ನನ್ನ ಮಗು ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಕೊಡುತ್ತಿಲ್ಲ. ನಾನು ತಪ್ಪು ಮಾಡುತ್ತಿದ್ದೇನಾ?',
        'deck': 'ಒಂದೇ ಆಟಿಕೆ ಇಬ್ಬರಿಗೂ ಬೇಕು. ಎಲ್ಲರೂ ನೋಡುತ್ತಿದ್ದಾರೆ ಅನ್ನೋ ಮುಜುಗರವೂ ಇದೆ. ಮುಂದಿನ ಕ್ಷಣವನ್ನು ಸ್ವಲ್ಪ ಸುಲಭ '
                'ಮಾಡೋಣ.',
        'topic': 'ಆಟಿಕೆಗಳು ಮತ್ತು ಮನೆಯ ಅತಿಥಿಗಳು',
        'age': '2–5 ವರ್ಷ',
        'read': 'ಉತ್ತರ ಓದಿ',
        'latest': 'ಈ ಪ್ರಶ್ನೆಯಿಂದ ಆರಂಭಿಸೋಣ',
        'promise': 'ನೆಮ್ಮದಿಯಾಗಿ ಯೋಚಿಸಲು ಒಂದು ಜಾಗ.',
        'promisebody': 'ದಿನನಿತ್ಯದ ಒಂದು ಸಂದರ್ಭ, ನೆಮ್ಮದಿಯಾಗಿ ಯೋಚಿಸಲು ಸ್ವಲ್ಪ ಜಾಗ, ಪ್ರಯತ್ನಿಸಲು ಒಂದು ಸರಳ ಸಲಹೆ. ಪ್ರತಿ ಉತ್ತರದ '
                       'ಕೊನೆಯಲ್ಲಿ ಬಳಸಿದ ಮೂಲಗಳೂ ಇರುತ್ತವೆ.',
        'pilottag': 'ಮೊದಲ ಲೇಖನ · ಪ್ರಾಯೋಗಿಕ ಪ್ರಕಟಣೆ',
        'byline': 'ಕಬ್ಬನ್ ಕ್ರೇಯಾನ್ಸ್ ಬರಹ',
        'date': 'ಮೂಲಗಳನ್ನು ಪರಿಶೀಲಿಸಿದ ದಿನ: 21 ನವೆಂಬರ್ 2026',
        'notice': 'ಆರಂಭದಲ್ಲಿರುವುದು ಉದಾಹರಣೆಗೆ ಬರೆದ ಸಂದರ್ಭ; ಓದುಗರು ಕಳುಹಿಸಿದ ನೈಜ ಘಟನೆಯಲ್ಲ. ಇದು ಸಾಮಾನ್ಯ ಮಾರ್ಗದರ್ಶನ, ಒಂದು '
                  'ನಿರ್ದಿಷ್ಟ ಮಗುವಿನ ಮೌಲ್ಯಮಾಪನವಲ್ಲ.',
        'opening': 'ಮನೆಗೆ ಬಂದ ಮಕ್ಕಳ ಜೊತೆ ನಿಮ್ಮ ಮಗು ಖುಷಿಯಾಗಿ ಆಡಲಿ ಅಂದುಕೊಂಡಿದ್ದಿರಿ. ಆದರೆ ಈಗ ಅದು ಒಂದು ಆಟಿಕೆಯನ್ನು ಬಿಗಿಯಾಗಿ '
                   'ಹಿಡಿದುಕೊಂಡಿದೆ. ಇನ್ನೊಂದು ಮಗು ಕಾಯುತ್ತಿದೆ. ಎಲ್ಲರೂ ಏನು ಅಂದುಕೊಳ್ಳುತ್ತಾರೋ ಎಂಬ ಚಿಂತೆಯೂ ಬರಬಹುದು. ಆ ಕ್ಷಣ '
                   'ಮುಜುಗರವಾಗಬಹುದು. ಅದಕ್ಕಾಗಿ ನಿಮ್ಮನ್ನಾಗಲಿ, ಮಗುವನ್ನಾಗಲಿ ದೂಷಿಸಬೇಕಿಲ್ಲ.',
        'quickheading': 'ಎಲ್ಲವನ್ನೂ ಇವತ್ತೇ ಕಲಿಸಬೇಕಿಲ್ಲ',
        'quick': 'ಸರದಿಯಲ್ಲಿ ಆಡುವುದನ್ನು ಕಲಿಸಲು, ಮಗುವಿನ ಎಲ್ಲ ಇಷ್ಟದ ಆಟಿಕೆಗಳನ್ನೂ ಬೇರೆಯವರಿಗೆ ಕೊಡಿಸಬೇಕಿಲ್ಲ. ತುಂಬಾ ಇಷ್ಟದ '
                 'ಆಟಿಕೆಯನ್ನು ಅತಿಥಿಗಳು ಬರುವ ಮೊದಲು ತೆಗೆದಿಡಬಹುದು. ಎಲ್ಲರೂ ಆಡಲು ಬೇರೆ ಕೆಲವು ಆಟಿಕೆಗಳನ್ನು ಮಗುವಿನ ಜೊತೆ ಆಯ್ಕೆ '
                 'ಮಾಡಿ. ಜಗಳವಾದರೆ ಹತ್ತಿರವಿದ್ದು ಸಹಾಯ ಮಾಡಿ. ಒಂದೇ ದಿನದಲ್ಲಿ ಎಲ್ಲವನ್ನೂ ಕಲಿಸಬೇಕೆಂಬ ಒತ್ತಡ ಬೇಡ. [1, 2]',
        'toc': 'ಈ ಲೇಖನದಲ್ಲಿ',
        'understand': 'ಕಾಯುವುದು ಇನ್ನೂ ಸುಲಭವಲ್ಲ',
        'understandbody': 'ಎರಡು ವರ್ಷದ ಮಗುವಿಗೂ ಐದು ವರ್ಷದ ಮಗುವಿಗೂ ಬೇಕಾಗುವ ಸಹಾಯ ಬೇರೆಬೇರೆ ಇರಬಹುದು. ಚಿಕ್ಕ ಮಕ್ಕಳಿಗೆ ಕಾಯುವುದು '
                          'ಕಷ್ಟವಾಗಬಹುದು. ಸ್ವಲ್ಪ ದೊಡ್ಡ ಮಕ್ಕಳಿಗೆ ಸರದಿಯಲ್ಲಿ ಆಡುವುದು ಅರ್ಥವಾದರೂ, ಇಷ್ಟದ ಆಟಿಕೆ ಬಂದಾಗ ಕಾಯಲು '
                          'ಕಷ್ಟವಾಗಬಹುದು. ಈಗ ನಿಮ್ಮ ಮಗುವಿಗೆ ಯಾವ ಸಹಾಯ ಬೇಕು ಎಂದು ನೋಡಿ. ಒಂದು ಭೇಟಿಯನ್ನೇ ಮಗುವಿನ ಒಳ್ಳೆಯತನದ '
                          'ಪರೀಕ್ಷೆಯಾಗಿ ನೋಡಬೇಕಿಲ್ಲ. [1, 2]',
        'stepsheading': 'ಮುಂದಿನ ಬಾರಿ ಹೀಗೆ ಮಾಡಿ ನೋಡಿ',
        'steps': [('ಎಲ್ಲರೂ ಬರುವ ಮೊದಲು',
                   'ಒಟ್ಟಿಗೆ ಆಡಲು ಕೆಲವು ಆಟಿಕೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಲು ಮಗುವಿನ ಸಹಾಯ ಕೇಳಿ. ತುಂಬಾ ಇಷ್ಟದ ಆಟಿಕೆಯನ್ನು ಆ ಭೇಟಿಯ '
                   'ಸಮಯದಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ತೆಗೆದಿಡಿ. ಯಾರಾದರೂ ಕಾಯುವ ಮೊದಲೇ ಈ ಬಗ್ಗೆ ಮಾತನಾಡಿಕೊಳ್ಳಬಹುದು. [2, 3]'),
                  ('ಇಬ್ಬರಿಗೂ ಒಂದೇ ಆಟಿಕೆ ಬೇಕಾದಾಗ',
                   'ಎರಡೂ ಮಕ್ಕಳಿಗೆ ಅದೇ ಆಟಿಕೆ ಬೇಕಾಗಿದೆ ಎಂದು ಚಿಕ್ಕದಾಗಿ ಹೇಳಿ. ಸರದಿಯಲ್ಲಿ ಆಡಲು ಸಹಾಯ ಮಾಡಿ. ಕಾಯುವ ಮಗುವಿಗೆ ಬೇರೆ '
                   'ಆಟವನ್ನೂ ಸೂಚಿಸಬಹುದು. ಕಸಿದುಕೊಳ್ಳುವುದನ್ನು, ನೋಯಿಸುವುದನ್ನು ತಡೆಯಿರಿ. [1, 2]'),
                  ('ಆಮೇಲೆ, ಎಲ್ಲರೂ ಶಾಂತವಾದಾಗ',
                   'ಮಗು ಸುಲಭವಾಗಿ ಬೇರೆಯವರಿಗೆ ಕೊಡುವ ಆಟಿಕೆಯಿಂದ ಸರದಿಯಲ್ಲಿ ಆಡಿ ನೋಡಿ. ಮಗು ಇನ್ನೊಬ್ಬರಿಗೆ ಸರದಿ ಕೊಟ್ಟಾಗ ಅದನ್ನು '
                   'ಗಮನಿಸಿ ಮೆಚ್ಚಿ. ಬೇರೆ ಮಗುವಿನ ಜೊತೆ ಹೋಲಿಸಬೇಕಿಲ್ಲ. [1, 2]')],
        'wordsheading': 'ಹೀಗೆ ಹೇಳಿ ನೋಡಬಹುದು',
        'wordsintro': 'ಎಲ್ಲವನ್ನೂ ಒಮ್ಮೆಲೇ ವಿವರಿಸಬೇಕಿಲ್ಲ. ಮೃದುವಾಗಿ ಒಂದು ಚಿಕ್ಕ ಮಾತಿನಿಂದ ಆರಂಭಿಸಿ.',
        'phrases': ['“ನೀವಿಬ್ಬರೂ ಸೇರಿ ಆಡಲು ಏನಾದರೂ ಹುಡುಕೋಣವಾ?”',
                    '“ನೀನು ಇನ್ನೂ ಆಡುತ್ತಿದ್ದೀಯ ಅಲ್ವಾ? ಆಮೇಲೆ ಮುಂದಿನ ಸರದಿ ಯಾರದ್ದು ಅಂತ ನೋಡೋಣ.”'],
        'relativeheading': 'ಸಂಬಂಧಿಕರು ಏನಾದರೂ ಹೇಳಿದರೆ?',
        'relativebody': 'ಆಗ ಆ ಕ್ಷಣ ಇನ್ನೂ ಕಷ್ಟ ಅನ್ನಿಸಬಹುದು. ಚಿಕ್ಕದಾಗಿ ಉತ್ತರಿಸಬಹುದು: “ನಾನು ನೋಡಿಕೊಳ್ಳುತ್ತೇನೆ. ಸ್ವಲ್ಪ ಸಮಯ '
                        'ಕೊಡೋಣ.” ಮಕ್ಕಳು ಶಾಂತವಾದ ಮೇಲೆ ಬೇಕಿದ್ದರೆ ಇನ್ನಷ್ಟು ಮಾತನಾಡಬಹುದು.',
        'againheading': 'ಮುಂದಿನ ಬಾರಿಯೂ ಕಷ್ಟವಾದರೆ?',
        'againbody': 'ಭೇಟಿಯ ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡಿ ನೋಡಿ ಅಥವಾ ಬೇರೆ ಆಟ ಆಯ್ಕೆ ಮಾಡಿ. ಜಗಳಗಳಲ್ಲಿ ಪದೇಪದೇ ಯಾರಿಗಾದರೂ '
                     'ಅಪಾಯವಾಗುತ್ತಿದ್ದರೆ ಅಥವಾ ನಿಭಾಯಿಸುವುದು ತುಂಬಾ ಕಷ್ಟವಾಗುತ್ತಿದ್ದರೆ, ನಿಮ್ಮ ಕುಟುಂಬಕ್ಕೆ ತಕ್ಕ ಸಲಹೆಗಾಗಿ ಅರ್ಹ '
                     'ತಜ್ಞರ ಸಹಾಯ ಕೇಳಿ.',
        'sourceheading': 'ಈ ಉತ್ತರಕ್ಕೆ ಬಳಸಿದ ಮೂಲಗಳು',
        'sourcenote': 'ವಯಸ್ಸಿನ ವಿವರಣೆ ಮತ್ತು ಸರಳ ಸಲಹೆಗಳಿಗೆ ಈ ಮೂಲಗಳನ್ನು ಬಳಸಲಾಗಿದೆ. ಲೇಖನದ ಬರಹ, ಉದಾಹರಣೆಯ ಸಂದರ್ಭ ಮತ್ತು '
                      'ಮಾತುಗಳನ್ನು ಕಬ್ಬನ್ ಕ್ರೇಯಾನ್ಸ್\u200cಗಾಗಿ ಸ್ವತಂತ್ರವಾಗಿ ಬರೆಯಲಾಗಿದೆ. ಈ ಲೇಖನವನ್ನು ಸ್ವತಂತ್ರ ತಜ್ಞರು '
                      'ಪರಿಶೀಲಿಸಿಲ್ಲ.',
        'relatedheading': 'ಕಥೆಯ ಜೊತೆ ಮಾತು ಮುಂದುವರಿಸೋಣ',
        'relatedbody': 'ಕಥೆಯಿಂದ ಮಾತು ಆರಂಭಿಸುವುದು ಸುಲಭ ಅನ್ನಿಸಿದರೆ, “ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ” ಓದಿ ನೋಡಬಹುದು. ಅದರಲ್ಲಿ '
                       'ಹಂಚಿಕೊಳ್ಳುವ ಇನ್ನೊಂದು ಪರಿಚಿತ ಸಂದರ್ಭವಿದೆ. ನಿಮ್ಮ ಅನುಕೂಲಕ್ಕೆ ತಕ್ಕಂತೆ ಜೊತೆಯಾಗಿ ಓದಿ, ಮಾತನಾಡಿ, '
                       'ಚಟುವಟಿಕೆ ಮಾಡಿ.',
        'storytitle': 'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ',
        'storyalt': 'ಮೀರಾಳಿಗೆ ಒಂದು ಇಡ್ಲಿ ಪುಸ್ತಕದ ಮೂಲ ಮುಖಪುಟ',
        'preview': 'ಕಥೆಯ ಮಾದರಿ ಪುಟಗಳನ್ನು ನೋಡಿ',
        'price': '₹49 · ಕನ್ನಡ + ಇಂಗ್ಲಿಷ್ · ಮುದ್ರಿಸಬಹುದಾದ ಪಿಡಿಎಫ್',
        'questionheading': 'ಯಾವ ಸಂದರ್ಭದ ಬಗ್ಗೆ ನಾವು ಬರೆಯಲಿ?',
        'questionbody': 'ಮಕ್ಕಳನ್ನು ಬೆಳೆಸುವಾಗ ಎದುರಾಗುವ ದಿನನಿತ್ಯದ ವಿಷಯವನ್ನು ನಮ್ಮ ಸಂಪರ್ಕ ಪುಟದಲ್ಲಿ ಸೂಚಿಸಿ. ಮಕ್ಕಳ ಹೆಸರುಗಳು, '
                        'ಫೋಟೋಗಳು ಮತ್ತು ಖಾಸಗಿ ವಿವರಗಳನ್ನು ಸೇರಿಸಬೇಡಿ. ಈ ಸಲಹೆಗಳನ್ನು ಮುಂದಿನ ಲೇಖನಗಳ ಆಯ್ಕೆಗೆ ಬಳಸುತ್ತೇವೆ; '
                        'ವೈಯಕ್ತಿಕ ಮಾರ್ಗದರ್ಶನ ನೀಡುವುದಕ್ಕಲ್ಲ.',
        'suggest': 'ಮುಂದಿನ ವಿಷಯ ಸೂಚಿಸಿ',
        'back': 'ಪೋಷಕರ ಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ',
        'footer': 'ಪುಟ್ಟ ಕಥೆಗಳು. ದಿನನಿತ್ಯದ ಕಾಳಜಿ.',
        'privacy': 'ಗೌಪ್ಯತೆ',
        'support': 'ಸಂಪರ್ಕ',
        'sourceslink': 'ಮೂಲಗಳು',
        'articlelink': 'ನಮ್ಮ ಮೊದಲ ಲೇಖನ ಓದಿ',
        'closing': 'ಸದ್ಯಕ್ಕೆ ಒಂದನ್ನು ಪ್ರಯತ್ನಿಸಿ ನೋಡಿ. ಉಳಿದದ್ದನ್ನು ಆಮೇಲೆ ನೋಡಿಕೊಳ್ಳಬಹುದು.'}}
def esc(x):return html.escape(x,quote=True)
def langlinks(d,kind,lang):
 other=d['other'+kind]
 paths={'en':d[kind] if lang=='en' else other,'kn':d[kind] if lang=='kn' else other}
 return '<nav class="language-choice" aria-label="Reading language">'+''.join(f'<a href="/{paths[k]}" lang="{k}" hreflang="{k}" data-reading-language="{k}"'+(' aria-current="page"' if k==lang else '')+'>'+label+'</a>' for k,label in [('en','English'),('kn','ಕನ್ನಡ')])+'</nav>'
def shell(lang,kind,body):
 d=DATA[lang];path=d[kind];other=d['other'+kind];title=d['corner'] if kind=='hub' else d['title']
 alternates=langlinks(d,kind,lang)
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self' data:; style-src 'self'; script-src 'self'; font-src 'self'; base-uri 'none'; form-action 'none'"><meta name="theme-color" content="#fcf9f1"><title>{esc(title)} · Cubbon Crayons</title><meta name="description" content="{esc(d['deck'] if kind=='article' else d['intro'])}"><link rel="canonical" href="{URL}/{path}"><link rel="alternate" hreflang="{lang}" href="{URL}/{path}"><link rel="alternate" hreflang="{'kn' if lang=='en' else 'en'}" href="{URL}/{other}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(d['deck'])}"><meta property="og:url" content="{URL}/{path}"><meta property="og:type" content="{'article' if kind=='article' else 'website'}"><link rel="stylesheet" href="/styles.css?v=20261121-larger-covers"><link rel="stylesheet" href="/parent-corner.css?v=20261121-warm"><script src="/parent-corner.js?v=20261121-warm" defer></script></head><body class="home editorial"><a class="skip-link" href="#reading">{d['skip']}</a><header class="site-header wrap"><a class="brand" href="/"><span class="mark" aria-hidden="true">c<span>.</span></span>Cubbon Crayons</a><nav aria-label="Main navigation"><a href="/#stories">{d['stories']}</a><a href="/{d['hub']}" aria-current="page">{d['corner']}</a><a href="/#our-story">{d['about']}</a></nav></header><main id="reading" class="editorial-main wrap"><div class="editorial-topline"><a class="breadcrumb" href="/{d['hub']}">{d['corner']}</a>{alternates}</div>{body}</main><footer class="site-footer wrap"><span>© 2026 Cubbon Crayons</span><nav aria-label="Footer"><a href="/privacy.html">{d['privacy']}</a><a href="https://payhip.com/CubbonCrayons/contact" rel="noreferrer">{d['support']}</a></nav></footer></body></html>'''
def hub(lang):
 d=DATA[lang]
 intro=d['intro'].replace('2–5','<span class="age-range">2–5</span>')
 body=f'''<section class="editorial-hero"><p class="eyebrow">{d['series']}</p><h1>{d['heading']}</h1><p class="editorial-deck">{intro}</p></section><section class="first-read" aria-labelledby="first-title"><figure class="feature-art"><img src="/assets/parent-corner-sharing.webp" width="744" height="990" alt="{d['artalt']}" fetchpriority="high"><figcaption>{d['artcaption']}</figcaption></figure><div class="first-read-copy"><p class="eyebrow">{d['latest']}</p><p class="article-meta">{d['topic']} · {d['age']}</p><h2 id="first-title"><a href="/{d['article']}">{d['cardtitle']}</a></h2><p>{d['deck']}</p><a class="button" href="/{d['article']}">{d['read']}</a><p class="pilot-note">{d['pilottag']}</p></div></section><section class="editorial-promise"><h2>{d['promise']}</h2><p>{d['promisebody']}</p></section>'''
 return shell(lang,'hub',body)
def article(lang):
 d=DATA[lang];ids=[('understand',d['understand']),('try',d['stepsheading']),('words',d['wordsheading']),('sources',d['sourceheading'])]
 toc=''.join(f'<li><a href="#{key}">{title}</a></li>' for key,title in ids)
 steps=''.join(f'<li><h3>{title}</h3><p>{copy}</p></li>' for title,copy in d['steps'])
 phrases=''.join(f'<p class="say-line">{p}</p>' for p in d['phrases'])
 sources=''.join(f'<li><a href="{url}" rel="noreferrer">{name}</a></li>' for name,url in SOURCES)
 body=f'''<article><header class="article-header"><p class="eyebrow">{d['series']}</p><p class="article-meta">{d['topic']} · {d['age']}</p><h1>{d['title']}</h1><p class="editorial-deck">{d['deck']}</p><p class="article-meta">{d['byline']} · <time datetime="2026-11-21">{d['date']}</time></p><p class="pilot-note">{d['pilottag']}</p></header><div class="article-layout"><aside class="reading-toc"><details><summary>{d['toc']}</summary><ul>{toc}</ul></details></aside><div class="article-prose"><p class="opening">{d['opening']}</p><section class="quick-answer"><h2>{d['quickheading']}</h2><p>{d['quick']}</p><a class="phrase-jump" href="#words">{d['jumpphrases']}</a></section><section id="understand"><h2>{d['understand']}</h2><p>{d['understandbody']}</p></section><section id="try"><h2>{d['stepsheading']}</h2><ul class="practical-options">{steps}</ul></section><section id="words" class="words-panel" aria-labelledby="words-title"><p class="eyebrow">{'A LITTLE HELP WITH THE WORDS' if lang=='en' else 'ಮಾತುಗಳಿಗೆ ಒಂದು ಪುಟ್ಟ ನೆರವು'}</p><h2 id="words-title">{d['wordsheading']}</h2><p>{d['wordsintro']}</p>{phrases}</section><section><h2>{d['relativeheading']}</h2><p>{d['relativebody']}</p></section><section><h2>{d['againheading']}</h2><p>{d['againbody']}</p><p class="gentle-close">{d['closing']}</p></section><section id="sources" class="article-sources"><h2>{d['sourceheading']}</h2><ol>{sources}</ol><p>{d['sourcenote']}</p><p class="scenario-note">{d['notice']}</p></section><aside class="related-story" aria-labelledby="related-title"><img src="/assets/previews/idli-cover-small.webp" alt="{d['storyalt']}" width="780" height="1103" loading="lazy"><div><p class="eyebrow">{'OPTIONAL STORY COMPANION' if lang=='en' else 'ಓದಲು ಒಂದು ಸಂಬಂಧಿತ ಕಥೆ'}</p><h2 id="related-title">{d['relatedheading']}</h2><p>{d['relatedbody']}</p><p><strong>{d['storytitle']}</strong><br>{d['price']}</p><a class="text-link" href="/?preview=idli#previews" data-parent-story="idli">{d['preview']}</a></div></aside><section class="suggest-topic"><h2>{d['questionheading']}</h2><p>{d['questionbody']}</p><a class="text-link" href="https://payhip.com/CubbonCrayons/contact" rel="noreferrer">{d['suggest']}</a></section><a class="back-link" href="/{d['hub']}">{d['back']}</a></div></div></article>'''
 return shell(lang,'article',body)
for lang in DATA:
 for kind,fn in [('hub',hub),('article',article)]:
  path=OUT/DATA[lang][kind];path.parent.mkdir(exist_ok=True,parents=True);path.write_text(fn(lang),encoding='utf8')
(ROOT/'article-content.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf8')
print('Built four bilingual pages, one original article.')
