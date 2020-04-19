import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import styles from '../../static/assets/styles/main.scss';
import Layout from './Layout';
import Dashboard from './Dashboard';

import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div className={styles.App}>
          <Layout>
            <Dashboard />
          </Layout>
        </div>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
