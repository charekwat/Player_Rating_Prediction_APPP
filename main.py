
from mailbox import ExternalClashError
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
#pickle_in = open('filename.pkl', 'rb')
#classifier = pickle.load(pickle_in)
with open("filemodel","rb") as f:
     classifier = pickle.load(f)


def welcome():
    return 'welcome to Fifa prediction app'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(age, weight_kg, nationality, potential, value_eur, player_positions, international_reputation, skill_moves, release_clause_eur, team_position, joined, contract_valid_until, shooting, passing, dribbling, defending, physic, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, player_traits, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, skill_dribbling, skill_curve, skill_fk_accuracy, skill_ball_control, movement_sprint_speed, movement_agility, movement_reactions, movement_balance, power_shot_power, power_jumping, power_stamina, power_strength, mentality_aggression, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure, defending_marking, defending_standing_tackle, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_reflexes, ls, stm, rs, lw, lf, cf, rf, rw, lam, cam, ram, lcm, cm, rcm, lwb, ldm, cdm, rdm, rwb, lcb, cb, rcb):
    prediction = classifier.predict(
        [[age, weight_kg, nationality, potential, value_eur, player_positions, international_reputation, skill_moves, release_clause_eur, team_position, joined, contract_valid_until, shooting, passing, dribbling, defending, physic, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, player_traits, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, skill_dribbling, skill_curve, skill_fk_accuracy, skill_ball_control, movement_sprint_speed, movement_agility, movement_reactions, movement_balance, power_shot_power, power_jumping, power_stamina, power_strength, mentality_aggression, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure, defending_marking, defending_standing_tackle, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_reflexes, ls, stm, rs, lw, lf, cf, rf, rw, lam, cam, ram, lcm, cm, rcm, lwb, ldm, cdm, rdm, rwb, lcb, cb, rcb]])
    print(prediction)
    return prediction

    # this is the main function in which we define our webpage


def main():
    # giving the webpage a title
    st.title("Fifa Overall Rating Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Fifa Player Overall Rating Prediction </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    st.sidebar.title("FIFA Player rating")  # get input values
    age = st.sidebar.slider('age')
    weight_kg = st.sidebar.slider("weight_kg")
    nationality = st.sidebar.slider("nationality")
    potential= st.sidebar.slider("potential")
    value_eur= st.sidebar.slider(" value_eur")

    player_positions= st.sidebar.slider("player_positions")
    international_reputation = st.sidebar.slider("international_reputation")
    skill_moves = st.sidebar.slider("skill_moves")
    release_clause_eur = st.sidebar.slider("release_clause_eur")
    team_position = st.sidebar.slider("team_position")
    joined= st.sidebar.slider("joined")
    contract_valid_until= st.sidebar.slider("contract_valid_until")
    shooting= st.sidebar.slider("shooting")
    passing= st.sidebar.slider("passing")
    dribbling= st.sidebar.slider("dribbling")
    defending= st.sidebar.slider("defending")
    physic= st.sidebar.slider("physic")
    gk_diving= st.sidebar.slider("gk_diving")
    gk_handling= st.sidebar.slider("gk_handling")
    gk_kicking= st.sidebar.slider("gk_kicking")
    gk_reflexes= st.sidebar.slider("gk_reflexes")
    gk_speed= st.sidebar.slider("gk_speed")
    gk_positioning= st.sidebar.slider("gk_positioning")
    player_traits= st.sidebar.slider("player_traits")
    attacking_finishing= st.sidebar.slider("attacking_finishing")
    attacking_heading_accuracy= st.sidebar.slider("attacking_heading_accuracy")
    attacking_short_passing= st.sidebar.slider("attacking_short_passing")
    skill_dribbling= st.sidebar.slider("skill_dribbling")
    skill_curve= st.sidebar.slider("skill_curve")
    skill_fk_accuracy= st.sidebar.slider("skill_fk_accuracy")
    skill_ball_control= st.sidebar.slider("skill_ball_control")
    movement_sprint_speed= st.sidebar.slider("movement_sprint_speed")
    movement_agility= st.sidebar.slider("movement_agility")
    movement_reactions= st.sidebar.slider("movement_reactions")
    movement_balance= st.sidebar.slider("movement_balance")
    power_shot_power= st.sidebar.slider("power_shot_power")
    power_jumping= st.sidebar.slider("power_jumping")
    power_stamina= st.sidebar.slider("power_stamina")
    power_strength= st.sidebar.slider("power_strength")
    mentality_aggression= st.sidebar.slider("mentality_aggression")
    mentality_positioning= st.sidebar.slider("mentality_positioning")
    mentality_vision= st.sidebar.slider("mentality_vision")
    mentality_penalties= st.sidebar.slider("mentality_penalties")
    mentality_composure= st.sidebar.slider("mentality_composure")
    defending_marking= st.sidebar.slider("defending_marking")
    defending_standing_tackle= st.sidebar.slider("defending_standing_tackle")
    goalkeeping_diving= st.sidebar.slider("goalkeeping_diving")
    goalkeeping_handling= st.sidebar.slider("goalkeeping_handling")
    goalkeeping_kicking= st.sidebar.slider("goalkeeping_kicking")
    goalkeeping_reflexes= st.sidebar.slider("goalkeeping_reflexes")
    ls= st.sidebar.slider("ls")
    stm= st.sidebar.slider("stm")
    rs= st.sidebar.slider("rs")
    lw= st.sidebar.slider("lw")
    lf= st.sidebar.slider("lf")
    cf= st.sidebar.slider("cf")
    rf= st.sidebar.slider("rf")
    rw= st.sidebar.slider("rw")
    lam= st.sidebar.slider("lam")
    cam= st.sidebar.slider("cam")
    ram= st.sidebar.slider("ram")
    lcm= st.sidebar.slider("lcm")
    cm= st.sidebar.slider("cm")
    rcm= st.sidebar.slider("rcm")
    lwb= st.sidebar.slider("lwb")
    ldm= st.sidebar.slider("ldm")
    cdm= st.sidebar.slider("cdm")
    rdm= st.sidebar.slider("rdm")
    rwb= st.sidebar.slider("rwb")
    lcb= st.sidebar.slider("lcb")
    cb= st.sidebar.slider("cb")
    rcb= st.sidebar.slider("rcb")

    result = ""

    if st.button("Predict"):
        result = prediction(age, weight_kg, nationality, potential, value_eur, player_positions, international_reputation, skill_moves, release_clause_eur, team_position, joined, contract_valid_until, shooting, passing, dribbling, defending, physic, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, player_traits, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, skill_dribbling, skill_curve, skill_fk_accuracy, skill_ball_control, movement_sprint_speed, movement_agility, movement_reactions, movement_balance, power_shot_power, power_jumping, power_stamina, power_strength, mentality_aggression, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure, defending_marking, defending_standing_tackle, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_reflexes, ls, stm, rs, lw, lf, cf, rf, rw, lam, cam, ram, lcm, cm, rcm, lwb, ldm, cdm, rdm, rwb, lcb, cb, rcb)
    st.success('Overall rating is {}'.format(result))


if __name__ == '__main__':
    main()