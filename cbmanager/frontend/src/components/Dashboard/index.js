import React, { Component } from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import SummaryCard from '../SummaryCard';
import styles from './styles.scss';
import { People } from 'react-bootstrap-icons';
import { Book } from 'react-bootstrap-icons';
import { Award } from 'react-bootstrap-icons';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getProgress } from '../../actions/progress';

export class Dashboard extends Component {
  static propTypes = {
    progress: PropTypes.object.isRequired
  }

  componentDidMount() {
    this.props.getProgress()
  }

  render() {
    return (
      <div className={styles.wrapper}>
        <Row xs={1} sm={3}>
          <Col>
            <SummaryCard title='Students' value='100' icon={<People />} />
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

const mapStateToProps = state => ({
  progress: state.progressReducer.progress
})

export default connect(mapStateToProps, { getProgress })(Dashboard)
