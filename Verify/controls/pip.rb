# copyright: 2018, The Authors

title "Modules Of Python to Proyect Knight"

control 'Module Art' do
  impact 1
  title 'Moudule Art'
  desc ''
  describe pip('art') do
    it {should be_installed}
    its('version') { should eq '4.6' }
  end
end

control 'Module Urllib3' do
  impact 1
  title 'Moudule urllib3'
  desc ''
  describe pip('urllib3') do
    it {should be_installed}
    #its('version') { should eq '1.24.2' }
    its('version') { should eq '1.25.8' }
  end
end

control 'Moduule Rich' do
  impact 1
  title 'Moudle rich'
  desc ''
  describe pip('rich') do
    it {should be_installed}
    its('version') { should eq '1.0.3' }
  end
end

control 'Module Colorama' do
  impact 1
  title 'Moudule colorama'
  desc ''
  describe pip('colorama') do
    it {should be_installed}
    its('version') { should eq '0.4.3' }
  end
end

control 'Module Os' do
  impact 1
  title 'Moudule os'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/os.html'
  describe pip('os') do
    skip 'This module has been installed with python'
  end
end

control 'Module RE' do
  impact 1
  title 'Moudule re'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'
  describe pip('re') do
    skip 'This module has been installed with python'
  end
end

control 'Module Urllib' do
  impact 1
  title 'Module Urllib'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'
  describe pip('urllib') do
    skip 'This module has been installed with python'
  end
end

control 'Module Requests' do
  impact 1
  title 'Verify that module request are be installed'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'
  describe pip('requests') do
    it { should be_installed }
    #its('version') { should eq '2.20.0' }
    its('version') { should eq '2.22.0' }
  end
end
control 'Module netifaces' do
  impact 1
  title 'Verify that module request are be installed'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'
  describe pip('netifaces') do
    it { should be_installed }
    its('version') { should eq '0.10.9' }
  end
end
control 'Module Glob' do
  impact 1
  title 'Verify that module request are be installed'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'

  describe pip('glob') do
    skip 'This module has been installed with python'
  end
end

control 'Module Shutil' do
  impact 1
  title 'Verify that module request are be installed'
  desc ''

  ref 'Get more information in', url: 'https://docs.python.org/3.6/library/re.html'

  describe pip('shutil') do
    skip 'This module has been installed with python'
  end
end
