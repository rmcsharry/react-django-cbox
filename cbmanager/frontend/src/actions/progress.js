import axios from 'axios'

import { PROGRESS_RECEIVED } from './types'

export const doFetchProgress = () => (dispatch) => {
  axios
    .get('/api/v1/progress/')
    .then((res) => {
      dispatch({
        type: PROGRESS_RECEIVED,
        payload: res.data,
      })
    })
    .catch((err) => console.log(err))
}
