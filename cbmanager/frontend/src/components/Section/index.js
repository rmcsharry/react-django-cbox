import React from 'react'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import styles from './styles.scss'

function SectionHeader({text}) {
  return (
    <Row>
      <Col>
        <div className={`${styles.headerContainer} bg-primary`}>
          <h3>{text}</h3>
        </div>
      </Col>
    </Row>
  )
}

export default SectionHeader
