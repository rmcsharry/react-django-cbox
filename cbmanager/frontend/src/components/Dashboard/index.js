import React, { Component } from 'react'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { createSelector } from 'reselect'
import { getProgress } from '../../actions/progress'

import SummaryCard from '../SummaryCard'
import { People } from 'react-bootstrap-icons'
import { Book } from 'react-bootstrap-icons'
import { Award } from 'react-bootstrap-icons'
import styles from './styles.scss'

export class Dashboard extends Component {
  static propTypes = {
    progress: PropTypes.object.isRequired,
    getProgress: PropTypes.func.isRequired,
    totalResults: PropTypes.number.isRequired,
  }

  componentDidMount() {
    this.props.getProgress()
  }

  render() {
    return (
      <div className={styles.wrapper}>
        <Row className="justify-content-center">
          
          <div className={styles.titleContainer}>
            <img
              src='/static/legologo.jpeg'
              width='30'
              height='30'
              className='d-inline-block align-middle'
              alt='Dashboard Logo'
            />
              <h2 className={styles.title}>AEKI Dashboard</h2>
          </div>
          
        </Row>
        <Row xs={1} sm={3}>
          <Col>
            <SummaryCard
              title='Students'
              value={this.props.totalResults}
              icon={<People />}
            />
          </Col>
          <Col>
            <SummaryCard
              title='Courses'
              value={this.props.progress.count}
              icon={<Book />}
            />
          </Col>
          <Col>
            <SummaryCard title='Certified' value='0' icon={<Award />} />
          </Col>
        </Row>
      </div>
    )
  }
}

const progressSelector = (state) => state.progressReducer.progress

const totalResultsSelector = createSelector(progressSelector, (progress) => {
  if (!progress.results) return 0
  const total = progress.results.reduce((acc, result) => {
    return acc + result.total
  }, 0)
  return total
})

const mapStateToProps = (state) => ({
  progress: progressSelector(state),
  totalResults: totalResultsSelector(state),
})

export default connect(mapStateToProps, { getProgress })(Dashboard)
