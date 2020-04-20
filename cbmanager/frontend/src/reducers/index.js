import { combineReducers } from 'redux'
import progressReducer from './progress'
import coursesReducer from './courses'

export default combineReducers({
  progressReducer,
  coursesReducer
})
