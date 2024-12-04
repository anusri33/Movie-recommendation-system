{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6ad0eb0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-29 14:25:24.639 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\anusr\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-11-29 14:25:24.640 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from pymongo import MongoClient\n",
    "\n",
    "# Connect to MongoDB\n",
    "client = MongoClient(\"mongodb://localhost:27017/\")\n",
    "db = client[\"movie_recommendation\"]\n",
    "movies_collection = db[\"movies\"]\n",
    "\n",
    "st.title(\"Movie Recommendation System\")\n",
    "\n",
    "# Search for movies by genre\n",
    "genre = st.text_input(\"Enter genre to search for movies:\")\n",
    "if genre:\n",
    "    movies = movies_collection.find({\"genres\": genre})\n",
    "    st.write(\"Movies:\")\n",
    "    for movie in movies:\n",
    "        st.write(movie[\"title\"])\n",
    "\n",
    "# Add a new rating\n",
    "user_id = st.number_input(\"User ID\", min_value=1, step=1)\n",
    "movie_id = st.number_input(\"Movie ID\", min_value=1, step=1)\n",
    "rating = st.slider(\"Rating\", 0.0, 5.0, step=0.5)\n",
    "if st.button(\"Submit Rating\"):\n",
    "    db[\"ratings\"].insert_one({\n",
    "        \"userId\": user_id,\n",
    "        \"movieId\": movie_id,\n",
    "        \"rating\": rating\n",
    "    })\n",
    "    st.success(\"Rating submitted!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65178e9f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
