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
        "How do returns work?",
        "Do you offer refunds?",
        "Are there any ongoing sales or promotions?",
        "Do you have any discounts right now?",
        "Is there a sale going on?",
        "What are your shipping options?",
        "How long does delivery take?",
        "How can I check my order status?",
        "Where is my order?",
        "How do I contact customer support?",
        
        
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
