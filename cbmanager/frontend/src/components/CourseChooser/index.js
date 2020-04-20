import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { doFetchCourses, doChooseCourse } from '../../actions/courses'
import { COURSE_CHOSEN } from '../../actions/types'
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'
import PieBaker from '../PieBaker'

export class CoursesChooser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedValue: 0,
    }
    this.handleChoice = this.handleChoice.bind(this)
  }

  static propTypes = {
    courses: PropTypes.array.isRequired,
    fetchCourses: PropTypes.func.isRequired,
    chooseCourse: PropTypes.func.isRequired,
    allOption: PropTypes.shape({
      label: PropTypes.string,
      value: PropTypes.number
    })
  }

  componentDidMount() {
    this.props.fetchCourses()
    this.setState({
      selectedValue: this.props.defaultValue,
    })
  }

  handleChoice(selectedOption) {
    this.setState({ selectedValue: selectedOption.target.value })
    this.props.chooseCourse(selectedOption.target.value)
  }

  render() {
    const courseOptions = () => {
      return this.props.courses.map((course) => (
        <option key={course.id} value={course.id}>
          {course.language} | {course.level}
        </option>
      ))
    }

    return (
      <div>
        <Form>
          <Form.Group controlId='exampleForm.ControlSelect1'>
            <Form.Row>
              <Form.Label column='lg' xs={4} md={2}>
                Courses
              </Form.Label>
              <Col xs={8} md={4}>
                <Form.Control
                  as='select'
                  size='lg'
                  value={
                    this.props.courses.filter(
                      ({ id }) => id === this.state.selectedValue
                    ).id
                  }
                  onChange={this.handleChoice}
                >
                  <option value={this.props.allOption.value}>{this.props.allOption.label}</option>
                  {courseOptions()}
                </Form.Control>
              </Col>
            </Form.Row>
          </Form.Group>
        </Form>
        <PieBaker />
      </div>
    )
  }
}

const coursesSelector = (state) => state.coursesReducer.courses

const mapStateToProps = (state) => ({
  courses: coursesSelector(state),
  allOption: {
    label: "All courses",
    value: 0
  }
})

const mapDispatchToProps = {
  chooseCourse: doChooseCourse,
  fetchCourses: doFetchCourses
}

export default connect(mapStateToProps, mapDispatchToProps)(CoursesChooser)
