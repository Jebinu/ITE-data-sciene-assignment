{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "247c447d-1872-490a-befd-3eef6971cf0a",
   "metadata": {},
   "source": [
    "# Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a7e3820-8354-43e0-9fe4-f849c24fa164",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "512da3b2-8d5a-42ae-9696-f3f5f83f1fa8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "# Import functions from their respective files\n",
    "from recommend_exhibitors_by_answers_and_test import recommend_exhibitors_by_answers\n",
    "from recommend_exhibitors_by_visitor_email_and_test import recommend_exhibitors\n",
    "from recommend_visitors_by_exhibitorID_and_test import recommend_visitors_by_exhibitorID\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "37be5f5e-7a3a-4558-85d7-37e7b468e2ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "exhibitor_final=pd.read_csv(\"exhibitor_final.csv\")\n",
    "visitors_final=pd.read_csv(\"final_analysis_data_visitors.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "23d86bf6-ff33-4001-bacd-310624fb70b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running test for: recommend_exhibitors_by_answers\n",
      "✅ Passed recommend_exhibitors_by_answers\n"
     ]
    }
   ],
   "source": [
    "#Run Test\n",
    "print(\"Running test for: recommend_exhibitors_by_answers\")\n",
    "\n",
    "visitor_id = visitors_final['visitor_id'].dropna().astype(str).iloc[0]\n",
    "recommendations_answers = recommend_exhibitors_by_answers(visitor_id, top_n=5)\n",
    "\n",
    "assert not recommendations_answers.empty, \"❌ No results for valid visitor ID with answers\"\n",
    "assert 'similarity_score' in recommendations_answers.columns, \"❌ Missing similarity_score column\"\n",
    "\n",
    "print(\"✅ Passed recommend_exhibitors_by_answers\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bef52040-35ef-4b0c-b19e-81ef229e6a0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting test for: recommend_exhibitors_by_visitor_email\n",
      "✅ Test passed for recommend_exhibitors_by_visitor_email\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Running test for the recommendation function based on visitor email\n",
    "print(\"Starting test for: recommend_exhibitors_by_visitor_email\")\n",
    "\n",
    "# Sample visitor email taken from the dataset\n",
    "sample_email = visitors_final['email'].dropna().iloc[0]\n",
    "\n",
    "# Get recommendations for exhibitors using the sample visitor email\n",
    "recommendations_email = recommend_exhibitors(sample_email, top_n=5)\n",
    "\n",
    "# Ensure that recommendations are returned and not empty\n",
    "assert not recommendations_email.empty, \"❌ No recommendations returned for a valid visitor email\"\n",
    "\n",
    "# Check if the 'similarity_score' column exists in the returned recommendations\n",
    "assert 'similarity_score' in recommendations_email.columns, \"❌ 'similarity_score' column is missing in the recommendations\"\n",
    "\n",
    "# If all checks pass, print a success message\n",
    "print(\"✅ Test passed for recommend_exhibitors_by_visitor_email\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7680f62b-e33f-40e2-982d-39e83ff0692d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting test for: recommend_visitors_by_exhibitorID\n",
      "✅ Test passed for recommend_visitors_by_exhibitorID\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Running test for the visitor recommendation based on exhibitor ID\n",
    "print(\"Starting test for: recommend_visitors_by_exhibitorID\")\n",
    "\n",
    "# Pick a valid exhibitor ID from the dataset\n",
    "sample_exhibitor_id = exhibitor_final['exhibitorid'].dropna().iloc[0]\n",
    "\n",
    "# Get recommended visitors for that exhibitor\n",
    "recommendations = recommend_visitors(sample_exhibitor_id, top_n=5)\n",
    "\n",
    "# Check if we received any recommendations\n",
    "assert not recommendations.empty, \"❌ No recommendations returned for a valid exhibitor ID\"\n",
    "\n",
    "# Check if similarity scores are present\n",
    "assert 'similarity_score' in recommendations.columns, \"❌ 'similarity_score' column is missing in the recommendations\"\n",
    "\n",
    "# If all checks pass\n",
    "print(\"✅ Test passed for recommend_visitors_by_exhibitorID\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1a77b1d-558c-43ac-9e60-62e8ce89005e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
