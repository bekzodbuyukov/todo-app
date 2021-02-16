import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import axios from 'axios';


class App extends Component {
  state = {
    todos: []
  }

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://127.0.0.1:8000/api/v1/todos/?format=json')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      // <div className="App">
      //   <header className="App-header">
      //     <img src={logo} className="App-logo" alt="logo" />
      //     <p>
      //       Edit <code>src/App.js</code> and save to reload.
      //     </p>
      //     <a
      //       className="App-link"
      //       href="https://reactjs.org"
      //       target="_blank"
      //       rel="noopener noreferrer"
      //     >
      //       Learn React
      //     </a>
      //   </header>
      // </div>
      <main class="flex-shrink-0">
        <div class="container">
          <h1 class="mt-5">Todos</h1>

          {this.state.todos.map(item => (
            <div key={item.id}>
              <h2 class="mt-5">{item.title}</h2>
              <p class="lead">{item.description}</p>
              <p>Created: {item.created_date}</p>
              <p>Deadline: {item.deadline_date}</p>
            </div>
          ))}
                  
        </div>
      </main>
    );
  }

}


export default App;
