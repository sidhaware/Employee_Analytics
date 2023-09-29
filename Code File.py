import joblib
import pickle
import streamlit as st
import sklearn

model = pickle.load(open('rf_model.pkl','rb'))

def main():
    st.title('Employee Churn Predictor')

    #input Variables
    # 'children', 'Claim_Amount', 'past_consultations','Hospital_expenditure', 'Anual_Salary'
    lv=st.text_input('Last evaluation score (normalized value between 0 to 1)')
    np =st.text_input('Number of projects completed')
    ty =st.text_input('Total years completed in the Company')
    sl=st.text_input('Salary (1 - Low category \n 2 - Medium category \n 3 - High category)')
   


    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[float(lv), float(np), float(ty), float(sl)]])
        output=round (makeprediction[0], 2)
        if output==1:
            st.success('The employee is likely to churn')
        else:
            st.success('The employee is not likely to churn')

        

if __name__ == '__main__':
    main()

