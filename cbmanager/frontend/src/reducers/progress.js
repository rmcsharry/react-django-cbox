import { GET_PROGRESS } from '../actions/types.js'

const initialState = {
  progress: {},
  organisation: {}, // TODO: provide different dashboards per organisation so this will store which is the 'current' one
}

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_PROGRESS:
      return {
        ...state,
        progress: action.payload,
      }
    default:
      return state
  }
}
