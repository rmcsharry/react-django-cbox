import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import SummaryCard from '../SummaryCard';
import styles from './styles.scss';
import { People } from 'react-bootstrap-icons';
import { Book } from 'react-bootstrap-icons';
import { Award } from 'react-bootstrap-icons';

function Dashboard() {
  return (
    <div className={styles.wrapper}>
      <Row xs={1} sm={3}>
        <Col>
          <SummaryCard title='Students' value='100' icon={<People />} />
        </Col>
        <Col>
          <SummaryCard title='Courses' value='8' icon={<Book />} />
        </Col>
        <Col>
          <SummaryCard title='Certified' value='0' icon={<Award />} />
        </Col>
      </Row>
    </div>
  );
}

export default Dashboard;
