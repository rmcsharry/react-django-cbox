import { GET_COURSES } from '../actions/types.js'

const initialState = {
  courses: [],
}

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_COURSES:
      return {
        ...state,
        // TODO: Ignore pagination for now and just get the results array
        courses: action.payload.results, 
      }
    default:
      return state
  }
}
