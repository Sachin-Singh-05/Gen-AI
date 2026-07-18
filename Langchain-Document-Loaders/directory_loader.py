from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader = DirectoryLoader(
    path='Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(len(docs))

# print(docs[220].page_content)
# print(docs[220].metadata)

# LAZY LOADER

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)