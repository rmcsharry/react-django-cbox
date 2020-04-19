import { GET_PROGRESS } from '../actions/types.js';

const initialState = {
  progress: {}
}

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_PROGRESS:
      return {
        ...state,
        progress: action.payload
      }
    default:
      return state
  }
}
