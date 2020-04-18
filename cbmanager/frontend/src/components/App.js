import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import styles from '../../static/assets/styles/main.scss';
import Layout from './Layout';
import Dashboard from './Dashboard';

class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <Layout>
          <Dashboard />
        </Layout>
      </div>
    );
  }
}
ReactDOM.render(<App />, document.getElementById('app'));
