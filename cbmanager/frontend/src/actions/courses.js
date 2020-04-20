import axios from 'axios'

import { GET_COURSES } from './types'

export const getCourses = () => (dispatch) => {
  axios
    .get('/api/v1/organisations/1/courses')
    .then((res) => {
      dispatch({
        type: GET_COURSES,
        payload: res.data,
      })
    })
    .catch((err) => console.log(err))
}
