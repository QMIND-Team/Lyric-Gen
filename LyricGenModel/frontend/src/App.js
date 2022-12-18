import React from 'react';
import logo from './logo.svg';
import {Container, Header, Button, Segment, Loader, Dimmer} from 'semantic-ui-react'
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading:false,
      genre:null,
      lyrics:null
    }
  }

  fakeUpload() {
    this.setState({loading:true});
    setTimeout(()=>this.setState({
      loading:false,
      genre:"Rap",
      lyrics:"Gucci Gang\nGucci Gang\nGucci Gang"
    }),1000);
  }

  render() {
    const {loading,genre,lyrics} = this.state;
    return (
      <Segment basic>
        <Container>
          <Header>
            Lyric Generator
          </Header>
          <p>
            Submit an instrumental audio file and see what our AI comes up with!
          </p>
          <Button onClick={()=>this.fakeUpload()}>Upload</Button>
          <Segment style={{minHeight:'300px'}}>
            <Loader active={loading}/>
            {(genre || lyrics) && <div>
              <Header>Genre</Header>
              <p>The detected genre is {genre}</p>
              <Header>Lyrics</Header>
              {lyrics.split("\n").map(lyric=><p key={lyric}>{lyric}</p>)}
            </div>
            }
          </Segment>
        </Container>
      </Segment>
    );
  }
}

export default App;
