import axios from 'axios'

import { COURSES_RECEIVED, COURSE_CHOSEN } from './types'

export const doFetchCourses = () => (dispatch) => {
  axios
    .get('/api/v1/organisations/1/courses')
    .then((res) => {
      dispatch({
        type: COURSES_RECEIVED,
        payload: res.data,
      })
    })
    .catch((err) => console.log(err))
}

export const doChooseCourse = payload => ({ type: COURSE_CHOSEN, payload })
