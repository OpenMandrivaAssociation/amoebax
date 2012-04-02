Name:		amoebax
Version:	0.2.0
Release:	%mkrel 1
Summary:	Action-Puzzle Game
Group:		Games/Puzzles
License:	GPLv2+ and Free Art
URL:		http://www.emma-soft.com/games/amoebax/
Source0:	http://www.emma-soft.com/games/amoebax/download/%{name}-%{version}.tar.bz2
Patch0:		amoebax-0.2.0-gcc43.patch
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	zlib-devel
BuildRequires:	png-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	doxygen

%description
Amoebax is a cute and addictive action-puzzle game. Due an awful mutation,
some amoeba's species have started to multiply until they take the world if
you can't stop them. Fortunately the mutation made then too unstable and
lining up four or more will make them disappear.

Follow Kim or Tom through 6 levels in their quest to prevent the cute
multiplying amoebas to take the world and become the new Amoeba Master. Watch
out for the cute but amoeba's controlled creatures that will try to put and
end to your quest.

Amoebax is designed with levels for everyone, from children to adults. With
the training mode everybody will quickly become a master and the tournament
mode will let you have a good time with your friends. There is also catchy
music, funny sound effects, and beautiful screens that sure appeal to everyone
in the family.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
%__cp %{buildroot}%{_datadir}/pixmaps/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/

%__rm %{buildroot}%{_defaultdocdir}/%{name}/manual.pdf

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS COPYING* NEWS README* THANKS TODO doc/manual.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man6/%{name}.6.*

