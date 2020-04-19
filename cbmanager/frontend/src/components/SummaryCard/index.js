import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import styles from './styles.scss';

function SummaryCard({title, value}) {
  return (
    <div className={styles.wrapper}>
      <Row>
        <Col>
          <h1>{value}</h1>
        </Col>
      </Row>
      <Row>
        <Col>
          <h3>{title}</h3>
        </Col>
        <Col>IMG</Col>
      </Row>
    </div>
  );
}

export default SummaryCard;
