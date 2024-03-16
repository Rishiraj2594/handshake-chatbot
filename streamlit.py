import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'

app1= App.from_config(config={
  "app": {
    "config": {
      "id": "bot1",
    }

  },
  'llm': {
        'provider': 'openai',
        'config': {
            'model': 'gpt-3.5-turbo',
            'temperature': 1.0,
            'max_tokens': 1000,
            'top_p': 1,
            'prompt': (
                "Use the following pieces of context to answer the query at the end.\n"
                "Query can have typo or no that clear, think closet possible answer from below context"
                "Try go level 2 deep before answering the query and conects all the dots then answer\n"
                "$context\n\nQuery: $query\n\nHelpful Answer:"
            ),
            'system_prompt': (
                 "your name Handshake guru Act as a very knowlegable ai that helps people regarding their queries"
                #"Helpful assitant"
            ),
        }
    },
})
print(app1.db.get())
app1.add('https://github.com/handshake-org/hsd/blob/master/README.md')
# app1.add(("What is Handshake?", "Handshake is a peer-to-peer blockchain which serves as a decentralised DNS root zone of the internet. It ensures that the global DNS infrastructure is freed from the centralised control of ICANN. Handshake is a POW chain and is forked from Bcoin which is a fork of bitcoin. Handshake serves as a root for all the TLDs on the internet. Examples of TLDs you may be familiar with are .com, .org, .in, .us etc. Basically, domain extensions which live on the ‘right side of the dot’. It grandfathers the legacy internet by locking off all the existing 1500 plus TLDs to ensure there are no name clashes. All other words and phrases can be created as a TLD on this blockchain."), data_type="qna_pair")
# app1.add(("What is HNS token?", "HNS is the native token of the Handshake ecosystem. It is used to bid on the Tokens. The winner pays the second highest amount and that amount is burned this leading to a deflationary token. The total supply if 2.1 billion."), data_type="qna_pair")
# app1.add(("What is Agaamin?", "Agaamin Technologies is a digital identity provider built on Handshake. They are based in India and are focussed to using Handshake to empower non-English speakers on an Internet which is largely built on an English infrastructure."), data_type="qna_pair")
# app1.add(("Who is Sajan?", "Sajan Nair is the CEO and Founder of Agaamin Technologies.  Kriti, Rishi and Raju are developers who have been instrumental in building the tech stack. Dakshita looks after operations, partner relations and marketing at Agaamin. "), data_type="qna_pair")
# app1.add(("what are the list of reserved name in hanshake", "List of reserved Handshake names claimed so far can be found here. https://handshake.rsvp/"), data_type="qna_pair")

# app1.add(("How are TLDs on Handshake created?", "Anyone can pass a transaction on Handshake and create a TLD. The TLD then goes through an auction process which lasts 5 days. This ensures that everyone has a chance at acquiring a TLD. The highest bidder at the end of 5 days is declared the winner and gets to keep the TLD. The auctions are conducted in HNS, the native token of the Handshake ecosystem."), data_type="qna_pair")
