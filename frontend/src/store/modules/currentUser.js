import api from "../../services/api";

const state = {
  currentUser: [],
  isConfirm: false,
};

const getters = {
  currentUser: (state) => {
    return state.currentUser;
  },
  isConfirm: (state) => {
    return state.isConfirm;
  },
};

const actions = {
  getCurrentUser({ commit }) {
    api
      .get(`users/current_user/`)
      .then((currentuser) => {
        commit("setVerify", currentuser);
        commit("setCurrentuser", currentuser);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  changeCurrentUserSummonerName({ commit }, payload) {
    console.log(payload);

    api
      .post(`users/${payload.id}/update_user_from_riotusername/`, {
        riot_name: payload.riot_name,
      })

      .then((currentuser) => {
        console.log(currentuser);
        commit("setCurrentuser", currentuser);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setCurrentuser(state, currentuser) {
    state.currentUser = currentuser.data;
  },
  setVerify(state, currentuser) {
    state.isConfirm = currentuser.data.is_confirm;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
