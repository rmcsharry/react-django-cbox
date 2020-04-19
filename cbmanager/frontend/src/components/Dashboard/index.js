import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import SummaryCard from '../SummaryCard';
import styles from './styles.scss';

function Dashboard() {
  return (
    <div className={styles.wrapper}>
      <Row>
        <Col><SummaryCard title='Students' value='100'/></Col>
        <Col><SummaryCard title='Courses' value='8'/></Col>
        <Col><SummaryCard title='Certified' value='0'/></Col>
      </Row>
    </div>
  );
}

export default Dashboard;
