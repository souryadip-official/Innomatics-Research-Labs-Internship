import streamlit as st
import boto3
from config import AWS_REGION, KNOWLEDGE_BASE_ID, MODEL_ARN

bedrock_agent_runtime = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name=AWS_REGION
)

def query_knowledge_base(question):
    try:
        response = bedrock_agent_runtime.retrieve_and_generate(
            input={
                "text": question
            },
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": MODEL_ARN,
                    "retrievalConfiguration": {
                        "vectorSearchConfiguration": {
                            "numberOfResults": 5
                        }
                    }
                }
            }
        )

        answer = response["output"]["text"]

        # Extract citations
        citations = []
        if "citations" in response:
            for c in response["citations"]:
                for ref in c["retrievedReferences"]:
                    citations.append({
                        "content": ref.get("content", "")[:200],
                        "source": ref.get("location", {}).get("s3Location", {}).get("uri", "Unknown")
                    })

        return answer, citations

    except Exception as e:
        return str(e), []


st.set_page_config(page_title="Enterprise RAG Q&A", layout="wide")

st.title("📊 Enterprise Knowledge Base Q&A (RAG)")
st.write("Ask questions about internal company documents")

# input
query = st.text_input("Enter your question:")

if st.button("Ask") and query:
    with st.spinner("Retrieving answer..."):
        answer, citations = query_knowledge_base(query)

    # answer
    st.subheader("💡 Answer")
    st.write(answer)

    if citations:
        st.subheader("📚 Sources")
        for i, c in enumerate(citations):
            st.markdown(f"**Source {i+1}:** {c['source']}")
            st.caption(c["content"])