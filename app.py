import streamlit as st
import pickle
import numpy as np

# ---------------------------------------------------
# Load saved files
# ---------------------------------------------------

popular = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📚 Book Recommendation System")

st.write(
    "Select a book you like and get four similar book recommendations."
)

st.divider()


# ---------------------------------------------------
# Book selection
# ---------------------------------------------------

book_name = st.selectbox(
    "🔍 Select a Book",
    pt.index.values
)


# ---------------------------------------------------
# Recommendation
# ---------------------------------------------------

if st.button("🎯 Recommend Books"):

    index = np.where(pt.index == book_name)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    st.subheader("📖 Recommended Books")

    cols = st.columns(4)

    for col, i in zip(cols, similar_items):

        book_title = pt.index[i[0]]

        temp_df = books[
            books['Book-Title'] == book_title
        ].drop_duplicates('Book-Title')

        author = temp_df['Book-Author'].values[0]

        # Use large image
        image_url = temp_df['Image-URL-L'].values[0]

        with col:

            st.image(
                image_url,
                width="stretch"
            )

            st.markdown(
                f"**{book_title}**"
            )

            st.write(
                f"✍️ {author}"
            )