import React, { Component } from 'react'
import PieChart from '../PieChart'
import styles from './styles.scss'
import { connect } from 'react-redux'

export class PieBaker extends Component {
  render() {
    return (
      <div className={styles.pieWrapper}>
        <PieChart data={this.props.pieFilling}></PieChart>
      </div>
    )
  }
}

const reducer = (data) => {
  // this function takes the full set of results for all courses and accumulates the invdividual
  // metrics for each course into a totals object that will represent each slice of the pie
  return data.reduce(
    (prev, next) => {
      return {
        ontrack: (prev.ontrack += next.ontrack),
        slow: (prev.slow += next.slow),
        inactive: (prev.inactive += next.inactive),
        lapsed: (prev.lapsed += next.lapsed),
      }
    },
    { ontrack: 0, slow: 0, inactive: 0, lapsed: 0 }
  )
}

const bake = (courseData) => {
  // this function takes a single course record and transforms it
  // into the elements needed for the pie slices
  if (!courseData[0]) return []

  const filling = []
  Object.entries(courseData[0]).forEach(([key, value]) => {
    switch (key) {
      case 'ontrack':
      case 'slow':
      case 'inactive':
      case 'lapsed':
        filling.push({ id: key, label: key, value: value })
        break
      default:
        return null
    }
  })
  return filling
}

const bakePie = ({ progress, chosenCourse }) => {
  // this function determines whether we need to build the pie dataset for all courses, or just a chosen course
  // it then calls the bake function to bake the data for the pie :)
  if (chosenCourse == 0 && progress.results.length > 0) {
    return { pieFilling: bake([reducer(progress.results)]) }
  } else
    return {
      // NOTE item.course is a string (json from the API) whereas chosenChourse is a number
      pieFilling: bake(
        progress.results.filter((item) => item.course == chosenCourse)
      ),
    }
}

function mapStateToProps(state) {
  return bakePie(state.progressReducer)
}

export default connect(mapStateToProps)(PieBaker)
