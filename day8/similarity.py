from sentence_transformers import util, SentenceTransformer      #util is libraryfunction
model = SentenceTransformer("all-MiniLM-L6-v2")#embedding model
sentences =[
    "I love cricket",
    "I enjoy eatting food",
    "My habbit was listening songs"
]
sentence_embedding = model.encode(sentences)# to change sentences into vector form 
similarity1 = util.cos_sim(sentence_embedding[0], sentence_embedding[1])
print(similarity1.item())
#print(sentence_embedding[0])

