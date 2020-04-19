import React, { Component } from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createSelector } from 'reselect'
import { getProgress } from '../../actions/progress';

import SummaryCard from '../SummaryCard';
import { People } from 'react-bootstrap-icons';
import { Book } from 'react-bootstrap-icons';
import { Award } from 'react-bootstrap-icons';
import styles from './styles.scss';

export class Dashboard extends Component {
  static propTypes = {
    progress: PropTypes.object.isRequired,
    getProgress: PropTypes.func.isRequired,
  }

  componentDidMount() {
    this.props.getProgress()
  }

  render() {
    return (
      <div className={styles.wrapper}>
        <Row xs={1} sm={3}>
          <Col>
            <SummaryCard title='Students' value={this.props.totalResults} icon={<People />} />
          </Col>
          <Col>
            <SummaryCard title='Courses' value={this.props.progress.count} icon={<Book />} />
          </Col>
          <Col>
            <SummaryCard title='Certified' value='0' icon={<Award />} />
          </Col>
        </Row>
      </div>
    )
  }
}

const progressSelector = state => state.progressReducer.progress

const totalResultsSelector = createSelector (
  progressSelector,
  progress => {
    if (!progress['results']) return 0
    console.log('results', progress['results'])
    const total = progress['results'].reduce((acc, result) => {
      acc + result['total']
    }, 0)
    console.log('total', total)
    return 100
  }
)

const mapStateToProps = state => ({
  progress: progressSelector(state),
  totalResults: totalResultsSelector(state)
})

export default connect(mapStateToProps, { getProgress })(Dashboard)
