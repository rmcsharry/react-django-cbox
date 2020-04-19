import axios from 'axios';

import { GET_PROGRESS } from './types';

// GET PROGRESS action
export const getProgress = () => (dispatch) => {
  axios
    .get('/api/v1/progress/')
    .then((res) => {
      dispatch({
        type: GET_PROGRESS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
