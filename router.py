from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.routers import SemanticRouter


# Initialize encoder
encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

# Define FAQ route
faq = Route(
    name='faq',
    utterances=[
        "What is your return policy?",
        "Can I return a product?",
        "Is this book in stock?",
        "Do you offer discounts on bulk purchases?",
        "Are there any ongoing sales or promotions?",
        "Do you sell used or second-hand books?",
        "Is there a sale going on?",
        "What are your shipping options?",
        "Do you ship internationally?",
        "Can I read reviews before buying?",
        "Can I track my order?",
        "Do you offer gift cards?",
        "I can't find a book I'm looking for",
        
        
    ]
)

# Define SQL route
sql = Route(
    name='sql',
    utterances=[
         "Are there any books on sale?",
        "Which books are discounted?",
        "What is the price of Then She Was Gone: A Novel?",
        "How much does Then She Was Gone cost?",
        "Is this book available?",
        "List all available books",
        "Show me books under 20 euros",
        "Which books are written by this author?",
        "How many books are in the catalog?",
       
    ]
)

# Create router
router = SemanticRouter(encoder=encoder,routes=[sql,faq],auto_sync="local" )

if __name__ == "__main__":
    # Test queries
    query1 = "What is your policy on defective product?"
    result1 = router(query1)
    print(f"Query: {query1}")
    print(f"Route: {result1.name}\n")
    
    query2 = "Pink Puma shoes in price range 5000 to 1000"
    result2 = router(query2)
    print(f"Query: {query2}")
    print(f"Route: {result2.name}")
