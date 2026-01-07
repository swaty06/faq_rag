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
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
    ]
)

# Define SQL route
sql = Route(
    name='sql',
    utterances=[
        "Are there any books on sale?",
        "What is the price of Then She Was Gone: A Novel?",  # Fixed typo
        "Show me products under 1000",
        "Which items are discounted?",
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
