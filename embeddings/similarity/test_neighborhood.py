import sys
from unittest import TestCase
from unittest.mock import MagicMock

from embeddings.similarity.neighborhood import Neighborhood
from embeddings.word2vec import Word2vec
from parameters.parameters import Parameters


class TestNeighborhood(TestCase):
    def setUp(self):
        self.word2vec = Word2vec()
        self.parameters = Parameters()
        self.parameters.params["repo_dir"] = '/scratch/index/indri_5_7/ap8889'

        self.doc_words = ['pride', 'prejudice', 'novel', 'jane', 'austen', 'published', 'story', 'charts', 'emotional',
                          'development', 'protagonist', 'elizabeth', 'bennet', 'learns', 'error', 'making', 'hasty',
                          'judgements', 'comes', 'appreciate', 'difference', 'superficial', 'essential', 'comedy',
                          'writing', 'lies', 'depiction', 'manners', 'education', 'marriage', 'money', 'british',
                          'regency', 'bennet', 'estate', 'daughters', 'property', 'entailed', 'meaning', 'girls',
                          'inherit', 'married', 'woman', 'fortune', 'imperative', 'girls', 'marries', 'order',
                          'support', 'death', 'jane', 'austen', 'opening', 'line', 'truth', 'universally',
                          'acknowledged', 'single', 'man', 'possession', 'good', 'fortune', 'wife', 'sentence',
                          'filled', 'irony', 'playfulness', 'novel', 'revolves', 'necessity', 'marrying', 'love',
                          'simply', 'mercenary', 'reasons', 'despite', 'social', 'pressures', 'make', 'good', 'wealthy',
                          'match', 'pride', 'prejudice', 'retains', 'fascination', 'modern', 'readers', 'consistently',
                          'appearing', 'near', 'top', 'lists', 'loved', 'books', 'literary', 'scholars', 'general',
                          'public', 'popular', 'novels', 'english', 'literature', 'million', 'copies', 'sold', 'paved',
                          'way', 'specify', 'archetypes', 'abound', 'modern', 'literature', 'continuing', 'interest',
                          'book', 'resulted', 'number', 'dramatic', 'adaptations', 'abundance', 'novels', 'stories',
                          'imitating', 'austen', 'memorable', 'characters', 'themes', 'article', 'plot', 'summary',
                          'long', 'excessively', 'detailed', 'please', 'help', 'improve', 'removing', 'unnecessary',
                          'details', 'making', 'concise', 'september', 'learn', 'remove', 'template', 'message',
                          'novel', 'opens', 'bennet', 'trying', 'persuade', 'bennet', 'visit', 'eligible', 'bachelor',
                          'arrived', 'neighborhood', 'verbal', 'sparring', 'bennet', 'baiting', 'wife', 'transpires',
                          'visit', 'taken', 'place', 'rented', 'house', 'visit', 'followed', 'invitation', 'ball',
                          'local', 'assembly', 'rooms', 'neighborhood', 'attend', 'ball', 'open', 'cheerful', 'popular',
                          'guests', 'appears', 'attracted', 'beautiful', 'miss', 'bennet', 'friend', 'darcy', 'reputed',
                          'twice', 'wealthy', 'haughty', 'aloof', 'declines', 'dance', 'elizabeth', 'suggesting',
                          'pretty', 'tempt', 'finds', 'amusing', 'jokes', 'statement', 'friends', 'miss', 'jane',
                          'bennet', 'attracts', 'attention', 'sister', 'caroline', 'invites', 'visit', 'jane', 'visits',
                          'miss', 'caught', 'rain', 'shower', 'way', 'catching', 'serious', 'cold', 'elizabeth',
                          'genuine', 'concern', 'sister', 'visits', 'sister', 'point', 'darcy', 'begins', 'attraction',
                          'elizabeth', 'miss', 'jealous', 'elizabeth', 'wants', 'marry', 'darcy', 'illustration',
                          'hugh', 'thomson', 'representing', 'collins', 'protesting', 'reads', 'novels', 'collins',
                          'cousin', 'bennet', 'heir', 'estate', 'visits', 'bennet', 'family', 'pompous', 'obsequious',
                          'clergyman', 'expects', 'bennet', 'girls', 'wish', 'marry', 'due', 'inheritance', 'plans',
                          'propose', 'elizabeth', 'jane', 'led', 'believe', 'jane', 'taken', 'elizabeth', 'family',
                          'meet', 'dashing', 'charming', 'wickham', 'singles', 'elizabeth', 'tells', 'story',
                          'hardship', 'darcy', 'caused', 'depriving', 'living', 'position', 'clergyman', 'prosperous',
                          'parish', 'good', 'revenue', 'granted', 'life', 'promised', 'darcy', 'late', 'father',
                          'elizabeth', 'dislike', 'darcy', 'confirmed', 'ball', 'wickham', 'present', 'elizabeth',
                          'dances', 'darcy', 'jane', 'elizabeth', 'members', 'bennet', 'family', 'show', 'lack',
                          'decorum', 'bennet', 'states', 'loudly', 'expects', 'jane', 'engaged', 'member', 'family',
                          'exposes', 'ridicule', 'following', 'morning', 'collins', 'proposes', 'elizabeth', 'rejects',
                          'fury', 'mother', 'relief', 'father', 'receive', 'news', 'leaving', 'london', 'collins',
                          'proposed', 'charlotte', 'lucas', 'sensible', 'lady', 'elizabeth', 'friend', 'slightly',
                          'older', 'grateful', 'receive', 'proposal', 'guarantee', 'home', 'elizabeth', 'aghast',
                          'pragmatism', 'matters', 'love', 'jane', 'goes', 'visit', 'aunt', 'uncle', 'gardiner',
                          'unfashionable', 'address', 'london', 'miss', 'clearly', 'continue', 'friendship', 'jane',
                          'upset', 'composed', 'spring', 'elizabeth', 'visits', 'charlotte', 'collins', 'kent',
                          'elizabeth', 'hosts', 'frequently', 'invited', 'rosings', 'park', 'imposing', 'home', 'lady',
                          'catherine', 'lady', 'catherine', 'darcy', 'aunt', 'extremely', 'wealthy', 'expects', 'darcy',
                          'marry', 'daughter', 'darcy', 'cousin', 'colonel', 'fitzwilliam', 'visit', 'lady',
                          'catherine', 'colonel', 'fitzwilliam', 'tells', 'elizabeth', 'darcy', 'managed', 'friend',
                          'bad', 'match', 'convincing', 'friend', 'lady', 'indifference', 'elizabeth', 'horrified',
                          'darcy', 'involvement', 'affair', 'caused', 'sister', 'pain', 'darcy', 'fallen', 'love',
                          'elizabeth', 'proposes', 'rejects', 'stating', 'love', 'man', 'caused', 'sister',
                          'unhappiness', 'accuses', 'treating', 'wickham', 'unjustly', 'darcy', 'accuses', 'family',
                          'wanting', 'propriety', 'suggests', 'kinder', 'furious', 'part', 'barely', 'speaking',
                          'following', 'morning', 'darcy', 'gives', 'elizabeth', 'letter', 'explains', 'treatment',
                          'wickham', 'caused', 'fact', 'wickham', 'refused', 'living', 'compensated', 'economically',
                          'proceeded', 'waste', 'money', 'impoverished', 'demanded', 'living', 'threats', 'refused',
                          'tried', 'elope', 'darcy', 'old', 'sister', 'georgiana', 'great', 'dowry', 'colonel',
                          'fitzwilliam', 'attest', 'claimed', 'believed', 'miss', 'bennet', 'despite', 'amiability',
                          'actually', 'bit', 'reserved', 'love', 'darcy', 'apologises', 'hurting', 'jane', 'elizabeth',
                          'begins', 'rejudge', 'darcy', 'clearer', 'basis', 'elizabeth', 'tells', 'father', 'darcy',
                          'responsible', 'uniting', 'lydia', 'wickham', 'two', 'earliest', 'illustrations', 'pride',
                          'prejudice', 'clothing', 'styles', 'reflect', 'time', 'illustration', 'engraved', 'time',
                          'novel', 'written', 'set', 'months', 'later', 'elizabeth', 'aunt', 'uncle', 'gardiner',
                          'visit', 'darcy', 'estate', 'derbyshire', 'elizabeth', 'hears', 'account', 'housekeeper',
                          'generous', 'darcy', 'returns', 'unexpectedly', 'overwhelmingly', 'civil', 'invites',
                          'elizabeth', 'gardiner', 'meet', 'sister', 'fishing', 'elizabeth', 'surprised', 'delighted',
                          'kindness', 'aunt', 'uncle', 'suddenly', 'news', 'sister', 'lydia', 'eloped', 'wickham',
                          'tells', 'darcy', 'immediately', 'departs', 'haste', 'believing', 'lydia', 'disgrace', 'ruin',
                          'family', 'good', 'name', 'agonizing', 'wait', 'wickham', 'persuaded', 'marry', 'lydia',
                          'payment', 'debts', 'required', 'degree', 'decency', 'restored', 'lydia', 'visits',
                          'elizabeth', 'tells', 'darcy', 'wedding', 'gardiner', 'informs', 'elizabeth', 'darcy', 'made',
                          'match', 'hints', 'motive', 'point', 'darcy', 'return', 'proposes', 'jane', 'accepted',
                          'delight', 'lady', 'catherine', 'visits', 'elizabeth', 'impression', 'going', 'marry',
                          'darcy', 'elizabeth', 'refuses', 'deny', 'claim', 'lady', 'catherine', 'leaves', 'outraged',
                          'perceived', 'insolence', 'darcy', 'elizabeth', 'walk', 'engaged', 'elizabeth', 'convince',
                          'father', 'marrying', 'money', 'speaks', 'darcy', 'true', 'worth', 'happy', 'wedding',
                          'elizabeth', 'darcy', 'hugh', 'thomson', 'elizabeth', 'bennet', 'edit', 'elizabeth', 'darcy',
                          'bennet', 'reader', 'sees', 'unfolding', 'plot', 'characters', 'viewpoint', 'second',
                          'bennet', 'daughters', 'twenty', 'years', 'old', 'intelligent', 'lively', 'playful',
                          'attractive', 'witty', 'tendency', 'judge', 'impression', 'prejudice', 'title', 'selective',
                          'evidence', 'bases', 'judgments', 'plot', 'begins', 'closest', 'relationships', 'father',
                          'sister', 'jane', 'aunt', 'gardiner', 'best', 'friend', 'charlotte', 'lucas', 'story',
                          'progresses', 'relationship', 'darcy', 'course', 'elizabeth', 'darcy', 'relationship',
                          'ultimately', 'decided', 'darcy', 'overcomes', 'pride', 'elizabeth', 'overcomes', 'prejudice',
                          'leading', 'surrender', 'love', 'fitzwilliam', 'darcy', 'edit', 'fitzwilliam', 'darcy',
                          'esquire', 'initially', 'presented', 'wealthy', 'friend', 'newcomer', 'village', 'ultimately',
                          'elizabeth', 'bennet', 'love', 'interest', 'darcy', 'twenty', 'eight', 'old', 'wealthy',
                          'owner', 'renowned', 'family', 'estate', 'derbyshire', 'rumoured', 'worth', 'least',
                          'equivalent', 'usd', 'million', 'million', 'usd', 'depending', 'method', 'calculation',
                          'income', 'put', 'wealthiest', 'families', 'country', 'time', 'meaning', 'inheritance',
                          'family', 'accumulated', 'fortune', 'totals', 'minimum', 'likewise', 'inheritance', 'totals',
                          'giving', 'interest', 'handsome', 'tall', 'intelligent', 'darcy', 'lacks', 'ease', 'social',
                          'graces', 'comes', 'naturally', 'closest', 'friend', 'charles', 'cousin', 'colonel',
                          'fitzwilliam', 'former', 'childhood', 'friend', 'turned', 'antagonist', 'george', 'wickham',
                          'abuses', 'frequently', 'mistake', 'aloof', 'decorum', 'rectitude', 'proof', 'excessive',
                          'pride', 'part', 'considered', 'pride', 'title', 'makes', 'poor', 'impression', 'strangers',
                          'landed', 'gentry', 'darcy', 'greatly', 'valued', 'know', 'novel', 'progresses', 'darcy',
                          'elizabeth', 'repeatedly', 'forced', 'company', 'resulting', 'altering', 'feelings', 'better',
                          'acquaintance', 'changes', 'environment', 'end', 'work', 'overcome', 'differences',
                          'impressions', 'fall', 'love', 'bennet', 'edit', 'bennet', 'esquire', 'late', 'middle',
                          'aged', 'landed', 'gentleman', 'modest', 'income', 'annum', 'patriarch', 'dwindling',
                          'bennet', 'family', 'family', 'hertfordshire', 'landed', 'gentry', 'five', 'unmarried',
                          'daughters', 'beginning', 'story', 'jane', 'elizabeth', 'lizzy', 'eliza', 'mary', 'catherine',
                          'kitty', 'lydia', 'bennet', 'bennet', 'described', 'appearance', 'book', 'odd', 'mixture',
                          'quick', 'parts', 'sarcastic', 'humour', 'reserve', 'caprice', 'experience', 'three',
                          'twenty', 'years', 'insufficient', 'make', 'wife', 'understand', 'character', 'ironic',
                          'sarcastic', 'cynical', 'sense', 'humour', 'irritates', 'wife', 'indolent', 'parenting',
                          'style', 'manners', 'suggested', 'questionable', 'times', 'novel', 'loves', 'daughters',
                          'elizabeth', 'particular', 'ultimately', 'bennet', 'blames', 'insufficiently', 'disciplining',
                          'daughters', 'ultimately', 'enabled', 'lydia', 'run', 'away', 'wickham', 'resent',
                          'elizabeth', 'advised', 'letting', 'lydia', 'brighton', 'colonel', 'forster', 'regiment',
                          'newly', 'married', 'forster', 'particular', 'friend', 'place', 'bennet', 'possesses',
                          'inherited', 'property', 'estate', 'estate', 'entailed', 'pass', 'male', 'heirs', 'bennet',
                          'daughters', 'inherit', 'estate', 'death', 'addition', 'allowed', 'income', 'spent',
                          'frivolously', 'wife', 'failed', 'put', 'aside', 'money', 'daughters', 'dowries', 'five',
                          'daughters', 'left', 'death', 'share', 'mother', 'dowry', 'bennet', 'current', 'heir',
                          'presumptive', 'distant', 'second', 'cousin', 'sorts', 'william', 'collins', 'son', 'late',
                          'distant', 'cousin', 'bennet', 'later', 'story', 'volume', 'chapter', 'revealed', 'narrator',
                          'bennet', 'married', 'wife', 'based', 'initial', 'superficial', 'attraction', 'bennet',
                          'captivated', 'youth', 'beauty', 'appearance', 'good', 'humour', 'youth', 'beauty',
                          'generally', 'give', 'married', 'woman', 'weak', 'understanding', 'illiberal', 'mind',
                          'early', 'marriage', 'put', 'end', 'real', 'affection', 'respect', 'esteem', 'confidence',
                          'vanished', 'views', 'domestic', 'happiness', 'overthrown', 'bennet', 'disposition', 'seek',
                          'comfort', 'disappointment', 'imprudence', 'brought', 'pleasures', 'console', 'unfortunate',
                          'folly', 'vice', 'safe', 'say', 'speaks', 'living', 'making', 'sport', 'neighbours',
                          'laughing', 'turn', 'saying', 'folly', 'married', 'bennet', 'place', 'bennet', 'edit',
                          'bennet', 'gardiner', 'middle', 'aged', 'wife', 'social', 'superior', 'bennet', 'mother',
                          'five', 'daughters', 'jane', 'elizabeth', 'lizzy', 'eliza', 'mary', 'catherine', 'kitty',
                          'lydia', 'bennet', 'bennet', 'shameless', 'childish', 'frivolous', 'excitable',
                          'temperamental', 'officious', 'greedy', 'grasping', 'illogical', 'loquacious', 'invasive',
                          'artless', 'attention', 'seeking', 'hypochondriac', 'imagines', 'susceptible', 'attacks',
                          'tremors', 'palpitations', 'poor', 'nerves', 'displeased', 'things', 'going', 'way', 'child',
                          'emotionally', 'adult', 'body', 'public', 'manners', 'social', 'climbing', 'source',
                          'constant', 'embarrassment', 'jane', 'elizabeth', 'pastimes', 'shopping', 'socializing',
                          'gossiping', 'boasting', 'favourite', 'daughter', 'youngest', 'lydia', 'takes', 'younger',
                          'self', 'values', 'eldest', 'jane', 'jane', 'great', 'physical', 'beauty', 'considers',
                          'jane', 'feelings', 'virtue', 'reputation', 'least', 'favourite', 'daughter', 'elizabeth',
                          'closely', 'followed', 'mary', 'understand', 'main', 'ambition', 'life', 'marry', 'daughters',
                          'wealthy', 'men', 'matches', 'give', 'daughters', 'happiness', 'concern', 'jane', 'bennet',
                          'edit', 'letter', 'cassandra', 'dated', 'jane', 'austen', 'describes', 'picture', 'gallery',
                          'good', 'likeness', 'jane', 'bennet', 'deirdre', 'faye', 'world', 'novels', 'suggests',
                          'portrait', 'picture', 'austen', 'referring', 'jane', 'bennet', 'eldest', 'bennet', 'sister',
                          'twenty', 'two', 'years', 'old', 'novel', 'begins', 'considered', 'beautiful', 'young',
                          'lady', 'character', 'contrasted', 'elizabeth', 'sweeter', 'shyer', 'equally', 'sensible',
                          'clever', 'notable', 'trait', 'desire', 'good', 'anna', 'quindlen', 'wrote', 'jane', 'sugar',
                          'elizabeth', 'lemonade', 'jane', 'closest', 'elizabeth', 'character', 'contrasted',
                          'elizabeth', 'falls', 'love', 'charles', 'rich', 'young', 'gentleman', 'recently', 'moved',
                          'hertfordshire', 'close', 'friend', 'darcy', 'love', 'initially', 'thwarted', 'darcy',
                          'caroline', 'concerned', 'jane', 'low', 'situation', 'society', 'plans', 'darcy', 'aided',
                          'elizabeth', 'eventually', 'sees', 'error', 'ways', 'instrumental', 'bringing', 'jane',
                          'back', 'mary', 'bennet', 'edit', 'mary', 'bennet', 'plain', 'bennet', 'sister', 'join',
                          'family', 'activities', 'reads', 'plays', 'music', 'impatient', 'display', 'accomplishments',
                          'vain', 'work', 'hard', 'knowledge', 'accomplishment', 'genius', 'taste', 'two', 'younger',
                          'sisters', 'kitty', 'lydia', 'silly', 'bennet', 'mary', 'intelligent', 'thinks', 'wise',
                          'collins', 'refused', 'elizabeth', 'bennet', 'hopes', 'mary', 'prevailed', 'accept', 'led',
                          'believe', 'mary', 'hopes', 'direction', 'knows', 'engaged', 'charlotte', 'lucas', 'time',
                          'mary', 'appear', 'novel', 'sister', 'elizabeth', 'bennet', 'prefers', 'reason', 'feel',
                          'james', 'edward', 'austen', 'leigh', 'memoir', 'jane', 'austen', 'mary', 'ended', 'marrying',
                          'uncle', 'philips', 'law', 'clerks', 'name', 'mentioned', 'moving', 'catherine', 'bennet',
                          'edit', 'catherine', 'kitty', 'bennet', 'fourth', 'daughter', 'years', 'old', 'older',
                          'lydia', 'shadow', 'follows', 'pursuits', 'officers', 'regiment', 'appears', 'portrayed',
                          'envious', 'lydia', 'silly', 'young', 'woman', 'improved', 'end', 'novel', 'james', 'edward',
                          'austen', 'leigh', 'memoir', 'jane', 'austen', 'kitty', 'later', 'married', 'clergyman',
                          'name', 'mentioned', 'lived', 'near', 'derbyshire', 'lydia', 'bennet', 'edit', 'lydia',
                          'wickham', 'bennet', 'youngest', 'bennet', 'sister', 'aged', 'novel', 'begins', 'frivolous',
                          'headstrong', 'main', 'activity', 'life', 'socializing', 'especially', 'flirting', 'officers',
                          'militia', 'leads', 'running', 'george', 'wickham', 'intention', 'marrying', 'dominates',
                          'older', 'sister', 'kitty', 'supported', 'family', 'mother', 'lydia', 'shows', 'regard',
                          'moral', 'code', 'society', 'ashley', 'tauchert', 'says', 'lydia', 'feels', 'reasoning',
                          'feels', 'remorse', 'disgrace', 'causes', 'family', 'charles', 'edit', 'charles', 'esquire',
                          'handsome', 'affable', 'amiable', 'good', 'natured', 'wealthy', 'young', 'gentleman',
                          'nouveau', 'riche', 'years', 'old', 'beginning', 'novel', 'leases', 'park', 'estate', 'miles',
                          'hopes', 'purchasing', 'respectable', 'family', 'roots', 'north', 'england', 'entire',
                          'fortune', 'derived', 'trade', 'charles', 'late', 'father', 'wished', 'purchase', 'estate',
                          'order', 'raise', 'family', 'ranks', 'gentry', 'died', 'son', 'charles', 'inheriting',
                          'father', 'fortune', 'giving', 'income', 'annum', 'interest', 'seeks', 'make', 'wish',
                          'reality', 'buying', 'country', 'manor', 'surrounding', 'estate', 'beginning', 'novel',
                          'charles', 'leasing', 'park', 'hope', 'prove', 'perfect', 'plans', 'contrasted', 'friend',
                          'darcy', 'charming', 'generally', 'pleasing', 'manners', 'clever', 'experienced', 'lacks',
                          'resolve', 'easily', 'influenced', 'practically', 'led', 'nose', 'sisters', 'two', 'sisters',
                          'miss', 'caroline', 'louisa', 'hurst', 'disapprove', 'growing', 'affection', 'miss', 'jane',
                          'bennet', 'caroline', 'edit', 'caroline', 'vainglorious', 'snobbish', 'sister', 'charles',
                          'dowry', 'giving', 'additional', 'interest', 'annum', 'inheritance', 'miss', 'harbours',
                          'designs', 'darcy', 'jealous', 'growing', 'attachment', 'elizabeth', 'attempts', 'dissuade',
                          'darcy', 'liking', 'elizabeth', 'ridiculing', 'bennet', 'family', 'criticising', 'elizabeth',
                          'comportment', 'miss', 'disapproves', 'brother', 'esteem', 'jane', 'bennet', 'acknowledged',
                          'later', 'darcy', 'agreement', 'attempted', 'separate', 'couple', 'attempting', 'dissuade',
                          'jane', 'attachment', 'concealing', 'brother', 'jane', 'presence', 'london', 'jane',
                          'determined', 'find', 'fault', 'finally', 'forced', 'admit', 'deceived', 'thinking',
                          'genuine', 'friendship', 'caroline', 'realisation', 'relays', 'elizabeth', 'letter',
                          'described', 'novel', 'sister', 'fine', 'women', 'air', 'decided', 'fashion', 'disdainful',
                          'society', 'hertfordshire', 'louisa', 'caroline', 'behaviour', 'assembly', 'calculated',
                          'please', 'general', 'quickness', 'observation', 'temper', 'sister', 'judgment', 'unassailed',
                          'attention', 'disposed', 'approve', 'fact', 'fine', 'ladies', 'deficient', 'good', 'humour',
                          'pleased', 'power', 'agreeable', 'chose', 'proud', 'conceited', 'handsome', 'educated',
                          'private', 'seminaries', 'town', 'fortune', 'habit', 'spending', 'associating', 'people',
                          'rank', 'respect', 'entitled', 'think', 'respectable', 'family', 'north', 'england',
                          'circumstance', 'deeply', 'impressed', 'memories', 'brother', 'fortune', 'acquired', 'trade',
                          'george', 'wickham', 'edit', 'george', 'wickham', 'acquainted', 'darcy', 'infancy', 'son',
                          'darcy', 'father', 'steward', 'officer', 'militia', 'superficially', 'charming', 'rapidly',
                          'forms', 'attachment', 'elizabeth', 'bennet', 'spreads', 'tales', 'wrongs', 'darcy', 'done',
                          'adding', 'local', 'society', 'prejudice', 'eventually', 'found', 'wrongdoer', 'runs',
                          'lydia', 'intention', 'marrying', 'resulted', 'complete', 'disgrace', 'darcy', 'intervention',
                          'bribe', 'wickham', 'marry', 'paying', 'immediate', 'debts', 'william', 'collins', 'edit',
                          'article', 'contain', 'excessive', 'amount', 'intricate', 'detail', 'interest', 'specific',
                          'audience', 'please', 'help', 'spinning', 'relocating', 'relevant', 'information', 'removing',
                          'excessive', 'detail', 'inclusion', 'policy', 'january', 'learn', 'remove', 'template',
                          'message', 'rev', 'william', 'collins', 'aged', 'years', 'old', 'novel', 'begins', 'bennet',
                          'distant', 'second', 'cousin', 'clergyman', 'current', 'heir', 'presumptive', 'estate',
                          'house', 'physical', 'appearance', 'described', 'tall', 'heavy', 'looking', 'young', 'man',
                          'five', 'twenty', 'air', 'grave', 'stately', 'manners', 'formal', 'born', 'father', 'collins',
                          'deceased', 'described', 'illiterate', 'miserly', 'father', 'subjection', 'father', 'brought',
                          'originally', 'given', 'great', 'humility', 'manner', 'characteristic', 'good', 'deal',
                          'counteracted', 'self', 'conceit', 'weak', 'head', 'replaced', 'arrogance', 'vanity', 'due',
                          'early', 'unexpected', 'prosperity', 'early', 'prosperity', 'come', 'chance', 'hands', 'lady',
                          'catherine', 'vacancy', 'arose', 'living', 'parish', 'respect', 'felt', 'high', 'rank',
                          'veneration', 'mingling', 'good', 'opinion', 'authority', 'clergyman', 'rights', 'rector',
                          'made', 'altogether', 'mixture', 'pride', 'obsequiousness', 'self', 'importance', 'humility',
                          'conceited', 'pompous', 'narrow', 'minded', 'silly', 'man', 'elizabeth', 'rejection',
                          'collins', 'marriage', 'proposal', 'welcomed', 'father', 'regardless', 'financial', 'benefit',
                          'family', 'match', 'collins', 'marries', 'elizabeth', 'friend', 'charlotte', 'lucas',
                          'collins', 'usually', 'considered', 'foil', 'darcy', 'grave', 'serious', 'acts', 'propriety',
                          'times', 'hand', 'collins', 'acts', 'impropriety', 'exaggerated', 'humility', 'offers',
                          'comedic', 'relief', 'lady', 'catherine', 'edit', 'lady', 'catherine', 'elizabeth', 'brock',
                          'lady', 'catherine', 'confronts', 'elizabeth', 'darcy', 'title', 'page', 'illustrated',
                          'edition', 'two', 'illustrations', 'novel', 'lady', 'catherine', 'fitzwilliam', 'daughter',
                          'sister', 'earl', 'widow', 'sir', 'lewis', 'knight', 'baronet', 'rosings', 'park', 'kent',
                          'daughter', 'miss', 'anne', 'possesses', 'wealth', 'social', 'standing', 'birth', 'marriage',
                          'haughty', 'pompous', 'domineering', 'condescending', 'manner', 'entirely', 'proper',
                          'admirable', 'collins', 'example', 'admire', 'characteristics', 'deferring', 'opinions',
                          'desires', 'likes', 'distinction', 'rank', 'preserved', 'elizabeth', 'contrast', 'duly',
                          'respectful', 'intimidated', 'lady', 'catherine', 'nephew', 'darcy', 'embarrassed', 'lack',
                          'manners', 'especially', 'elizabeth', 'later', 'courts', 'disapproval', 'marrying',
                          'elizabeth', 'spite', 'numerous', 'objections', 'lady', 'catherine', 'long', 'planned',
                          'marry', 'sickly', 'daughter', 'anne', 'darcy', 'unite', 'two', 'great', 'estates',
                          'claiming', 'dearest', 'wish', 'late', 'sister', 'lady', 'anne', 'darcy', 'fitzwilliam',
                          'gardiner', 'edit', 'gardiner', 'edward', 'gardiner', 'bennet', 'brother', 'successful',
                          'tradesman', 'sensible', 'gentlemanly', 'character', 'aunt', 'gardiner', 'name', 'revealed',
                          'hinted', 'letter', 'wrote', 'elizabeth', 'signs', 'gardiner', 'close', 'nieces', 'jane',
                          'elizabeth', 'jane', 'stays', 'gardiners', 'london', 'period', 'elizabeth', 'travels',
                          'derbyshire', 'meets', 'darcy', 'gardiners', 'quick', 'perception', 'attachment', 'elizabeth',
                          'darcy', 'judge', 'prejudice', 'actively', 'involved', 'helping', 'darcy', 'arrange',
                          'marriage', 'lydia', 'wickham', 'georgiana', 'darcy', 'edit', 'georgiana', 'darcy', 'darcy',
                          'quiet', 'amiable', 'shy', 'younger', 'sister', 'dowry', 'giving', 'additional', 'interest',
                          'annum', 'inheritance', 'aged', 'barely', 'years', 'old', 'story', 'begins', 'miss', 'darcy',
                          'eloped', 'wickham', 'made', 'believe', 'two', 'love', 'reality', 'sought', 'dowry', 'miss',
                          'darcy', 'introduced', 'elizabeth', 'later', 'delighted', 'prospect', 'sister', 'law',
                          'georgiana', 'extremely', 'timid', 'gets', 'embarrassed', 'fairly', 'easily', 'brother',
                          'darcy', 'fitzwilliam', 'darcy', 'two', 'share', 'extremely', 'close', 'sibling', 'bond',
                          'jane', 'elizabeth', 'thanks', 'years', 'tutorage', 'masters', 'accomplished', 'piano',
                          'singing', 'playing', 'harp', 'drawing', 'modern', 'languages', 'modest', 'charlotte',
                          'lucas', 'edit', 'charlotte', 'collins', 'lucas', 'elizabeth', 'friend', 'years', 'old',
                          'past', 'prime', 'marriage', 'age', 'fears', 'burden', 'family', 'agrees', 'marry', 'collins',
                          'love', 'merely', 'days', 'previously', 'proposed', 'elizabeth', 'gain', 'financial',
                          'security', 'novel', 'stresses', 'importance', 'love', 'understanding', 'marriage',
                          'anticipated', 'success', 'elizabeth', 'darcy', 'relationship', 'austen', 'condemn',
                          'charlotte', 'decision', 'marry', 'money', 'austen', 'uses', 'lucas', 'common', 'voice',
                          'early', 'century', 'society', 'views', 'relationships', 'marriage', 'austen', 'uses',
                          'charlotte', 'convey', 'women', 'time', 'adhere', 'society', 'expectation', 'women', 'marry',
                          'love', 'convenience', 'daughter', 'sir', 'william', 'lucas', 'lady', 'lucas', 'friends',
                          'bennet', 'louisa', 'hurst', 'edit', 'louisa', 'hurst', 'older', 'sister', 'caroline',
                          'charles', 'wife', 'hurst', 'coming', 'marriage', 'dowry', 'giving', 'additional', 'interest',
                          'annum', 'inheritance', 'described', 'novel', 'sister', 'fine', 'women', 'air', 'decided',
                          'fashion', 'disdainful', 'society', 'hertfordshire', 'louisa', 'caroline', 'behaviour',
                          'assembly', 'calculated', 'please', 'general', 'quickness', 'observation', 'temper', 'sister',
                          'judgment', 'unassailed', 'attention', 'disposed', 'approve', 'fact', 'fine', 'ladies',
                          'deficient', 'good', 'humour', 'pleased', 'power', 'agreeable', 'chose', 'proud', 'conceited',
                          'handsome', 'educated', 'private', 'seminaries', 'town', 'fortune', 'habit', 'spending',
                          'associating', 'people', 'rank', 'respect', 'entitled', 'think', 'respectable', 'family',
                          'north', 'england', 'circumstance', 'deeply', 'impressed', 'memories', 'brother', 'fortune',
                          'acquired', 'trade', 'arguably', 'nicer', 'two', 'sisters', 'caroline', 'encourage',
                          'brother', 'admiration', 'jane', 'bennet', 'lack', 'connections', 'placing', 'caroline',
                          'personal', 'chances', 'social', 'advancement', 'brother', 'happiness', 'conspired',
                          'caroline', 'darcy', 'keep', 'charles', 'jane', 'hurst', 'edit', 'hurst', 'husband', 'louisa',
                          'hurst', 'brother', 'law', 'charles', 'caroline', 'described', 'man', 'fashion', 'fortune',
                          'social', 'status', 'consequences', 'elaborated', 'background', 'originally', 'trade', 'wife',
                          'sufficiently', 'large', 'fortune', 'order', 'entice', 'miss', 'louisa', 'marrying',
                          'indolent', 'man', 'drunk', 'lives', 'eat', 'sleep', 'pass', 'drunk', 'drink', 'play',
                          'cards', 'hears', 'miss', 'elizabeth', 'bennet', 'say', 'preferred', 'plain', 'dish', 'fresh',
                          'fruit', 'heavily', 'seasoned', 'ragout', 'dish', 'say', 'philips', 'edit', 'philips',
                          'attorney', 'practice', 'lives', 'inherited', 'late', 'father', 'law', 'law', 'clerks',
                          'marrying', 'boss', 'daughter', 'philips', 'gardiner', 'sister', 'bennet', 'silly',
                          'unintelligent', 'gossip', 'sister', 'bennet', 'phillips', 'inherited', 'dowry', 'father',
                          'entertains', 'nieces', 'guests', 'parlour', 'husband', 'residence', 'interrelationships',
                          'edit', 'comprehensive', 'web', 'showing', 'relationships', 'main', 'characters', 'pride',
                          'prejudice', 'major', 'themes', 'edit', 'critics', 'take', 'novel', 'title', 'starting',
                          'point', 'analysing', 'major', 'themes', 'pride', 'prejudice', 'robert', 'fox', 'cautions',
                          'reading', 'title', 'commercial', 'factors', 'played', 'role', 'selection', 'success',
                          'sense', 'sensibility', 'natural', 'bring', 'novel', 'author', 'formula', 'antithesis',
                          'alliteration', 'title', 'pointed', 'qualities', 'title', 'exclusively', 'assigned',
                          'protagonists', 'elizabeth', 'darcy', 'display', 'pride', 'prejudice', 'title', 'likely',
                          'taken', 'passage', 'fanny', 'burney', 'popular', 'novel', 'cecilia', 'novel', 'austen',
                          'known', 'admired', 'unfortunate', 'business', 'lyster', 'result', 'pride', 'prejudice',
                          'remember', 'pride', 'prejudice', 'owe', 'miseries', 'wonderfully', 'good', 'evil',
                          'balanced', 'pride', 'prejudice', 'owe', 'termination', 'original', 'major', 'theme',
                          'austen', 'work', 'importance', 'environment', 'upbringing', 'development', 'young', 'people',
                          'character', 'morality', 'social', 'standing', 'wealth', 'necessarily', 'advantages', 'world',
                          'theme', 'common', 'austen', 'work', 'ineffectual', 'parents', 'pride', 'prejudice',
                          'failure', 'bennet', 'parents', 'blamed', 'lydia', 'lack', 'moral', 'judgment', 'darcy',
                          'hand', 'taught', 'principled', 'scrupulously', 'honourable', 'proud', 'overbearing', 'kitty',
                          'rescued', 'lydia', 'bad', 'influence', 'spending', 'time', 'older', 'sisters', 'marry',
                          'improve', 'greatly', 'superior', 'society', 'american', 'novelist', 'anna', 'quindlen',
                          'observed', 'introduction', 'edition', 'austen', 'novel', 'pride', 'prejudice', 'thing',
                          'great', 'novels', 'consider', 'search', 'self', 'great', 'novel', 'teaches', 'search',
                          'surely', 'undertaken', 'drawing', 'room', 'making', 'small', 'talk', 'pursuit', 'great',
                          'white', 'whale', 'public', 'punishment', 'adultery', 'marriage', 'edit', 'opening', 'line',
                          'novel', 'announces', 'truth', 'universally', 'acknowledged', 'single', 'man', 'possession',
                          'good', 'fortune', 'wife', 'sets', 'marriage', 'central', 'subject', 'central', 'problem',
                          'novel', 'generally', 'readers', 'poised', 'question', 'single', 'men', 'fact', 'wife',
                          'desires', 'dictated', 'neighborhood', 'families', 'daughters', 'require', 'good', 'fortune',
                          'marriage', 'complex', 'social', 'activity', 'takes', 'political', 'economy', 'economy',
                          'generally', 'account', 'case', 'charlotte', 'lucas', 'example', 'success', 'marriage',
                          'lies', 'comfortable', 'economy', 'household', 'relationship', 'bennet', 'serves',
                          'illustrate', 'bad', 'marriages', 'based', 'initial', 'attraction', 'surface', 'substance',
                          'economic', 'psychological', 'bennets', 'marriage', 'example', 'youngest', 'bennet', 'lydia',
                          'come', 'enact', 'wickham', 'results', 'felicitous', 'central', 'characters', 'elizabeth',
                          'darcy', 'begin', 'novel', 'hostile', 'acquaintances', 'unlikely', 'friends', 'eventually',
                          'work', 'understand', 'marry', 'compatible', 'terms', 'personally', 'equal', 'social',
                          'status', 'remains', 'fraught', 'elizabeth', 'rejects', 'darcy', 'proposal', 'argument',
                          'marrying', 'love', 'introduced', 'elizabeth', 'accepts', 'darcy', 'proposal', 'loves',
                          'feelings', 'reciprocated', 'austen', 'complex', 'sketching', 'different', 'marriages',
                          'ultimately', 'allows', 'readers', 'question', 'forms', 'alliance', 'desirable', 'especially',
                          'comes', 'privileging', 'economic', 'sexual', 'companionate', 'attraction', 'wealth', 'edit',
                          'money', 'plays', 'key', 'role', 'marriage', 'market', 'young', 'ladies', 'seeking',
                          'husband', 'men', 'wish', 'marry', 'woman', 'means', 'two', 'examples', 'george', 'wickham',
                          'tried', 'elope', 'georgiana', 'darcy', 'colonel', 'fitzwilliam', 'marrying', 'woman', 'rich',
                          'family', 'ensured', 'linkage', 'high', 'family', 'visible', 'desires', 'sisters', 'brother',
                          'married', 'georgiana', 'darcy', 'bennet', 'encouraging', 'daughters', 'marry', 'wealthy',
                          'man', 'high', 'social', 'class', 'example', 'chapter', 'arrives', 'says', 'thinking',
                          'marrying', 'inheritance', 'descent', 'restricted', 'entailment', 'restrict', 'inheritance',
                          'male', 'heirs', 'case', 'bennet', 'family', 'collins', 'inherit', 'family', 'farm', 'bennet',
                          'death', 'proposal', 'elizabeth', 'allowed', 'share', 'refused', 'offer', 'inheritance',
                          'laws', 'benefited', 'males', 'women', 'independent', 'legal', 'rights', 'second', 'half',
                          'century', 'consequence', 'women', 'financial', 'security', 'time', 'novel', 'set',
                          'depended', 'men', 'upper', 'middle', 'aristocratic', 'classes', 'marriage', 'man',
                          'reliable', 'income', 'route', 'security', 'woman', 'future', 'children', 'ironically',
                          'text', 'opens', 'line', 'truth', 'universally', 'acknowledged', 'single', 'man',
                          'possession', 'good', 'fortune', 'wife', 'ironic', 'generally', 'society', 'woman', 'looking',
                          'wealthy', 'husband', 'order', 'prosperous', 'life', 'class', 'edit', 'austen', 'known',
                          'romances', 'marriages', 'take', 'place', 'novels', 'engage', 'form', 'economic', 'concerns',
                          'involved', 'matches', 'pride', 'prejudice', 'darcy', 'proposes', 'elizabeth', 'cites',
                          'economic', 'social', 'differences', 'obstacle', 'excessive', 'love', 'overcome', 'anxiously',
                          'harps', 'problems', 'poses', 'social', 'circle', 'aunt', 'lady', 'catherine', 'later',
                          'characterizes', 'differences', 'particularly', 'harsh', 'terms', 'conveys', 'elizabeth',
                          'marriage', 'darcy', 'shades', 'polluted', 'elizabeth', 'responds', 'lady', 'catherine',
                          'accusations', 'potentially', 'contaminating', 'economic', 'social', 'position', 'elizabeth',
                          'insists', 'darcy', 'equals', 'lady', 'catherine', 'refuses', 'accept', 'darcy', 'actual',
                          'marriage', 'elizabeth', 'novel', 'closes', 'present', 'particular', 'problem', 'navigating',
                          'social', 'class', 'caroline', 'hurst', 'behave', 'speak', 'belonged', 'upper', 'echelons',
                          'society', 'austen', 'makes', 'point', 'explain', 'acquired', 'wealth', 'trade', 'gentry',
                          'aristocracy', 'methods', 'inheriting', 'estates', 'making', 'money', 'tenants', 'landlords',
                          'fact', 'rents', 'hall', 'distinguishes', 'significantly', 'darcy', 'estate', 'belonged',
                          'father', 'family', 'mother', 'grandson', 'nephew', 'earl', 'darcy', 'property', 'portable',
                          'growing', 'wealth', 'makes', 'good', 'catch', 'marriage', 'market', 'daughters', 'gentility',
                          'jane', 'bennet', 'social', 'status', 'good', 'family', 'require', 'money', 'stake', 'claim',
                          'quasi', 'aristocrats', 'class', 'plays', 'central', 'role', 'evolution', 'characters',
                          'jane', 'austen', 'radical', 'approach', 'class', 'plot', 'unfolds', 'addition',
                          'undercurrent', 'old', 'anglo', 'norman', 'upper', 'class', 'hinted', 'story', 'suggested',
                          'names', 'fitzwilliam', 'darcy', 'aunt', 'lady', 'catherine', 'fitzwilliam', 'burke',
                          'traditional', 'norman', 'surnames', 'self', 'knowledge', 'edit', 'elizabeth', 'darcy',
                          'born', 'great', 'match', 'interactions', 'critiques', 'recognise', 'faults', 'work',
                          'correct', 'elizabeth', 'meditates', 'mistakes', 'thoroughly', 'chapter', 'despicably',
                          'acted', 'cried', 'prided', 'discernment', 'valued', 'abilities', 'disdained', 'generous',
                          'sister', 'gratified', 'vanity', 'useless', 'distrust', 'humiliating', 'discovery',
                          'humiliation', 'love', 'wretchedly', 'blind', 'vanity', 'love', 'folly', 'pleased',
                          'preference', 'offended', 'neglect', 'beginning', 'acquaintance', 'courted', 'prepossession',
                          'ignorance', 'driven', 'reason', 'away', 'concerned', 'moment', 'knew', 'characters', 'type',
                          'self', 'reflection', 'capacity', 'experience', 'correct', 'tanner', 'essay', 'notes',
                          'bennet', 'particular', 'limited', 'view', 'requirements', 'performance', 'lacking',
                          'introspective', 'tendencies', 'incapable', 'appreciating', 'feelings', 'aware', 'material',
                          'objects', 'bennet', 'behaviour', 'reflects', 'society', 'lives', 'knows', 'daughters',
                          'succeed', 'married', 'business', 'life', 'daughters', 'married', 'solace', 'visiting',
                          'news', 'proves', 'bennet', 'aware', 'material', 'objects', 'feelings', 'emotions', 'style',
                          'edit', 'pride', 'prejudice', 'austen', 'works', 'employs', 'narrative', 'technique', 'free',
                          'indirect', 'speech', 'defined', 'free', 'representation', 'character', 'speech', 'means',
                          'words', 'actually', 'character', 'words', 'typify', 'character', 'thoughts', 'way',
                          'character', 'think', 'speak', 'thought', 'austen', 'creates', 'characters', 'fully',
                          'developed', 'personalities', 'unique', 'voices', 'darcy', 'bennet', 'alike', 'considerably',
                          'different', 'narrative', 'adopts', 'tone', 'vocabulary', 'particular', 'character', 'case',
                          'elizabeth', 'austen', 'invites', 'reader', 'follow', 'events', 'elizabeth', 'viewpoint',
                          'sharing', 'prejudices', 'misapprehensions', 'learning', 'curve', 'undergone', 'protagonists',
                          'disclosed', 'solely', 'elizabeth', 'point', 'view', 'free', 'indirect', 'speech',
                          'essential', 'remain', 'caught', 'stuck', 'elizabeth', 'misprisions', 'times', 'reader',
                          'allowed', 'gain', 'knowledge', 'character', 'feelings', 'letters', 'exchanged', 'novel',
                          'darcy', 'letter', 'elizabeth', 'example', 'letter', 'reader', 'elizabeth', 'given',
                          'knowledge', 'wickham', 'true', 'character', 'austen', 'known', 'irony', 'novel',
                          'especially', 'viewpoint', 'character', 'elizabeth', 'bennet', 'conveys', 'oppressive',
                          'rules', 'feminity', 'actually', 'dominate', 'life', 'work', 'covered', 'beautifully',
                          'carved', 'trojan', 'horse', 'ironic', 'distance', 'beginning', 'historical', 'investigation',
                          'development', 'particular', 'literary', 'form', 'transitioning', 'empirical',
                          'verifications', 'reveals', 'fid', 'tool', 'emerged', 'time', 'practical', 'means',
                          'addressing', 'physical', 'distinctness', 'minds', 'way', 'fid', 'distinctly', 'literary',
                          'response', 'environmental', 'concern', 'providing', 'scientific', 'justification', 'reduce',
                          'literature', 'mechanical', 'extension', 'biology', 'takes', 'value', 'original', 'form',
                          'development', 'novel', 'edit', 'page', 'letter', 'jane', 'austen', 'sister', 'cassandra',
                          'june', 'mentions', 'pride', 'prejudice', 'working', 'title', 'impressions', 'nla', 'austen',
                          'began', 'writing', 'novel', 'staying', 'park', 'kent', 'brother', 'edward', 'wife',
                          'originally', 'titled', 'impressions', 'written', 'october', 'august', 'november', 'austen',
                          'father', 'letter', 'london', 'bookseller', 'thomas', 'cadell', 'ask', 'interest',
                          'manuscript', 'offer', 'declined', 'return', 'post', 'austen', 'made', 'significant',
                          'revisions', 'manuscript', 'impressions', 'remains', 'original', 'manuscript', 'reduced',
                          'conjecture', 'large', 'number', 'letters', 'final', 'novel', 'assumed', 'impressions',
                          'epistolary', 'novel', 'later', 'renamed', 'story', 'pride', 'prejudice', 'renaming', 'novel',
                          'austen', 'probably', 'mind', 'sufferings', 'oppositions', 'final', 'chapter', 'fanny',
                          'burney', 'cecilia', 'called', 'pride', 'prejudice', 'phrase', 'appears', 'three', 'times',
                          'block', 'capitals', 'possible', 'novel', 'original', 'title', 'altered', 'avoid',
                          'confusion', 'works', 'years', 'completion', 'impressions', 'revision', 'pride', 'prejudice',
                          'two', 'works', 'published', 'name', 'novel', 'margaret', 'holford', 'comedy', 'horace',
                          'smith', 'publication', 'history', 'edit', 'title', 'page', 'edition', 'illustrated', 'brock',
                          'austen', 'sold', 'copyright', 'novel', 'thomas', 'egerton', 'military', 'library',
                          'whitehall', 'exchange', 'austen', 'asked', 'proved', 'costly', 'decision', 'austen',
                          'published', 'sense', 'sensibility', 'commission', 'basis', 'indemnified', 'publisher',
                          'losses', 'received', 'profits', 'costs', 'publisher', 'commission', 'unaware', 'sense',
                          'sensibility', 'sell', 'edition', 'making', 'passed', 'copyright', 'egerton', 'payment',
                          'meaning', 'risk', 'profits', 'jan', 'fergus', 'calculated', 'egerton', 'subsequently',
                          'made', 'two', 'editions', 'book', 'egerton', 'published', 'edition', 'pride', 'prejudice',
                          'three', 'hardcover', 'volumes', 'january', 'advertised', 'morning', 'chronicle', 'priced',
                          'favourable', 'reviews', 'edition', 'sold', 'second', 'edition', 'published', 'november',
                          'third', 'edition', 'published', 'foreign', 'language', 'translations', 'appeared', 'french',
                          'subsequent', 'translations', 'published', 'german', 'danish', 'swedish', 'pride',
                          'prejudice', 'published', 'united', 'states', 'august', 'elizabeth', 'bennet', 'pride',
                          'prejudice', 'novel', 'richard', 'bentley', 'standard', 'novel', 'series', 'chapman',
                          'scholarly', 'edition', 'pride', 'prejudice', 'published', 'standard', 'edition', 'modern',
                          'published', 'versions', 'novel', 'based', 'novel', 'originally', 'published', 'austen',
                          'name', 'written', 'author', 'sense', 'sensibility', 'carried', 'responsibility', 'austen',
                          'sense', 'sensibility', 'released', 'written', 'lady', 'reception', 'edit', 'main', 'article',
                          'reception', 'history', 'jane', 'austen', 'publication', 'edit', 'novel', 'received', 'three',
                          'favourable', 'reviews', 'months', 'following', 'publication', 'anne', 'isabella', 'milbanke',
                          'later', 'wife', 'lord', 'byron', 'called', 'fashionable', 'novel', 'noted', 'critic',
                          'reviewer', 'george', 'henry', 'lewes', 'declared', 'written', 'pride', 'prejudice', 'tom',
                          'jones', 'waverley', 'novels', 'charlotte', 'letter', 'lewes', 'wrote', 'pride', 'prejudice',
                          'disappointment', 'carefully', 'fenced', 'highly', 'cultivated', 'garden', 'neat', 'borders',
                          'delicate', 'flowers', 'open', 'country', 'fresh', 'air', 'blue', 'hill', 'bonny', 'beck',
                          'late', 'centuries', 'edit', 'shock', 'shocks', 'joyce', 'innocent', 'grass', 'makes',
                          'uncomfortable', 'english', 'spinster', 'middle', 'class', 'describe', 'amorous', 'effects',
                          'brass', 'reveal', 'frankly', 'sobriety', 'economic', 'basis', 'society', 'auden', 'austen',
                          'bbc', 'conducted', 'poll', 'best', 'loved', 'book', 'pride', 'prejudice', 'came', 'second',
                          'lord', 'rings', 'survey', 'australian', 'readers', 'pride', 'prejudice', 'came', 'list',
                          'best', 'books', 'written', 'anniversary', 'pride', 'prejudice', 'january', 'celebrated',
                          'globe', 'media', 'networks', 'huffington', 'post', 'new', 'york', 'times', 'daily',
                          'telegraph', 'adaptations', 'edit', 'film', 'television', 'theatre', 'edit', 'jane', 'austen',
                          'popular', 'culture', 'pride', 'prejudice', 'pride', 'prejudice', 'engendered', 'numerous',
                          'adaptations', 'notable', 'film', 'versions', 'starring', 'greer', 'garson', 'laurence',
                          'olivier', 'based', 'part', 'helen', 'jerome', 'stage', 'adaptation', 'starring', 'knightley',
                          'oscar', 'nominated', 'performance', 'matthew', 'macfadyen', 'notable', 'television',
                          'versions', 'two', 'bbc', 'version', 'starring', 'elizabeth', 'david', 'popular', 'version',
                          'starring', 'jennifer', 'ehle', 'colin', 'firth', 'stage', 'version', 'created', 'helen',
                          'jerome', 'played', 'james', 'theatre', 'london', 'starring', 'celia', 'johnson', 'hugh',
                          'williams', 'impressions', 'broadway', 'musical', 'version', 'starring', 'polly', 'bergen',
                          'farley', 'granger', 'hermione', 'gingold', 'musical', 'concept', 'album', 'written',
                          'bernard', 'taylor', 'claire', 'moore', 'role', 'elizabeth', 'bennet', 'peter', 'karrie',
                          'role', 'darcy', 'new', 'stage', 'production', 'jane', 'austen', 'pride', 'prejudice', 'new',
                          'musical', 'presented', 'concert', 'october', 'rochester', 'new', 'york', 'colin', 'donnell',
                          'darcy', 'literature', 'edit', 'main', 'article', 'list', 'literary', 'adaptations', 'pride',
                          'prejudice', 'novel', 'inspired', 'number', 'works', 'direct', 'adaptations', 'books',
                          'inspired', 'pride', 'prejudice', 'following', 'darcy', 'daughters', 'exploits', 'adventures',
                          'miss', 'alethea', 'darcy', 'elizabeth', 'aston', 'darcy', 'story', 'best', 'seller',
                          'dialogue', 'darcy', 'janet', 'aylmer', 'pride', 'prejudice', 'continued', 'unequal',
                          'marriage', 'pride', 'prejudice', 'twenty', 'years', 'later', 'emma', 'tennant', 'book',
                          'ruth', 'helen', 'baker', 'author', 'jane', 'austen', 'ruined', 'life', 'darcy', 'broke',
                          'heart', 'beth', 'precipitation', 'continuation', 'miss', 'jane', 'austen', 'pride',
                          'prejudice', 'helen', 'baker', 'author', 'searching', 'mary', 'simonsen', 'darcy', 'takes',
                          'wife', 'sequel', 'darcy', 'elizabeth', 'nights', 'days', 'linda', 'gwyn', 'comedic',
                          'romance', 'novel', 'seducing', 'darcy', 'heroine', 'lands', 'pride', 'prejudice', 'way',
                          'magic', 'massage', 'fling', 'darcy', 'unknowingly', 'changes', 'rest', 'story', 'abigail',
                          'reynolds', 'author', 'regency', 'set', 'variations', 'pride', 'prejudice', 'variations',
                          'series', 'includes', 'darcy', 'obsession', 'conquer', 'darcy', 'darcy', 'fitzwilliam',
                          'darcy', 'man', 'world', 'modern', 'adaptation', 'man', 'loved', 'pride', 'prejudice', 'set',
                          'cape', 'cod', 'helen', 'fielding', 'novel', 'bridget', 'jones', 'diary', 'based', 'pride',
                          'prejudice', 'spawned', 'feature', 'film', 'name', 'released', 'march', 'quirk', 'books',
                          'released', 'pride', 'prejudice', 'zombies', 'takes', 'austen', 'actual', 'original', 'work',
                          'mashes', 'zombie', 'hordes', 'cannibalism', 'ninja', 'ultraviolent', 'mayhem', 'march',
                          'quirk', 'books', 'published', 'prequel', 'deals', 'elizabeth', 'bennet', 'early', 'days',
                          'zombie', 'hunter', 'pride', 'prejudice', 'zombies', 'dawn', 'dreadfuls', 'movie',
                          'aforementioned', 'contemporary', 'literature', 'adaptation', 'released', 'starring', 'lily',
                          'james', 'matt', 'smith', 'author', 'mitzi', 'expanded', 'novel', 'pride', 'prejudice',
                          'hidden', 'lusts', 'historical', 'sex', 'parody', 'parallels', 'original', 'plot', 'writing',
                          'style', 'jane', 'austen', 'marvel', 'published', 'take', 'classic', 'releasing', 'short',
                          'comic', 'series', 'five', 'issues', 'stays', 'true', 'original', 'storyline', 'issue',
                          'published', 'april', 'written', 'nancy', 'published', 'graphic', 'novel', 'artwork', 'hugo',
                          'petrus', 'pamela', 'aidan', 'author', 'trilogy', 'books', 'telling', 'story', 'pride',
                          'prejudice', 'darcy', 'point', 'view', 'fitzwilliam', 'darcy', 'gentleman', 'books',
                          'assembly', 'duty', 'desire', 'three', 'remain', 'detective', 'novel', 'author', 'james',
                          'written', 'book', 'titled', 'death', 'comes', 'murder', 'mystery', 'set', 'six', 'years',
                          'elizabeth', 'darcy', 'marriage', 'sandra', 'lerner', 'sequel', 'pride', 'prejudice',
                          'second', 'impressions', 'develops', 'story', 'imagined', 'happened', 'original', 'novel',
                          'characters', 'written', 'style', 'austen', 'extensive', 'research', 'period', 'language',
                          'published', 'pen', 'name', 'ava', 'farmer', 'baker', 'novel', 'imagines', 'lives',
                          'servants', 'pride', 'prejudice', 'curtis', 'set', 'characters', 'pride', 'prejudice',
                          'modern', 'cincinnati', 'bennet', 'parents', 'erstwhile', 'cincinnati', 'social', 'climbers',
                          'fallen', 'hard', 'times', 'elizabeth', 'successful', 'independent', 'new', 'york',
                          'journalist', 'single', 'older', 'sister', 'jane', 'intervene', 'salvage', 'family',
                          'financial', 'situation', 'unemployed', 'adult', 'sisters', 'move', 'house', 'onward', 'life',
                          'process', 'encounter', 'chip', 'young', 'doctor', 'reluctant', 'reality', 'celebrity',
                          'medical', 'school', 'classmate', 'fitzwilliam', 'darcy', 'cynical', 'neurosurgeon', 'pride',
                          'prejudice', 'inspired', 'works', 'scientific', 'writing', 'scientists', 'named', 'pheromone',
                          'identified', 'male', 'mouse', 'urine', 'darcy', 'strongly', 'attracted', 'females',
                          'scientific', 'paper', 'published', 'journal', 'inherited', 'metabolic', 'diseases',
                          'speculated', 'bennet', 'carrier', 'rare', 'genetic', 'disease', 'explaining', 'bennets',
                          'sons', 'bennet', 'sisters', 'silly']

        self.other_unigrams = ['Modern', 'humans', '(Homo', 'sapiens,', 'primarily', 'ssp.', 'Homo', 'sapiens',
                               'sapiens)', 'are', 'the', 'only', 'extant', 'members', 'of', 'Hominina', 'tribe', '(or',
                               'human', 'tribe),', 'a', 'branch', 'of', 'the', 'tribe', 'Hominini', 'belonging', 'to',
                               'the', 'family', 'of', 'great', 'apes.', 'They', 'are', 'characterized', 'by', 'erect',
                               'posture', 'and', 'bipedal', 'locomotion;', 'manual', 'dexterity', 'and', 'increased',
                               'tool', 'use,', 'compared', 'to', 'other', 'animals;', 'and', 'a', 'general', 'trend',
                               'toward', 'larger,', 'more', 'complex', 'brains', 'and', 'societies.\nEarly',
                               'hominins—particularly', 'the', 'australopithecines,', 'whose', 'brains', 'and',
                               'anatomy', 'are', 'in', 'many', 'ways', 'more', 'similar', 'to', 'ancestral',
                               'non-human', 'apes—are', 'less', 'often', 'referred', 'to', 'as', '"human"', 'than',
                               'hominins', 'of', 'the', 'genus', 'Homo.', 'Several', 'of', 'these', 'hominins', 'used',
                               'fire,', 'occupied', 'much', 'of', 'Eurasia,', 'and', 'gave', 'rise', 'to',
                               'anatomically', 'modern', 'Homo', 'sapiens', 'in', 'Africa', 'about', '200,000', 'years',
                               'ago.', 'They', 'began', 'to', 'exhibit', 'evidence', 'of', 'behavioral', 'modernity',
                               'around', '50,000', 'years', 'ago.', 'In', 'several', 'waves', 'of', 'migration,',
                               'anatomically', 'modern', 'humans', 'ventured', 'out', 'of', 'Africa', 'and',
                               'populated', 'most', 'of', 'the', 'world.\nThe', 'spread', 'of', 'humans', 'and',
                               'their', 'large', 'and', 'increasing', 'population', 'has', 'had', 'a', 'profound',
                               'impact', 'on', 'large', 'areas', 'of', 'the', 'environment', 'and', 'millions', 'of',
                               'native', 'species', 'worldwide.', 'Advantages', 'that', 'explain', 'this',
                               'evolutionary', 'success', 'include', 'a', 'relatively', 'larger', 'brain', 'with', 'a',
                               'particularly', 'well-developed', 'neocortex,', 'prefrontal', 'cortex', 'and',
                               'temporal', 'lobes,', 'which', 'enable', 'high', 'levels', 'of', 'abstract',
                               'reasoning,', 'language,', 'problem', 'solving,', 'sociality,', 'and', 'culture',
                               'through', 'social', 'learning.', 'Humans', 'use', 'tools', 'to', 'a', 'much', 'higher',
                               'degree', 'than', 'any', 'other', 'animal,', 'are', 'the', 'only', 'extant', 'species',
                               'known', 'to', 'build', 'fires', 'and', 'cook', 'their', 'food,', 'and', 'are', 'the',
                               'only', 'extant', 'species', 'to', 'clothe', 'themselves', 'and', 'create', 'and', 'use',
                               'numerous', 'other', 'technologies', 'and', 'arts.\nHumans', 'are', 'uniquely', 'adept',
                               'at', 'utilizing', 'systems', 'of', 'symbolic', 'communication', '(such', 'as',
                               'language', 'and', 'art)', 'for', 'self-expression', 'and', 'the', 'exchange', 'of',
                               'ideas,', 'and', 'for', 'organizing', 'themselves', 'into', 'purposeful', 'groups.',
                               'Humans', 'create', 'complex', 'social', 'structures', 'composed', 'of', 'many',
                               'cooperating', 'and', 'competing', 'groups,', 'from', 'families', 'and', 'kinship',
                               'networks', 'to', 'political', 'states.', 'Social', 'interactions', 'between', 'humans',
                               'have', 'established', 'an', 'extremely', 'wide', 'variety', 'of', 'values,', 'social',
                               'norms,', 'and', 'rituals,', 'which', 'together', 'form', 'the', 'basis', 'of', 'human',
                               'society.', 'Curiosity', 'and', 'the', 'human', 'desire', 'to', 'understand', 'and',
                               'influence', 'the', 'environment', 'and', 'to', 'explain', 'and', 'manipulate',
                               'phenomena', '(or', 'events)', 'has', 'provided', 'the', 'foundation', 'for',
                               'developing', 'science,', 'philosophy,', 'mythology,', 'religion,', 'anthropology,',
                               'and', 'numerous', 'other', 'fields', 'of', 'knowledge.\nThough', 'most', 'of', 'human',
                               'existence', 'has', 'been', 'sustained', 'by', 'hunting', 'and', 'gathering', 'in',
                               'band', 'societies,', 'increasing', 'numbers', 'of', 'human', 'societies', 'began', 'to',
                               'practice', 'sedentary', 'agriculture', 'approximately', 'some', '10,000', 'years',
                               'ago,', 'domesticating', 'plants', 'and', 'animals,', 'thus', 'allowing', 'for', 'the',
                               'growth', 'of', 'civilization.', 'These', 'human', 'societies', 'subsequently',
                               'expanded', 'in', 'size,', 'establishing', 'various', 'forms', 'of', 'government,',
                               'religion,', 'and', 'culture', 'around', 'the', 'world,', 'unifying', 'people', 'within',
                               'regions', 'to', 'form', 'states', 'and', 'empires.', 'The', 'rapid', 'advancement',
                               'of', 'scientific', 'and', 'medical', 'understanding', 'in', 'the', '19th', 'and',
                               '20th', 'centuries', 'led', 'to', 'the', 'development', 'of', 'fuel-driven',
                               'technologies', 'and', 'increased', 'lifespans,', 'causing', 'the', 'human',
                               'population', 'to', 'rise', 'exponentially.', 'Today', 'the', 'global', 'human',
                               'population', 'is', 'estimated', 'by', 'the', 'United', 'Nations', 'to', 'be', 'near',
                               '7.5', 'billion.']

        self.significant_neighbors_wiki = [{'reasoning', 'motive', 'reason', 'factors', 'justification'},
                                           {'explaining', 'experience', 'knowledge', 'learn', 'understand'},
                                           {'folly', 'magic', 'conceit', 'clever', 'marvel'},
                                           {'sickly', 'hurting', 'poor', 'bad', 'low'},
                                           {'restricted', 'restrict', 'lack', 'insufficient', 'reduced'},
                                           {'musical', 'piano', 'singing', 'music', 'dances'},
                                           {'keep', 'unnecessary', 'reduce', 'overcome', 'dissuade'},
                                           {'rejects', 'accept', 'objections', 'disapproval', 'failure'},
                                           {'storyline', 'article', 'stories', 'diary', 'tales', 'memoir', 'narrative'},
                                           {'imperative', 'required', 'key', 'necessity', 'advantages', 'stresses',
                                            'role', 'desirable'},
                                           {'days', 'times', 'time', 'months', 'nights', 'years', 'twice', 'past'},
                                           {'born', 'lives', 'rescued', 'lived', 'death', 'staying', 'life',
                                            'deceased'}, {'resulted', 'came', 'began', 'broke', 'end'},
                                           {'educated', 'learning', 'learn', 'teaches', 'classes'},
                                           {'generally', 'simply', 'actually', 'natural', 'usually'},
                                           {'viewpoint', 'views', 'picture', 'opinion', 'perception'},
                                           {'haste', 'quick', 'unnecessary', 'illogical', 'cynical'},
                                           {'dictated', 'despite', 'changes', 'aided', 'support', 'benefited',
                                            'welcomed', 'counteracted', 'different', 'grateful', 'led', 'ensured',
                                            'altering', 'influenced'}, {'join', 'speak', 'meet', 'miss', 'invited'},
                                           {'duly', 'merely', 'equally', 'strongly', 'sufficiently'},
                                           {'zombies', 'greedy', 'lord', 'morality', 'oppressive'},
                                           {'humiliation', 'burden', 'miseries', 'problems', 'pain', 'hardship',
                                            'families', 'sufferings'},
                                           {'carried', 'conducted', 'pointed', 'undergone', 'taken', 'undertaken',
                                            'done', 'brought'}, {'going', 'transpires', 'unfolding', 'know', 'done'},
                                           {'disapproves', 'poll', 'disapproval', 'approve', 'dislike'},
                                           {'described', 'characterizes', 'describes', 'perceived', 'depiction'},
                                           {'expanded', 'significantly', 'improved', 'reduce', 'limited'},
                                           {'economic', 'wealthy', 'economy', 'rich', 'happiness', 'prosperous',
                                            'income', 'wealth'},
                                           {'argument', 'proof', 'case', 'empirical', 'justification'},
                                           {'sell', 'buying', 'sold', 'purchase', 'leasing'},
                                           {'inheritance', 'father', 'patriarch', 'manor', 'property', 'grandson',
                                            'estate', 'heirs'},
                                           {'pleasures', 'activities', 'pastimes', 'pursuits', 'socializing', 'pursuit',
                                            'happiness', 'conceit', 'sport', 'adventures'},
                                           {'adhere', 'following', 'come', 'follows', 'followed'},
                                           {'dramatic', 'significant', 'key', 'memorable', 'major'},
                                           {'trait', 'qualities', 'characteristic', 'tendency', 'tendencies',
                                            'prejudices', 'characteristics'},
                                           {'works', 'work', 'looking', 'trying', 'helping'},
                                           {'obsession', 'desires', 'arrogance', 'desire', 'intention'},
                                           {'love', 'dislike', 'loves', 'pleasing', 'preference'},
                                           {'completion', 'comprehensive', 'significant', 'numerous', 'entire',
                                            'detailed', 'experience', 'begin'},
                                           {'laws', 'policy', 'code', 'requirements', 'law', 'courts', 'rules',
                                            'legal'}, {'variations', 'revision', 'altering', 'revisions', 'altered'},
                                           {'merely', 'true', 'real', 'serious', 'great'},
                                           {'proposed', 'promised', 'decided', 'plans', 'anticipated'},
                                           {'reasoning', 'judge', 'decision', 'opinion', 'judgments'},
                                           {'responsibility', 'consequence', 'problems', 'effects', 'risk'},
                                           {'remain', 'keep', 'leaving', 'stays', 'remains', 'continue', 'staying',
                                            'living'}, {'sweeter', 'harsh', 'better', 'nicer', 'respectful'},
                                           {'beautifully', 'heavily', 'closely', 'scrupulously', 'thoroughly'},
                                           {'rents', 'sold', 'house', 'residence', 'lived'},
                                           {'experienced', 'successful', 'accomplishment', 'done', 'accomplishments'},
                                           {'join', 'encourage', 'engaged', 'involved', 'intervene'},
                                           {'generally', 'equally', 'alike', 'highly', 'insufficiently'},
                                           {'hordes', 'evil', 'ninja', 'characters', 'zombie'},
                                           {'decorum', 'political', 'morality', 'impropriety', 'principled', 'decency',
                                            'rectitude'}, {'found', 'search', 'find', 'looking', 'seeking'},
                                           {'ask', 'darcy', 'lord', 'lizzy', 'gentleman'},
                                           {'came', 'appeared', 'arose', 'revealed', 'arrived'},
                                           {'concern', 'concerns', 'hopes', 'fury', 'objections'},
                                           {'going', 'coming', 'begin', 'begins', 'beginning'},
                                           {'declared', 'identified', 'renamed', 'nominated', 'known'},
                                           {'goes', 'uses', 'work', 'teaches', 'working'},
                                           {'allows', 'allowed', 'aided', 'helping', 'managed'},
                                           {'ironically', 'surely', 'proved', 'considered', 'probably'},
                                           {'phrase', 'alliteration', 'language', 'abilities', 'words'},
                                           {'generous', 'poor', 'greedy', 'respectable', 'modest'},
                                           {'thought', 'believed', 'claimed', 'accepted', 'speculated'},
                                           {'approach', 'tool', 'method', 'ways', 'technique'},
                                           {'admiration', 'obsequiousness', 'affection', 'fascination', 'esteem'},
                                           {'genuine', 'actually', 'real', 'reality', 'truth'},
                                           {'publication', 'version', 'editions', 'published', 'article'},
                                           {'scientists', 'research', 'scholarly', 'empirical', 'biology'},
                                           {'attorney', 'case', 'sentence', 'judgment', 'courts'},
                                           {'bit', 'actually', 'significantly', 'greatly', 'slightly'},
                                           {'sex', 'marriage', 'unmarried', 'morality', 'marriages'},
                                           {'folly', 'arrogance', 'insolence', 'ignorance', 'rectitude'},
                                           {'celebrity', 'character', 'qualities', 'characters', 'protagonists'},
                                           {'novels', 'adaptation', 'translations', 'characters', 'sequel'},
                                           {'position', 'problem', 'problems', 'circumstance', 'matters'},
                                           {'unintelligent', 'sensible', 'minded', 'witty', 'clever'},
                                           {'stating', 'message', 'letters', 'statement', 'dated'},
                                           {'asked', 'refuses', 'fallen', 'specify', 'refused'},
                                           {'information', 'disclosed', 'detailed', 'specify', 'detail'},
                                           {'minimum', 'required', 'require', 'standard', 'rules'},
                                           {'shows', 'suggesting', 'show', 'reveals', 'display'},
                                           {'turn', 'came', 'put', 'brought', 'moved'},
                                           {'repeatedly', 'subsequently', 'recently', 'initially', 'originally'},
                                           {'conquer', 'join', 'uniting', 'united', 'bring'},
                                           {'goes', 'learns', 'unfolds', 'comes', 'happened'}]

        self.significant_neighbors_wiki_index = {0: {'reason', 'motive', 'factors', 'justification', 'reasoning'},
                                                 1: {'learn', 'experience', 'understand', 'knowledge', 'explaining'},
                                                 2: {'conceit', 'magic', 'folly', 'clever', 'marvel'},
                                                 3: {'sickly', 'low', 'hurting', 'bad', 'poor'},
                                                 4: {'restrict', 'restricted', 'lack', 'insufficient', 'reduced'},
                                                 5: {'music', 'piano', 'singing', 'musical', 'dances'},
                                                 6: {'unnecessary', 'reduce', 'dissuade', 'overcome', 'keep'},
                                                 7: {'objections', 'disapproval', 'failure', 'rejects', 'accept'},
                                                 8: {'diary', 'narrative', 'stories', 'tales', 'storyline', 'memoir',
                                                     'article'},
                                                 9: {'required', 'advantages', 'imperative', 'role', 'necessity', 'key',
                                                     'stresses', 'desirable'},
                                                 10: {'time', 'times', 'past', 'years', 'days', 'twice', 'nights',
                                                      'months'},
                                                 11: {'deceased', 'life', 'rescued', 'staying', 'death', 'lives',
                                                      'born', 'lived'},
                                                 12: {'began', 'end', 'resulted', 'broke', 'came'},
                                                 13: {'learning', 'teaches', 'classes', 'learn', 'educated'},
                                                 14: {'actually', 'usually', 'generally', 'simply', 'natural'},
                                                 15: {'opinion', 'picture', 'views', 'perception', 'viewpoint'},
                                                 16: {'unnecessary', 'haste', 'quick', 'cynical', 'illogical'},
                                                 17: {'influenced', 'despite', 'altering', 'benefited', 'dictated',
                                                      'aided', 'grateful', 'counteracted', 'support', 'different',
                                                      'changes', 'led', 'ensured', 'welcomed'},
                                                 18: {'invited', 'join', 'miss', 'meet', 'speak'},
                                                 19: {'sufficiently', 'strongly', 'equally', 'merely', 'duly'},
                                                 20: {'morality', 'greedy', 'lord', 'oppressive', 'zombies'},
                                                 21: {'burden', 'pain', 'miseries', 'hardship', 'sufferings',
                                                      'problems', 'families', 'humiliation'},
                                                 22: {'taken', 'carried', 'undergone', 'pointed', 'undertaken', 'done',
                                                      'conducted', 'brought'},
                                                 23: {'know', 'transpires', 'unfolding', 'going', 'done'},
                                                 24: {'disapproval', 'poll', 'approve', 'disapproves', 'dislike'},
                                                 25: {'depiction', 'describes', 'described', 'perceived',
                                                      'characterizes'},
                                                 26: {'reduce', 'improved', 'limited', 'significantly', 'expanded'},
                                                 27: {'economy', 'income', 'prosperous', 'economic', 'rich', 'wealth',
                                                      'happiness', 'wealthy'},
                                                 28: {'empirical', 'justification', 'argument', 'proof', 'case'},
                                                 29: {'leasing', 'sell', 'buying', 'purchase', 'sold'},
                                                 30: {'grandson', 'heirs', 'estate', 'manor', 'patriarch', 'property',
                                                      'father', 'inheritance'},
                                                 31: {'conceit', 'pastimes', 'sport', 'socializing', 'pleasures',
                                                      'pursuit', 'adventures', 'activities', 'happiness', 'pursuits'},
                                                 32: {'followed', 'following', 'come', 'adhere', 'follows'},
                                                 33: {'memorable', 'dramatic', 'significant', 'key', 'major'},
                                                 34: {'qualities', 'prejudices', 'characteristics', 'characteristic',
                                                      'trait', 'tendency', 'tendencies'},
                                                 35: {'helping', 'work', 'trying', 'works', 'looking'},
                                                 36: {'intention', 'desires', 'desire', 'arrogance', 'obsession'},
                                                 37: {'loves', 'pleasing', 'love', 'preference', 'dislike'},
                                                 38: {'experience', 'numerous', 'detailed', 'comprehensive',
                                                      'significant', 'entire', 'completion', 'begin'},
                                                 39: {'law', 'rules', 'code', 'courts', 'requirements', 'legal', 'laws',
                                                      'policy'},
                                                 40: {'altering', 'variations', 'revisions', 'altered', 'revision'},
                                                 41: {'real', 'serious', 'great', 'true', 'merely'},
                                                 42: {'decided', 'promised', 'proposed', 'anticipated', 'plans'},
                                                 43: {'judge', 'decision', 'judgments', 'opinion', 'reasoning'},
                                                 44: {'responsibility', 'risk', 'problems', 'consequence', 'effects'},
                                                 45: {'remains', 'continue', 'stays', 'remain', 'living', 'staying',
                                                      'leaving', 'keep'},
                                                 46: {'better', 'harsh', 'sweeter', 'respectful', 'nicer'},
                                                 47: {'thoroughly', 'scrupulously', 'beautifully', 'heavily',
                                                      'closely'}, 48: {'house', 'residence', 'rents', 'sold', 'lived'},
                                                 49: {'successful', 'accomplishment', 'accomplishments', 'done',
                                                      'experienced'},
                                                 50: {'intervene', 'encourage', 'join', 'engaged', 'involved'},
                                                 51: {'alike', 'generally', 'highly', 'insufficiently', 'equally'},
                                                 52: {'hordes', 'ninja', 'zombie', 'characters', 'evil'},
                                                 53: {'morality', 'rectitude', 'principled', 'decency', 'political',
                                                      'impropriety', 'decorum'},
                                                 54: {'seeking', 'search', 'find', 'found', 'looking'},
                                                 55: {'gentleman', 'lizzy', 'darcy', 'ask', 'lord'},
                                                 56: {'appeared', 'revealed', 'arose', 'came', 'arrived'},
                                                 57: {'hopes', 'concern', 'objections', 'fury', 'concerns'},
                                                 58: {'begins', 'beginning', 'coming', 'going', 'begin'},
                                                 59: {'declared', 'nominated', 'renamed', 'known', 'identified'},
                                                 60: {'uses', 'teaches', 'work', 'working', 'goes'},
                                                 61: {'allows', 'allowed', 'helping', 'aided', 'managed'},
                                                 62: {'surely', 'proved', 'ironically', 'considered', 'probably'},
                                                 63: {'words', 'abilities', 'phrase', 'alliteration', 'language'},
                                                 64: {'respectable', 'greedy', 'modest', 'generous', 'poor'},
                                                 65: {'speculated', 'believed', 'claimed', 'thought', 'accepted'},
                                                 66: {'approach', 'ways', 'method', 'technique', 'tool'},
                                                 67: {'obsequiousness', 'fascination', 'esteem', 'affection',
                                                      'admiration'},
                                                 68: {'actually', 'genuine', 'real', 'reality', 'truth'},
                                                 69: {'publication', 'published', 'article', 'editions', 'version'},
                                                 70: {'biology', 'research', 'empirical', 'scholarly', 'scientists'},
                                                 71: {'judgment', 'case', 'sentence', 'courts', 'attorney'},
                                                 72: {'actually', 'slightly', 'significantly', 'greatly', 'bit'},
                                                 73: {'marriages', 'morality', 'unmarried', 'sex', 'marriage'},
                                                 74: {'rectitude', 'folly', 'insolence', 'arrogance', 'ignorance'},
                                                 75: {'qualities', 'protagonists', 'celebrity', 'character',
                                                      'characters'},
                                                 76: {'sequel', 'adaptation', 'translations', 'novels', 'characters'},
                                                 77: {'problem', 'circumstance', 'matters', 'position', 'problems'},
                                                 78: {'sensible', 'minded', 'witty', 'clever', 'unintelligent'},
                                                 79: {'message', 'letters', 'statement', 'dated', 'stating'},
                                                 80: {'refuses', 'refused', 'fallen', 'asked', 'specify'},
                                                 81: {'information', 'detailed', 'disclosed', 'specify', 'detail'},
                                                 82: {'required', 'standard', 'require', 'minimum', 'rules'},
                                                 83: {'shows', 'display', 'reveals', 'show', 'suggesting'},
                                                 84: {'turn', 'put', 'moved', 'came', 'brought'},
                                                 85: {'subsequently', 'originally', 'recently', 'initially',
                                                      'repeatedly'},
                                                 86: {'uniting', 'united', 'conquer', 'join', 'bring'},
                                                 87: {'comes', 'unfolds', 'happened', 'goes', 'learns'}}

        self.significant_neighbors_weight = {0: 1.8937247285994858, 1: 1.7199366352869319, 2: 3.4570164916518578,
                                             3: 2.0314520776586873, 4: 1.7706842787592225, 5: 2.1195292237387457,
                                             6: 2.1850026150569617, 7: 1.7975316298254298, 8: 2.949700209718181,
                                             9: 1.9927229144180862, 10: 0.86472311759828502, 11: 1.5278866807058789,
                                             12: 1.0667467559477213, 13: 1.6186878178287194, 14: 1.4460918977035817,
                                             15: 2.1027277398046342, 16: 3.0135018013682227, 17: 1.7455375178526558,
                                             18: 1.3763064995384275, 19: 2.4225723165787469, 20: 2.9787298788792937,
                                             21: 2.0574074127071276, 22: 1.6348764267493465, 23: 2.0466286814664665,
                                             24: 2.4178529290839679, 25: 2.0242827909113452, 26: 1.5856917220679265,
                                             27: 1.944470357571036, 28: 2.1302056847799724, 29: 1.5562824993490156,
                                             30: 2.5515855459287833, 31: 2.5801563428761298, 32: 1.2754955709500986,
                                             33: 1.7671996874027147, 34: 2.7531760337817244, 35: 0.82399551496965295,
                                             36: 2.3799025608423694, 37: 2.0764989830657825, 38: 1.616081874740976,
                                             39: 1.1926940604742811, 40: 2.3114541345872732, 41: 1.6347605634767493,
                                             42: 1.2878626070626698, 43: 1.4910329693819828, 44: 1.4063033176086415,
                                             45: 1.0620522032605224, 46: 2.6843232828564121, 47: 2.6287865853968069,
                                             48: 1.3418233192275899, 49: 1.8864027929491669, 50: 1.6103381835326629,
                                             51: 1.9871188035311202, 52: 3.359073500297634, 53: 2.9757946898939012,
                                             54: 1.142907299637085, 55: 3.8017844478907095, 56: 1.6009982529514235,
                                             57: 1.6697480097261181, 58: 1.0195250181812443, 59: 1.6999132728382196,
                                             60: 1.4028296492231784, 61: 0.99095981854176274, 62: 1.5698487658446745,
                                             63: 2.6899048611350174, 64: 1.9435087641856974, 65: 1.2474574760013515,
                                             66: 1.8258601568078046, 67: 3.0325759240195507, 68: 2.0156028105241646,
                                             69: 1.6146667706585078, 70: 2.4653947041548014, 71: 1.343206484324142,
                                             72: 2.0189600313325906, 73: 2.4305901607204641, 74: 3.528690941714558,
                                             75: 2.3535702078667597, 76: 2.5763514512456465, 77: 1.3073346181218133,
                                             78: 3.2241826916396548, 79: 1.1902469564427711, 80: 1.519462984916895,
                                             81: 1.5646536577813435, 82: 1.3665297224378843, 83: 1.3538101384670755,
                                             84: 1.0400374033544608, 85: 1.5804391015733099, 86: 1.401698655104568,
                                             87: 1.7022629887297538}

        self.sorted_significant_neighbors = [({'darcy', 'lord', 'lizzy', 'ask', 'gentleman'}, 3.8017844478907095),
                                             ({'ignorance', 'arrogance', 'insolence', 'folly', 'rectitude'},
                                              3.528690941714558),
                                             ({'clever', 'marvel', 'magic', 'folly', 'conceit'}, 3.4570164916518578),
                                             ({'zombie', 'evil', 'characters', 'ninja', 'hordes'}, 3.359073500297634), (
                                                 {'clever', 'sensible', 'unintelligent', 'witty', 'minded'},
                                                 3.2241826916396548), (
                                                 {'esteem', 'affection', 'obsequiousness', 'fascination', 'admiration'},
                                                 3.0325759240195507), (
                                                 {'cynical', 'quick', 'unnecessary', 'illogical', 'haste'},
                                                 3.0135018013682227), (
                                                 {'greedy', 'lord', 'zombies', 'oppressive', 'morality'},
                                                 2.9787298788792937), (
                                                 {'political', 'principled', 'decency', 'morality', 'impropriety',
                                                  'rectitude', 'decorum'}, 2.975794689893901), (
                                                 {'memoir', 'narrative', 'article', 'tales', 'storyline', 'stories',
                                                  'diary'}, 2.949700209718181), (
                                                 {'trait', 'qualities', 'characteristics', 'prejudices', 'tendencies',
                                                  'characteristic', 'tendency'}, 2.7531760337817244), (
                                                 {'alliteration', 'language', 'phrase', 'words', 'abilities'},
                                                 2.6899048611350174),
                                             ({'better', 'sweeter', 'harsh', 'respectful', 'nicer'}, 2.684323282856412),
                                             ({'thoroughly', 'heavily', 'beautifully', 'scrupulously', 'closely'},
                                              2.628786585396807), (
                                                 {'sport', 'socializing', 'pastimes', 'happiness', 'pursuits',
                                                  'pleasures',
                                                  'pursuit', 'activities', 'conceit', 'adventures'}, 2.58015634287613),
                                             (
                                                 {'adaptation', 'translations', 'novels', 'characters', 'sequel'},
                                                 2.5763514512456465), (
                                                 {'heirs', 'estate', 'patriarch', 'inheritance', 'property', 'manor',
                                                  'grandson', 'father'}, 2.5515855459287833), (
                                                 {'scholarly', 'empirical', 'biology', 'research', 'scientists'},
                                                 2.4653947041548014), (
                                                 {'sex', 'morality', 'unmarried', 'marriage', 'marriages'},
                                                 2.430590160720464), (
                                                 {'merely', 'sufficiently', 'strongly', 'equally', 'duly'},
                                                 2.422572316578747), (
                                                 {'poll', 'dislike', 'approve', 'disapproves', 'disapproval'},
                                                 2.417852929083968), (
                                                 {'obsession', 'arrogance', 'desires', 'desire', 'intention'},
                                                 2.3799025608423694), (
                                                 {'qualities', 'protagonists', 'character', 'characters', 'celebrity'},
                                                 2.3535702078667597), (
                                                 {'revisions', 'revision', 'variations', 'altering', 'altered'},
                                                 2.3114541345872732), (
                                                 {'reduce', 'overcome', 'unnecessary', 'dissuade', 'keep'},
                                                 2.1850026150569617), (
                                                 {'proof', 'empirical', 'case', 'argument', 'justification'},
                                                 2.1302056847799724),
                                             ({'musical', 'singing', 'piano', 'music', 'dances'}, 2.1195292237387457), (
                                                 {'perception', 'opinion', 'views', 'viewpoint', 'picture'},
                                                 2.1027277398046342), (
                                                 {'preference', 'pleasing', 'dislike', 'loves', 'love'},
                                                 2.0764989830657825), (
                                                 {'problems', 'burden', 'sufferings', 'pain', 'hardship', 'families',
                                                  'humiliation', 'miseries'}, 2.0574074127071276),
                                             ({'unfolding', 'done', 'going', 'transpires', 'know'}, 2.0466286814664665),
                                             ({'poor', 'low', 'bad', 'sickly', 'hurting'}, 2.0314520776586873), (
                                                 {'described', 'characterizes', 'perceived', 'describes', 'depiction'},
                                                 2.024282790911345), (
                                                 {'significantly', 'slightly', 'actually', 'greatly', 'bit'},
                                                 2.0189600313325906),
                                             ({'genuine', 'actually', 'truth', 'reality', 'real'}, 2.0156028105241646),
                                             ({'required', 'imperative', 'key', 'role', 'advantages', 'desirable',
                                               'necessity', 'stresses'}, 1.9927229144180862), (
                                                 {'insufficiently', 'equally', 'highly', 'alike', 'generally'},
                                                 1.9871188035311202), (
                                                 {'rich', 'economic', 'happiness', 'wealthy', 'economy', 'prosperous',
                                                  'income', 'wealth'}, 1.944470357571036), (
                                                 {'poor', 'greedy', 'respectable', 'generous', 'modest'},
                                                 1.9435087641856974), (
                                                 {'factors', 'motive', 'reason', 'justification', 'reasoning'},
                                                 1.8937247285994858), (
                                                 {'experienced', 'accomplishment', 'done', 'successful',
                                                  'accomplishments'},
                                                 1.886402792949167),
                                             ({'method', 'technique', 'ways', 'tool', 'approach'}, 1.8258601568078046),
                                             ({'objections', 'rejects', 'failure', 'disapproval', 'accept'},
                                              1.7975316298254298), (
                                                 {'reduced', 'restrict', 'lack', 'restricted', 'insufficient'},
                                                 1.7706842787592225), (
                                                 {'key', 'dramatic', 'significant', 'major', 'memorable'},
                                                 1.7671996874027147), (
                                                 {'dictated', 'aided', 'different', 'welcomed', 'altering', 'grateful',
                                                  'counteracted', 'led', 'ensured', 'support', 'influenced', 'changes',
                                                  'despite', 'benefited'}, 1.7455375178526558), (
                                                 {'knowledge', 'explaining', 'experience', 'understand', 'learn'},
                                                 1.7199366352869319),
                                             ({'unfolds', 'happened', 'learns', 'goes', 'comes'}, 1.7022629887297538), (
                                                 {'nominated', 'declared', 'identified', 'renamed', 'known'},
                                                 1.6999132728382196), (
                                                 {'concern', 'objections', 'hopes', 'fury', 'concerns'},
                                                 1.6697480097261181), (
                                                 {'carried', 'taken', 'undertaken', 'done', 'conducted', 'brought',
                                                  'undergone', 'pointed'}, 1.6348764267493465),
                                             ({'merely', 'true', 'great', 'serious', 'real'}, 1.6347605634767493), (
                                                 {'learning', 'teaches', 'educated', 'classes', 'learn'},
                                                 1.6186878178287194), (
                                                 {'numerous', 'entire', 'comprehensive', 'experience', 'completion',
                                                  'begin', 'detailed', 'significant'}, 1.616081874740976), (
                                                 {'published', 'article', 'publication', 'editions', 'version'},
                                                 1.6146667706585078), (
                                                 {'engaged', 'intervene', 'join', 'encourage', 'involved'},
                                                 1.610338183532663),
                                             ({'arrived', 'revealed', 'arose', 'came', 'appeared'}, 1.6009982529514235),
                                             ({'improved', 'reduce', 'expanded', 'significantly', 'limited'},
                                              1.5856917220679265), (
                                                 {'originally', 'initially', 'subsequently', 'repeatedly', 'recently'},
                                                 1.58043910157331), (
                                                 {'surely', 'considered', 'probably', 'ironically', 'proved'},
                                                 1.5698487658446745), (
                                                 {'disclosed', 'detailed', 'detail', 'information', 'specify'},
                                                 1.5646536577813435),
                                             ({'sold', 'purchase', 'buying', 'leasing', 'sell'}, 1.5562824993490156), (
                                                 {'staying', 'life', 'rescued', 'lives', 'death', 'deceased', 'lived',
                                                  'born'}, 1.5278866807058789),
                                             ({'asked', 'fallen', 'refuses', 'specify', 'refused'}, 1.519462984916895),
                                             ({'decision', 'opinion', 'judge', 'judgments', 'reasoning'},
                                              1.4910329693819828), (
                                                 {'natural', 'simply', 'usually', 'actually', 'generally'},
                                                 1.4460918977035817), (
                                                 {'problems', 'responsibility', 'risk', 'effects', 'consequence'},
                                                 1.4063033176086415),
                                             ({'working', 'work', 'goes', 'uses', 'teaches'}, 1.4028296492231784),
                                             ({'united', 'conquer', 'bring', 'join', 'uniting'}, 1.401698655104568),
                                             ({'miss', 'speak', 'invited', 'join', 'meet'}, 1.3763064995384275), (
                                                 {'required', 'standard', 'minimum', 'rules', 'require'},
                                                 1.3665297224378843), (
                                                 {'show', 'suggesting', 'display', 'reveals', 'shows'},
                                                 1.3538101384670755),
                                             (
                                                 {'sentence', 'judgment', 'case', 'courts', 'attorney'},
                                                 1.343206484324142),
                                             ({'house', 'sold', 'residence', 'rents', 'lived'}, 1.34182331922759), (
                                                 {'problems', 'position', 'circumstance', 'matters', 'problem'},
                                                 1.3073346181218133), (
                                                 {'proposed', 'anticipated', 'promised', 'plans', 'decided'},
                                                 1.2878626070626698), (
                                                 {'come', 'followed', 'follows', 'adhere', 'following'},
                                                 1.2754955709500986), (
                                                 {'claimed', 'thought', 'speculated', 'believed', 'accepted'},
                                                 1.2474574760013515), (
                                                 {'law', 'laws', 'legal', 'courts', 'requirements', 'policy', 'rules',
                                                  'code'}, 1.192694060474281), (
                                                 {'message', 'stating', 'statement', 'dated', 'letters'},
                                                 1.1902469564427711),
                                             ({'looking', 'search', 'seeking', 'found', 'find'}, 1.142907299637085),
                                             ({'broke', 'came', 'began', 'resulted', 'end'}, 1.0667467559477213), (
                                                 {'staying', 'remain', 'leaving', 'living', 'stays', 'continue',
                                                  'remains',
                                                  'keep'}, 1.0620522032605224),
                                             ({'turn', 'came', 'brought', 'moved', 'put'}, 1.0400374033544608),
                                             ({'beginning', 'begin', 'going', 'coming', 'begins'}, 1.0195250181812443),
                                             ({'helping', 'allows', 'managed', 'aided', 'allowed'}, 0.9909598185417627),
                                             ({'twice', 'years', 'past', 'months', 'time', 'nights', 'times', 'days'},
                                              0.864723117598285),
                                             ({'looking', 'works', 'work', 'trying', 'helping'}, 0.823995514969653)]

    def test_find_nearest_neighbor_in_a_list(self):
        self.word2vec.pre_trained_google_news_300_model()
        self.neighbor = Neighborhood(self.word2vec.model, self.parameters)

        unigram = "human"

        min_distance = 0.3
        neighbor_size = 10

        neighbor = self.neighbor.find_nearest_neighbor_in_a_list(unigram, self.other_unigrams, min_distance,
                                                                 neighbor_size)

        self.assertEqual(neighbor, ['humans', 'sapiens', 'bipedal', 'anatomy', 'evolutionary', 'Humans', 'scientific'])

    def test_find_significant_neighbors(self):
        self.word2vec.pre_trained_google_news_300_model()
        self.neighbor = Neighborhood(self.word2vec.model, self.parameters)

        min_distance = 0.4
        neighbor_size = 5

        significant_neighbor = self.neighbor.find_significant_neighbors(self.other_unigrams, min_distance,
                                                                        neighbor_size)

        self.assertEqual(significant_neighbor,
                         [['Homo', 'sapiens', 'hominins', 'species', 'evolutionary'],
                          ['in', 'about', 'out', 'through', 'at'],
                          ['humans', 'sapiens', 'hominins', 'genus', 'evolutionary'],
                          ['the', 'only', 'other', 'that', 'this'],
                          ['humans', 'sapiens', 'human', 'bipedal', 'evolutionary'],
                          ['increased', 'trend', 'increasing', 'higher', 'growth'],
                          ['compared', 'rise', 'increasing', 'higher', 'expanded'],
                          ['more', 'less', 'than', 'large', 'higher'],
                          ['brains', 'anatomically', 'brain', 'prefrontal', 'temporal'],
                          ['are', 'has', 'this', 'been', 'be'],
                          ['had', 'have', 'been', 'subsequently', 'is']])

    def test_merge_close_neighbors(self):
        self.neighbor = Neighborhood(None, self.parameters)

        minimum_merge_intersection = 1
        merged_neighbors = self.neighbor.merge_close_neighbors(
            [['Homo', 'sapiens', 'hominins', 'species', 'evolutionary'],
             ['in', 'about', 'out', 'through', 'at'],
             ['humans', 'sapiens', 'hominins', 'genus', 'evolutionary'],
             ['the', 'only', 'other', 'that', 'this'],
             ['humans', 'sapiens', 'human', 'bipedal', 'evolutionary'],
             ['increased', 'trend', 'increasing', 'higher', 'growth'],
             ['compared', 'rise', 'increasing', 'higher', 'expanded'],
             ['more', 'less', 'than', 'large', 'higher'],
             ['brains', 'anatomically', 'brain', 'prefrontal', 'temporal'],
             ['are', 'has', 'this', 'been', 'be'],
             ['had', 'have', 'been', 'subsequently', 'is']], minimum_merge_intersection)

        self.assertEqual(merged_neighbors,
                         [{'species', 'hominins', 'Homo', 'bipedal', 'evolutionary', 'humans', 'genus', 'human',
                           'sapiens'}, {'out', 'through', 'in', 'at', 'about'},
                          {'is', 'are', 'been', 'other', 'this', 'be', 'that', 'had', 'the', 'only', 'have',
                           'subsequently', 'has'},
                          {'trend', 'higher', 'than', 'increasing', 'less', 'increased', 'compared', 'expanded', 'rise',
                           'more', 'growth', 'large'}, {'brain', 'brains', 'prefrontal', 'anatomically', 'temporal'}])

    def test_find_significant_merged_neighbors(self):
        self.word2vec.pre_trained_google_news_300_model()
        self.neighbor = Neighborhood(self.word2vec.model, self.parameters)

        min_distance = 0.4
        neighbor_size = 5
        minimum_merge_intersection = 1

        significant_merge_neighbor = self.neighbor.find_significant_merged_neighbors(self.other_unigrams, min_distance,
                                                                                     neighbor_size,
                                                                                     minimum_merge_intersection)

        expected_res = [{'sapiens', 'human', 'genus', 'evolutionary', 'species', 'humans', 'hominins', 'Homo',
                         'bipedal'}, {'this', 'other', 'be', 'are', 'that', 'only', 'been', 'has', 'the'},
                        {'less', 'expanded', 'than', 'rise', 'more', 'growth', 'higher', 'large', 'trend', 'compared',
                         'increasing', 'increased'}, {'subsequently', 'have', 'had', 'been', 'is'},
                        {'about', 'at', 'in', 'through', 'out'},
                        {'prefrontal', 'brain', 'brains', 'temporal', 'anatomically'}]

        self.assertTrue(significant_merge_neighbor[0] in expected_res)
        self.assertEqual(len(significant_merge_neighbor), len(expected_res))

    def test_remove_stopwords_neighbors(self):
        self.neighbor = Neighborhood(None, self.parameters)
        max_stop_words = 3
        neighbors = [{'sapiens', 'human', 'genus', 'evolutionary', 'species', 'humans', 'hominins', 'Homo',
                      'bipedal'}, {'this', 'other', 'be', 'are', 'that', 'only', 'been', 'has', 'the'},
                     {'less', 'expanded', 'than', 'rise', 'more', 'growth', 'higher', 'large', 'trend', 'compared',
                      'increasing', 'increased'}, {'subsequently', 'have', 'had', 'been', 'is'},
                     {'about', 'at', 'in', 'through', 'out'},
                     {'prefrontal', 'brain', 'brains', 'temporal', 'anatomically'}]
        res = self.neighbor.remove_stopwords_neighbors(neighbors, max_stop_words)
        expected_res = [
            {'hominins', 'Homo', 'sapiens', 'evolutionary', 'genus', 'humans', 'human', 'bipedal', 'species'},
            {'increasing', 'less', 'trend', 'increased', 'higher', 'compared', 'rise', 'expanded', 'large', 'growth'},
            {'anatomically', 'brain', 'prefrontal', 'brains', 'temporal'}]
        self.assertEqual(res, expected_res)

    def test_remove_stemmed_similar_words(self):
        self.neighbor = Neighborhood(None, self.parameters)
        neighbors = [{'sapiens', 'human', 'genus', 'evolutionary', 'species', 'humans', 'hominins', 'Homo',
                      'bipedal'}, {'this', 'other', 'be', 'are', 'that', 'only', 'been', 'has', 'the'},
                     {'less', 'expanded', 'than', 'rise', 'more', 'growth', 'higher', 'large', 'trend', 'compared',
                      'increasing', 'increased'}, {'subsequently', 'have', 'had', 'been', 'is'},
                     {'about', 'at', 'in', 'through', 'out'},
                     {'prefrontal', 'brain', 'brains', 'temporal', 'anatomically'}]
        res = self.neighbor.remove_stemmed_similar_words_neighbors(neighbors)
        expected_res = [{'bipedal', 'species', 'human', 'sapiens', 'hominins', 'Homo', 'genus', 'evolutionary'},
                        {'been', 'the', 'are', 'that', 'other', 'be', 'has', 'this', 'only'},
                        {'increasing', 'than', 'rise', 'trend', 'growth', 'higher', 'more', 'compared', 'less',
                         'expanded', 'large'}, {'been', 'is', 'subsequently', 'have', 'had'},
                        {'at', 'about', 'through', 'in', 'out'},
                        {'brains', 'temporal', 'anatomically', 'prefrontal'}]
        self.assertEqual(res[0], expected_res[0])
        self.assertEqual(len(res), len(expected_res))

    def test_remove_stemmed_similar_words_list(self):
        self.neighbor = Neighborhood(None, self.parameters)
        neighbor = ['sapiens', 'human', 'genus', 'evolutionary', 'species', 'humans', 'hominins', 'Homo', 'bipedal']
        res = self.neighbor.remove_stemmed_similar_words_list(neighbor)
        expected_res = ['bipedal', 'species', 'human', 'sapiens', 'hominins', 'Homo', 'genus', 'evolutionary']
        self.assertEqual(set(res), set(expected_res))

    def test_replace_stemmed_similar_words_list(self):
        self.neighbor = Neighborhood(None, self.parameters)
        neighbor = ['sapiens', 'human', 'genus', 'evolutionary', 'species', 'humans', "Human", 'hominins', 'Homo',
                    'bipedal']
        res = self.neighbor.replace_stemmed_similar_words_list(neighbor)
        expected_res = ['sapiens', 'human', 'genus', 'evolutionary', 'species', 'human', 'human', 'hominins', 'Homo',
                        'bipedal']
        self.assertEqual(res, expected_res)

    def test_find_significant_pruned_neighbors(self):
        self.word2vec.pre_trained_google_news_300_model()
        self.neighbor = Neighborhood(self.word2vec.model, self.parameters)

        min_distance = 0.4
        neighbor_size = 5
        minimum_merge_intersection = 1
        max_stop_words = 1

        res = self.neighbor.find_significant_pruned_neighbors(self.other_unigrams, min_distance,
                                                              neighbor_size,
                                                              minimum_merge_intersection,
                                                              max_stop_words)

        expected_res = [{'humans', 'sapiens', 'hominins', 'species', 'evolutionary', 'genus', 'Homo', 'bipedal'},
                        {'brains', 'anatomically', 'prefrontal', 'temporal'}]

        self.assertTrue(len(res[0]) == len(expected_res[0]) or len(res[0]) == len(expected_res[1]))
        self.assertTrue(len(res[1]) == len(expected_res[1]) or len(res[1]) == len(expected_res[0]))

    def test_find_significant_pruned_neighbors_in_doc(self):
        self.word2vec.pre_trained_google_news_300_model()
        self.neighbor = Neighborhood(self.word2vec.model, self.parameters)

        min_distance = 0.4
        neighbor_size = 5
        minimum_merge_intersection = 2
        max_stop_words = 1

        self.neighbor.get_words = MagicMock(return_value=self.doc_words)

        res = self.neighbor.find_significant_pruned_neighbors_in_doc(
            "../../configs/others/pride_and_prejudice_wiki.txt",
            min_distance,
            neighbor_size,
            minimum_merge_intersection,
            max_stop_words)

        expected_res = self.significant_neighbors_wiki

        print(res, file=sys.stderr)

        self.assertEqual(len(res), len(expected_res))

    def test_find_significant_neighbors_weight(self):
        self.parameters.params["repo_dir"] = '/scratch/index/indri_5_7/ap8889'
        self.neighbor = Neighborhood(None, self.parameters)

        significant_neighbors_weight = \
            self.neighbor.find_significant_neighbors_weight(self.doc_words, self.significant_neighbors_wiki_index)
        print(significant_neighbors_weight, file=sys.stderr)
        self.assertEqual(significant_neighbors_weight, self.significant_neighbors_weight)

    def test_sort_significant_neighbors(self):
        self.neighbor = Neighborhood(None, self.parameters)

        sorted_significant_neighbors = self.neighbor.sort_significant_neighbors(self.significant_neighbors_weight,
                                                                                self.significant_neighbors_wiki_index)
        print(sorted_significant_neighbors, file=sys.stderr)
        self.assertEqual(sorted_significant_neighbors, self.sorted_significant_neighbors)

    def test_index_neighbors(self):
        self.neighbor = Neighborhood(None, self.parameters)
        significant_neighbors_wiki_index = self.neighbor.index_neighbors(self.significant_neighbors_wiki)
        print(significant_neighbors_wiki_index, file=sys.stderr)
        self.assertEqual(significant_neighbors_wiki_index, self.significant_neighbors_wiki_index)

    def test_get_words(self):
        self.neighbor = Neighborhood(None, self.parameters)
        doc_words = self.neighbor.get_words("../../configs/others/pride_and_prejudice_wiki.txt")
        print(doc_words, file=sys.stderr)
        self.assertEqual(doc_words, self.doc_words)

    def test_run(self):
        self.neighbor = Neighborhood(None, self.parameters)

        min_distance = 0.4
        neighbor_size = 5
        minimum_merge_intersection = 2
        max_stop_words = 1

        self.neighbor.get_words = MagicMock(return_value=self.doc_words)
        self.neighbor.find_significant_pruned_neighbors = MagicMock(return_value=self.significant_neighbors_wiki)
        self.neighbor.index_neighbors = MagicMock(return_value=self.significant_neighbors_wiki_index)
        self.neighbor.find_significant_neighbors_weight = MagicMock(return_value=self.significant_neighbors_weight)
        self.neighbor.sort_significant_neighbors = MagicMock(return_value=self.sorted_significant_neighbors)

        sorted_significant_neighbors = self.neighbor.run(
            "../../configs/others/pride_and_prejudice_wiki.txt",
            min_distance,
            neighbor_size,
            minimum_merge_intersection,
            max_stop_words)
        print(sorted_significant_neighbors, file=sys.stderr)
        self.assertEqual(sorted_significant_neighbors, self.sorted_significant_neighbors)
