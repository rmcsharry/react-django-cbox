import { PROGRESS_RECEIVED } from '../actions/types.js'
import { COURSE_CHOSEN } from '../actions/types.js'

const initialState = {
  progress: { results: [] },
  chosenCourse: 0,
  selectedOrganisation: {}, // TODO: provide different dashboards per organisation so this will store which is the 'current' one
}

export default function (state = initialState, action) {
  switch (action.type) {
    case PROGRESS_RECEIVED:
      return {
        ...state,
        progress: action.payload,
      }
    case COURSE_CHOSEN:
      return {
        ...state,
        chosenCourse: action.payload
      }
    default:
      return state
  }
}
